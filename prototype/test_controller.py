"""Tests for the minimal Deliberation Room controller."""

from controller import Action, NextMoveController
from state import (
    CognitiveObject,
    DeliberationState,
    EpistemicStatus,
    Provenance,
    Stability,
)


def make_object(content: str) -> CognitiveObject:
    """Create a human-confirmed cognitive object for tests."""

    return CognitiveObject(
        content=content,
        epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
        provenance=Provenance.HUMAN_ORIGINATED,
        confidence=1.0,
    )


def test_assumption_prefers_counterexample():
    """An explicit assumption should make COUNTEREXAMPLE highly ranked."""

    state = DeliberationState()

    state.cognitive.assumptions.append(
        make_object(
            "If the law were morally acceptable, "
            "the central problem would disappear."
        )
    )

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    assert decision.selected.action == Action.COUNTEREXAMPLE


def test_contradiction_prefers_distinguish():
    """A visible contradiction should favor DISTINGUISH."""

    state = DeliberationState()

    state.cognitive.contradictions.append(
        make_object(
            "The user says equal effort does not matter, "
            "but also says unequal effort is the problem."
        )
    )

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    assert decision.selected.action == Action.DISTINGUISH


def test_unresolved_question_prefers_clarify():
    """An unresolved question should favor CLARIFY."""

    state = DeliberationState()

    state.cognitive.unresolved_questions.append(
        make_object(
            "What does the user mean by 'dramatic'?"
        )
    )

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    assert decision.selected.action == Action.CLARIFY


def test_claim_without_other_state_requests_evidence():
    """A claim without visible support should favor REQUEST_EVIDENCE."""

    state = DeliberationState()

    state.record_human_claim(
        "Creon's authority makes him unable to revise his judgment."
    )

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    assert decision.selected.action == Action.REQUEST_EVIDENCE


def test_composition_request_overrides_deliberation():
    """Explicit human request for composition should take priority."""

    state = DeliberationState()

    state.record_human_claim(
        "I know what I mean and want help drafting it."
    )

    state.cognitive.assumptions.append(
        make_object(
            "The recipient will understand the distinction."
        )
    )

    state.composition_requested = True

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    assert (
        decision.selected.action
        == Action.TRANSITION_TO_COMPOSITION
    )


def test_withhold_is_always_available():
    """WITHHOLD should remain available as a legitimate action."""

    state = DeliberationState()

    state.record_human_claim(
        "The current model is reasonably stable."
    )

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    actions = {
        candidate.action
        for candidate in decision.candidates
    }

    assert Action.WITHHOLD in actions


def test_stable_state_includes_withhold():
    """Moderate stability should explicitly introduce WITHHOLD."""

    state = DeliberationState()

    state.cognitive.conceptual_stability = Stability.MODERATE

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    actions = {
        candidate.action
        for candidate in decision.candidates
    }

    assert Action.WITHHOLD in actions


def test_empty_state_selects_withhold():
    """With no justified cognitive target, the controller should withhold."""

    state = DeliberationState()

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    assert decision.selected.action == Action.WITHHOLD


def test_candidate_set_is_inspectable():
    """Policy decisions should preserve the ranked candidate set."""

    state = DeliberationState()

    state.cognitive.assumptions.append(
        make_object(
            "Changing one's mind always weakens authority."
        )
    )

    controller = NextMoveController()
    decision = controller.select_next_move(state)

    assert len(decision.candidates) >= 2

    assert (
        decision.candidates[0].action
        == decision.selected.action
    )


def test_system_does_not_relabel_human_origin():
    """Human cognitive content should remain human-originated."""

    state = DeliberationState()

    state.record_human_claim(
        "Being noticed is not the same as being included."
    )

    claim = state.cognitive.current_claims[0]

    assert (
        claim.provenance
        == Provenance.HUMAN_ORIGINATED
    )


def test_human_claim_is_observed_not_inferred():
    """Explicit human claims should retain observed epistemic status."""

    state = DeliberationState()

    state.record_human_claim(
        "I think the distinction is about authority."
    )

    claim = state.cognitive.current_claims[0]

    assert (
        claim.epistemic_status
        == EpistemicStatus.OBSERVED
    )
