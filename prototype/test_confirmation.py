"""Tests for the Deliberation Room human-confirmation gate."""

from confirmation import (
    ConfirmationDecision,
    ConfirmationGate,
)
from extractor import (
    ExtractionCandidate,
    ExtractionType,
)
from state import (
    DeliberationState,
    EpistemicStatus,
    Provenance,
)


def make_inferred_candidate(
    extraction_type: ExtractionType,
    content: str,
) -> ExtractionCandidate:
    """Create a system-inferred candidate for confirmation tests."""

    return ExtractionCandidate(
        extraction_type=extraction_type,
        content=content,
        source_text="source human language",
        epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
        provenance=Provenance.SYSTEM_PROPOSED,
        confidence=0.7,
        rationale="test inference",
    )


def test_inferred_candidate_requires_confirmation():
    """System-inferred content should require human review."""

    candidate = make_inferred_candidate(
        ExtractionType.ASSUMPTION,
        "Changing one's mind weakens authority.",
    )

    assert ConfirmationGate.requires_confirmation(candidate)


def test_observed_human_claim_does_not_require_confirmation():
    """Literal human-originated content should not require re-confirmation."""

    candidate = ExtractionCandidate(
        extraction_type=ExtractionType.CLAIM,
        content="The problem is authority.",
        source_text="The problem is authority.",
        epistemic_status=EpistemicStatus.OBSERVED,
        provenance=Provenance.HUMAN_ORIGINATED,
        confidence=1.0,
    )

    assert not ConfirmationGate.requires_confirmation(candidate)


def test_confirmed_assumption_enters_active_state():
    """Confirmed system inference should enter active state."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.ASSUMPTION,
        "Changing one's mind weakens authority.",
    )

    result = gate.confirm(
        state=state,
        candidate=candidate,
    )

    assert result.decision == ConfirmationDecision.CONFIRM
    assert len(state.cognitive.assumptions) == 1

    assumption = state.cognitive.assumptions[0]

    assert (
        assumption.epistemic_status
        == EpistemicStatus.HUMAN_CONFIRMED
    )

    assert (
        assumption.provenance
        == Provenance.SYSTEM_PROPOSED_HUMAN_RECOGNIZED
    )


def test_confirmation_records_recognition_event():
    """Confirmation should be visible in the deliberation trace."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.CLAIM,
        "The problem may be authority rather than law.",
    )

    result = gate.confirm(
        state=state,
        candidate=candidate,
    )

    event = state.trace[result.trace_event_id]

    assert event.actor == "human"
    assert event.event_type == "recognition"

    assert (
        event.provenance
        == Provenance.SYSTEM_PROPOSED_HUMAN_RECOGNIZED
    )


def test_revised_candidate_uses_human_revision():
    """Human revision should replace the inferred wording/content."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.ASSUMPTION,
        "Changing one's mind weakens authority.",
    )

    revised_content = (
        "The issue is not weakness; the argument assumes public revision "
        "undermines legitimacy."
    )

    result = gate.revise(
        state=state,
        candidate=candidate,
        revised_content=revised_content,
    )

    assert result.decision == ConfirmationDecision.REVISE
    assert result.final_content == revised_content

    assert len(state.cognitive.assumptions) == 1

    assumption = state.cognitive.assumptions[0]

    assert assumption.content == revised_content

    assert (
        assumption.provenance
        == Provenance.SYSTEM_PROPOSED_HUMAN_REVISED
    )

    assert (
        assumption.epistemic_status
        == EpistemicStatus.HUMAN_CONFIRMED
    )


def test_revision_records_revision_event():
    """A human revision of system inference should remain traceable."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.CLAIM,
        "The relationship problem is lack of attention.",
    )

    result = gate.revise(
        state=state,
        candidate=candidate,
        revised_content=(
            "The issue is not lack of attention; it is lack of inclusion "
            "in decisions that affect both people."
        ),
    )

    event = state.trace[result.trace_event_id]

    assert event.event_type == "revision"

    assert (
        event.provenance
        == Provenance.SYSTEM_PROPOSED_HUMAN_REVISED
    )


def test_rejected_candidate_does_not_enter_active_state():
    """Rejected inference must not become active cognitive state."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.ASSUMPTION,
        "The user believes the recipient does not care.",
    )

    result = gate.reject(
        state=state,
        candidate=candidate,
        explanation=(
            "No. I do not know what the recipient feels or intends."
        ),
    )

    assert result.decision == ConfirmationDecision.REJECT
    assert state.cognitive.assumptions == []


def test_rejection_is_preserved_in_trace():
    """Rejected inference should remain as useful provenance evidence."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.CONTRADICTION,
        "The user's two claims appear inconsistent.",
    )

    result = gate.reject(
        state=state,
        candidate=candidate,
        explanation=(
            "They are not inconsistent because they refer to different cases."
        ),
    )

    event = state.trace[result.trace_event_id]

    assert event.actor == "human"
    assert event.event_type == "rejection"

    assert (
        event.provenance
        == Provenance.SYSTEM_PROPOSED_HUMAN_REJECTED
    )

    assert (
        event.epistemic_status
        == EpistemicStatus.HUMAN_REJECTED
    )


def test_confirmed_uncertainty_routes_correctly():
    """Confirmed uncertainty should enter the uncertainty state."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.UNCERTAINTY,
        "Whether the claim generalizes beyond this case.",
    )

    gate.confirm(
        state=state,
        candidate=candidate,
    )

    assert len(state.cognitive.uncertainty) == 1

    assert (
        state.cognitive.uncertainty[0].content
        == "Whether the claim generalizes beyond this case."
    )


def test_confirmed_unresolved_question_routes_correctly():
    """Confirmed unresolved questions should enter the correct state."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.UNRESOLVED_QUESTION,
        "What does the user mean by 'dramatic'?",
    )

    gate.confirm(
        state=state,
        candidate=candidate,
    )

    assert len(state.cognitive.unresolved_questions) == 1


def test_confirmation_does_not_preserve_system_inferred_status():
    """Once confirmed, epistemic status should reflect human confirmation."""

    state = DeliberationState()
    gate = ConfirmationGate()

    candidate = make_inferred_candidate(
        ExtractionType.CLAIM,
        "The issue may concern authority.",
    )

    gate.confirm(
        state=state,
        candidate=candidate,
    )

    claim = state.cognitive.current_claims[0]

    assert (
        claim.epistemic_status
        != EpistemicStatus.SYSTEM_INFERRED
    )

    assert (
        claim.epistemic_status
        == EpistemicStatus.HUMAN_CONFIRMED
    )
