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
    assert result.pending_confirmation == []
    assert result.requires_human_confirmation is False


def test_apply_extraction_adds_observed_claim_to_active_state():
    """Observed human content should enter active cognitive state."""

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

    updated = apply_extraction(
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

    assert len(updated.candidates) == 1
    assert updated.pending_confirmation == []
    assert updated.requires_human_confirmation is False


def test_inferred_assumption_stays_pending():
    """System inference should not enter active cognitive state."""

    state = DeliberationState()

    inferred = ExtractionCandidate(
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

    result = ExtractionResult(
        raw_text=(
            "I don't know if the law is really the problem."
        ),
        candidates=[inferred],
    )

    updated = apply_extraction(
        state=state,
        result=result,
    )

    assert state.cognitive.assumptions == []
    assert updated.candidates == []
    assert len(updated.pending_confirmation) == 1
    assert updated.pending_confirmation[0] == inferred
    assert updated.requires_human_confirmation is True


def test_inferred_claim_stays_pending():
    """System-proposed claims should require review before policy can use them."""

    state = DeliberationState()

    inferred = ExtractionCandidate(
        extraction_type=ExtractionType.CLAIM,
        content="The deeper issue may be authority rather than law.",
        source_text="Maybe it isn't really about the law.",
        epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
        provenance=Provenance.SYSTEM_PROPOSED,
        confidence=0.65,
    )

    result = ExtractionResult(
        raw_text="Maybe it isn't really about the law.",
        candidates=[inferred],
    )

    updated = apply_extraction(
        state=state,
        result=result,
    )

    assert state.cognitive.current_claims == []
    assert len(updated.pending_confirmation) == 1
    assert updated.requires_human_confirmation is True


def test_inferred_uncertainty_stays_pending():
    """Inferred uncertainty should not be silently treated as human uncertainty."""

    state = DeliberationState()

    inferred = ExtractionCandidate(
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

    result = ExtractionResult(
        raw_text=(
            "I'm not sure whether that conclusion generalizes."
        ),
        candidates=[inferred],
    )

    updated = apply_extraction(
        state=state,
        result=result,
    )

    assert state.cognitive.uncertainty == []
    assert len(updated.pending_confirmation) == 1


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


def test_mixed_extraction_routes_observed_and_inferred_differently():
    """Observed content should activate while inferred content waits."""

    state = DeliberationState()

    observed = ExtractionCandidate(
        extraction_type=ExtractionType.CLAIM,
        content="I think the law matters.",
        source_text="I think the law matters.",
        epistemic_status=EpistemicStatus.OBSERVED,
        provenance=Provenance.HUMAN_ORIGINATED,
        confidence=1.0,
    )

    inferred = ExtractionCandidate(
        extraction_type=ExtractionType.ASSUMPTION,
        content=(
            "The claim may assume the moral quality of the law "
            "is the decisive variable."
        ),
        source_text="I think the law matters.",
        epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
        provenance=Provenance.SYSTEM_PROPOSED,
        confidence=0.5,
    )

    result = ExtractionResult(
        raw_text="I think the law matters.",
        candidates=[
            observed,
            inferred,
        ],
    )

    updated = apply_extraction(
        state=state,
        result=result,
    )

    assert len(state.cognitive.current_claims) == 1
    assert state.cognitive.assumptions == []

    assert len(updated.candidates) == 1
    assert updated.candidates[0] == observed

    assert len(updated.pending_confirmation) == 1
    assert updated.pending_confirmation[0] == inferred


def test_pending_confirmation_sets_confirmation_flag():
    """Any pending inferred candidate should raise the review flag."""

    state = DeliberationState()

    inferred = ExtractionCandidate(
        extraction_type=ExtractionType.UNRESOLVED_QUESTION,
        content="What does 'dramatic' mean here?",
        source_text="Every version sounds dramatic.",
        epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
        provenance=Provenance.SYSTEM_PROPOSED,
        confidence=0.7,
    )

    result = ExtractionResult(
        raw_text="Every version sounds dramatic.",
        candidates=[inferred],
    )

    updated = apply_extraction(
        state=state,
        result=result,
    )

    assert updated.requires_human_confirmation is True


def test_existing_pending_candidates_are_preserved():
    """Applying extraction should not discard already-pending review items."""

    state = DeliberationState()

    pending = ExtractionCandidate(
        extraction_type=ExtractionType.ASSUMPTION,
        content="Existing pending inference.",
        source_text="Earlier human language.",
        epistemic_status=EpistemicStatus.SYSTEM_INFERRED,
        provenance=Provenance.SYSTEM_PROPOSED,
        confidence=0.5,
    )

    observed = ExtractionCandidate(
        extraction_type=ExtractionType.CLAIM,
        content="New observed claim.",
        source_text="New observed claim.",
        epistemic_status=EpistemicStatus.OBSERVED,
        provenance=Provenance.HUMAN_ORIGINATED,
        confidence=1.0,
    )

    result = ExtractionResult(
        raw_text="New observed claim.",
        candidates=[observed],
        pending_confirmation=[pending],
        requires_human_confirmation=True,
    )

    updated = apply_extraction(
        state=state,
        result=result,
    )

    assert len(updated.pending_confirmation) == 1
    assert updated.pending_confirmation[0] == pending
    assert updated.requires_human_confirmation is True
