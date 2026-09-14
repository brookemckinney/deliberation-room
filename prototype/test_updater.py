"""Tests for the minimal Deliberation Room state updater."""

from controller import Action
from state import (
    DeliberationState,
    EpistemicStatus,
    Provenance,
    Stability,
)
from updater import StateUpdater


def test_human_response_is_observed():
    """A direct human response should be recorded as observed."""

    state = DeliberationState()
    updater = StateUpdater()

    event_id = updater.record_human_response(
        state=state,
        system_action=Action.CLARIFY,
        system_event_id=0,
        response_text="I mean the wording is too strong.",
        response_type="response_only",
    )

    event = state.trace[event_id]

    assert event.actor == "human"
    assert event.epistemic_status == EpistemicStatus.OBSERVED
    assert event.triggered_by == 0


def test_human_distinction_remains_human_originated():
    """A system-triggered distinction should still retain human provenance."""

    state = DeliberationState()
    updater = StateUpdater()

    event_id = updater.add_human_distinction(
        state=state,
        content="being noticed is not the same as being included",
        triggered_by=4,
    )

    event = state.trace[event_id]

    assert event.event_type == "distinction"
    assert event.provenance == Provenance.HUMAN_ORIGINATED
    assert event.triggered_by == 4


def test_human_revision_replaces_current_claim():
    """A human revision should replace the most recent active claim."""

    state = DeliberationState()
    updater = StateUpdater()

    state.record_human_claim(
        "The problem is that the law is unjust."
    )

    updater.revise_current_claim(
        state=state,
        revised_content=(
            "The deeper problem is that Creon's model of authority "
            "makes correction impossible."
        ),
        triggered_by=1,
    )

    assert len(state.cognitive.current_claims) == 1

    claim = state.cognitive.current_claims[0]

    assert (
        claim.content
        == "The deeper problem is that Creon's model of authority "
        "makes correction impossible."
    )
    assert claim.provenance == Provenance.HUMAN_ORIGINATED
    assert (
        claim.epistemic_status
        == EpistemicStatus.HUMAN_CONFIRMED
    )


def test_revision_event_links_to_system_trigger():
    """The trace should preserve which move triggered a revision."""

    state = DeliberationState()
    updater = StateUpdater()

    state.record_human_claim("Initial claim")

    event_id = updater.revise_current_claim(
        state=state,
        revised_content="Revised claim",
        triggered_by=7,
    )

    event = state.trace[event_id]

    assert event.event_type == "revision"
    assert event.triggered_by == 7


def test_add_assumption_updates_state_and_trace():
    """A human-identified assumption should enter both state and trace."""

    state = DeliberationState()
    updater = StateUpdater()

    event_id = updater.add_assumption(
        state=state,
        content="Changing one's mind always weakens authority.",
        triggered_by=2,
    )

    assert len(state.cognitive.assumptions) == 1

    assumption = state.cognitive.assumptions[0]

    assert (
        assumption.content
        == "Changing one's mind always weakens authority."
    )
    assert assumption.provenance == Provenance.HUMAN_ORIGINATED

    event = state.trace[event_id]

    assert event.event_type == "assumption"
    assert event.triggered_by == 2


def test_add_uncertainty_preserves_uncertainty():
    """Human uncertainty should remain explicit rather than being resolved."""

    state = DeliberationState()
    updater = StateUpdater()

    updater.add_uncertainty(
        state=state,
        content=(
            "I am not sure whether Sophocles intends this as a "
            "general political claim."
        ),
        triggered_by=3,
    )

    assert len(state.cognitive.uncertainty) == 1

    uncertainty = state.cognitive.uncertainty[0]

    assert (
        uncertainty.epistemic_status
        == EpistemicStatus.HUMAN_CONFIRMED
    )


def test_rejection_records_system_proposal_as_rejected():
    """Human rejection should not erase the system proposal's provenance."""

    state = DeliberationState()
    updater = StateUpdater()

    event_id = updater.reject_system_move(
        state=state,
        explanation=(
            "The idea is too strong. I do not mean that I feel abandoned."
        ),
        triggered_by=5,
    )

    event = state.trace[event_id]

    assert event.event_type == "rejection"

    assert (
        event.provenance
        == Provenance.SYSTEM_PROPOSED_HUMAN_REJECTED
    )

    assert (
        event.epistemic_status
        == EpistemicStatus.HUMAN_REJECTED
    )

    assert event.triggered_by == 5


def test_resolve_assumption_removes_latest_assumption():
    """Resolved assumptions should leave the active assumption set."""

    state = DeliberationState()
    updater = StateUpdater()

    updater.add_assumption(
        state=state,
        content="Assumption one",
        triggered_by=0,
    )

    updater.add_assumption(
        state=state,
        content="Assumption two",
        triggered_by=1,
    )

    updater.resolve_assumption(state)

    assert len(state.cognitive.assumptions) == 1

    assert (
        state.cognitive.assumptions[0].content
        == "Assumption one"
    )


def test_resolve_contradiction_removes_latest_contradiction():
    """Resolved contradictions should leave the active set."""

    state = DeliberationState()
    updater = StateUpdater()

    from state import CognitiveObject

    state.cognitive.contradictions.append(
        CognitiveObject(
            content="Contradiction",
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
        )
    )

    updater.resolve_contradiction(state)

    assert state.cognitive.contradictions == []


def test_resolve_question_removes_latest_question():
    """Resolved questions should leave the unresolved-question set."""

    state = DeliberationState()
    updater = StateUpdater()

    from state import CognitiveObject

    state.cognitive.unresolved_questions.append(
        CognitiveObject(
            content="What does dramatic mean here?",
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
        )
    )

    updater.resolve_question(state)

    assert state.cognitive.unresolved_questions == []


def test_stability_can_be_updated():
    """Conceptual stability should remain explicitly changeable."""

    state = DeliberationState()
    updater = StateUpdater()

    updater.set_stability(
        state,
        Stability.MODERATE,
    )

    assert (
        state.cognitive.conceptual_stability
        == Stability.MODERATE
    )
