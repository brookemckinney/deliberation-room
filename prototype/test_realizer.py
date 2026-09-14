"""Tests for the Deliberation Room template realizer."""

from controller import Action, CandidateMove
from realizer import MoveRealizer
from state import DeliberationState


def make_move(
    action: Action,
    target: str | None = None,
) -> CandidateMove:
    """Create a minimal candidate move for realization tests."""

    return CandidateMove(
        action=action,
        target=target,
        rationale="test",
        expected_cognitive_value="moderate",
        expected_information_gain="moderate",
        cognitive_substitution_risk="low",
    )


def test_withhold_emits_no_language():
    """WITHHOLD must remain a real no-output policy action."""

    state = DeliberationState()
    realizer = MoveRealizer()

    result = realizer.realize(
        make_move(Action.WITHHOLD),
        state,
    )

    assert result.action == Action.WITHHOLD
    assert result.text is None
    assert result.is_silent()


def test_clarify_realizes_selected_action():
    """CLARIFY should produce clarification language."""

    state = DeliberationState()
    realizer = MoveRealizer()

    result = realizer.realize(
        make_move(
            Action.CLARIFY,
            "What does 'dramatic' mean here?",
        ),
        state,
    )

    assert result.action == Action.CLARIFY
    assert result.text is not None
    assert "make sure" in result.text.lower()


def test_distinguish_does_not_supply_distinction():
    """The template should ask for a distinction rather than invent one."""

    state = DeliberationState()
    realizer = MoveRealizer()

    target = "Two claims appear to conflict."

    result = realizer.realize(
        make_move(
            Action.DISTINGUISH,
            target,
        ),
        state,
    )

    assert result.action == Action.DISTINGUISH
    assert result.text is not None
    assert "what distinction" in result.text.lower()
    assert target in result.text


def test_request_evidence_preserves_target():
    """Evidence requests should remain anchored to the selected target."""

    state = DeliberationState()
    realizer = MoveRealizer()

    target = "Creon's model of authority prevents revision."

    result = realizer.realize(
        make_move(
            Action.REQUEST_EVIDENCE,
            target,
        ),
        state,
    )

    assert result.text is not None
    assert target in result.text


def test_counterexample_template_preserves_human_generation():
    """The v0.1 template asks the human to generate the counterexample."""

    state = DeliberationState()
    realizer = MoveRealizer()

    target = "Changing one's mind always weakens authority."

    result = realizer.realize(
        make_move(
            Action.COUNTEREXAMPLE,
            target,
        ),
        state,
    )

    assert result.action == Action.COUNTEREXAMPLE
    assert result.text is not None
    assert "construct a case" in result.text.lower()
    assert target in result.text


def test_reflect_uses_existing_human_claim():
    """Reflection should expose represented human content."""

    state = DeliberationState()
    state.record_human_claim(
        "Being noticed is not the same as being included."
    )

    realizer = MoveRealizer()

    result = realizer.realize(
        make_move(Action.REFLECT),
        state,
    )

    assert result.text is not None
    assert (
        "Being noticed is not the same as being included."
        in result.text
    )


def test_reflect_does_not_invent_content_when_state_empty():
    """An empty state should not produce a fabricated reflection."""

    state = DeliberationState()
    realizer = MoveRealizer()

    result = realizer.realize(
        make_move(Action.REFLECT),
        state,
    )

    assert result.text is not None
    assert "not enough human-confirmed state" in result.text.lower()


def test_composition_transition_is_explicit():
    """Composition should remain an explicit policy transition."""

    state = DeliberationState()
    realizer = MoveRealizer()

    result = realizer.realize(
        make_move(
            Action.TRANSITION_TO_COMPOSITION,
        ),
        state,
    )

    assert (
        result.action
        == Action.TRANSITION_TO_COMPOSITION
    )

    assert result.text is not None
    assert "composition" in result.text.lower()


def test_realization_source_is_template():
    """The prototype should expose where realization came from."""

    state = DeliberationState()
    realizer = MoveRealizer()

    result = realizer.realize(
        make_move(Action.CLARIFY),
        state,
    )

    assert result.realization_source == "template"
