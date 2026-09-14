"""Tests for the Deliberation Room state extraction contract."""

from extractor import (
    ExtractionCandidate,
    ExtractionResult,
    ExtractionType,
    ManualStateExtractor,
    apply_extraction,
)
from state import (
    DeliberationState,
    EpistemicStatus,
    Provenance,
)


def test_manual_extractor_preserves_literal_human_text():
    """The no-inference extractor should preserve the human's wording."""

    state = DeliberationState()
    extractor = ManualStateExtractor()

    text = "I don't know if the law is really the problem."

    result = extractor.extract(
        text=text,
        state=state,
    )

    assert result.raw_text == text
    assert len(result.candidates) == 1

    candidate = result.candidates[0]

    assert candidate.content == text
    assert candidate.source_text == text


def test_manual_extractor_marks_literal_content_observed():
    """Literal human language should be marked observed, not inferred."""

    state = DeliberationState()
    extractor = ManualStateExtractor()

    result = extractor.extract(
        text="Creon's problem is the law.",
        state=state,
    )

    candidate = result.candidates[0]

    assert (
        candidate.epistemic_status
        == EpistemicStatus.OBSERVED
    )


def test_manual_extractor_preserves_human_origin():
    """Literal human contribution should remain human-originated."""

    state = DeliberationState()
    extractor = ManualStateExtractor()

    result = extractor.extract(
        text="Being noticed is not the same as being included.",
        state=state,
    )

    candidate = result.candidates[0]

    assert (
        candidate.provenance
        == Provenance.HUMAN_ORIGINATED
    )


def test_manual_extractor_does_not_infer_assumption():
    """The conservative baseline should not manufacture hidden assumptions."""

    state = DeliberationState()
    extractor = ManualStateExtractor()

    result = extractor.extract(
        text="I don't know if the law is really the problem.",
        state=state,
    )

    extraction_types = {
        candidate.extraction_type
        for candidate in result.candidates
    }

    assert ExtractionType.ASSUMPTION not in extraction_types
    assert ExtractionType.CONTRADICTION not in extraction_types
    assert ExtractionType.UNCERTAINTY not in extraction_types


def test_empty_input_produces_no_candidate():
    """Empty human input should not create synthetic state."""

    state = DeliberationState()
    extractor = ManualStateExtractor()

    result = extractor.extract(
        text="   ",
        state=state,
    )

    assert result.candidates == []
    assert result.requires_human_confirmation is False


def test_apply_extraction_adds_claim_to_state():
    """A claim extraction should enter the active claim state."""

    state = DeliberationState()

    result = ExtractionResult(
        raw_text="The problem is authority.",
        candidates=[
            ExtractionCandidate(
                extraction_type=ExtractionType.CLAIM,
                content="The problem is authority.",
                source_text="The problem is authority.",
                epistemic_status=EpistemicStatus.OBSERVED,
                provenance=Provenance.HUMAN_ORIGINATED,
                confidence=1.0,
            )
        ],
    )

    apply_extraction(
        state=state,
        result=result,
    )

    assert len(state.cognitive.current_claims) == 1

    claim = state.cognitive.current_claims[0]

    assert claim.content == "The problem is authority."
    assert (
        claim.epistemic_status
        == EpistemicStatus.OBSERVED
    )
    assert (
        claim.provenance
        == Provenance.HUMAN_ORIGINATED
    )


def test_apply_extraction_preserves_inferred_status():
    """System inference must not be promoted into human confirmation."""

    state = DeliberationState()

    result = ExtractionResult(
        raw_text="I don't know if the law is really the problem.",
        candidates=[
            ExtractionCandidate(
                extraction_type=ExtractionType.ASSUMPTION,
                content=(
                    "The current interpretation may depend on treating "
                    "the moral quality of the law as the central variable."
                ),
                source_text=(
                    "I don't know if the law is really the problem."
                ),
                epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
                provenance=Provenance.SYSTEM_PROPOSED,
                confidence=0.55,
                rationale="Candidate inference for inspection.",
            )
        ],
        requires_human_confirmation=True,
    )

    apply_extraction(
        state=state,
        result=result,
    )

    assumption = state.cognitive.assumptions[0]

    assert (
        assumption.epistemic_status
        == EpistemicStatus.SYSTEM_INFERRED
    )

    assert (
        assumption.provenance
        == Provenance.SYSTEM_PROPOSED
    )


def test_apply_extraction_routes_uncertainty_correctly():
    """Uncertainty candidates should enter the uncertainty state."""

    state = DeliberationState()

    result = ExtractionResult(
        raw_text="I'm not sure whether that conclusion generalizes.",
        candidates=[
            ExtractionCandidate(
                extraction_type=ExtractionType.UNCERTAINTY,
                content=(
                    "Whether the conclusion generalizes beyond this case."
                ),
                source_text=(
                    "I'm not sure whether that conclusion generalizes."
                ),
                epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
                provenance=Provenance.SYSTEM_PROPOSED,
                confidence=0.8,
            )
        ],
    )

    apply_extraction(
        state=state,
        result=result,
    )

    assert len(state.cognitive.uncertainty) == 1

    assert (
        state.cognitive.uncertainty[0].content
        == "Whether the conclusion generalizes beyond this case."
    )


def test_inferred_candidate_keeps_source_text():
    """Every inferred representation should remain traceable to its source."""

    candidate = ExtractionCandidate(
        extraction_type=ExtractionType.CONTRADICTION,
        content="Two represented claims may conflict.",
        source_text=(
            "Equal effort doesn't matter, but the unequal effort "
            "is what keeps bothering me."
        ),
        epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
        provenance=Provenance.SYSTEM_PROPOSED,
        confidence=0.6,
    )

    assert candidate.source_text
    assert (
        candidate.epistemic_status
        == EpistemicStatus.SYSTEM_INFERRED
    )


def test_extraction_can_require_human_confirmation():
    """Ambiguous inferred state should be able to require confirmation."""

    result = ExtractionResult(
        raw_text="Maybe it's not really about the law.",
        candidates=[],
        requires_human_confirmation=True,
        extraction_notes=[
            "Potential distinction requires human confirmation."
        ],
    )

    assert result.requires_human_confirmation is True
