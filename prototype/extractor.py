"""State-extraction contract for the Deliberation Room prototype.

This module defines the boundary between raw human language and candidate
structured state.

The first prototype does not yet use an LLM. The purpose of this interface
is to make extraction behavior explicit before any model is introduced.

Core rule:

    WHAT THE HUMAN LITERALLY SAID
        !=
    WHAT THE SYSTEM INFERS FROM IT

Observed content and inferred structure must remain distinguishable.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from state import (
    CognitiveObject,
    DeliberationState,
    EpistemicStatus,
    Provenance,
)


class ExtractionType(str, Enum):
    """Kinds of candidate cognitive objects an extractor may identify."""

    CLAIM = "claim"
    ASSUMPTION = "assumption"
    CONTRADICTION = "contradiction"
    UNRESOLVED_QUESTION = "unresolved_question"
    UNCERTAINTY = "uncertainty"


@dataclass
class ExtractionCandidate:
    """A candidate structured representation derived from human language.

    `source_text` preserves the exact human language that motivated the
    extraction.

    `content` contains the normalized or inferred representation.

    `epistemic_status` must indicate whether the representation was directly
    observed or system-inferred.

    The extractor must never label system inference as HUMAN_ORIGINATED merely
    because the inference concerns human reasoning.
    """

    extraction_type: ExtractionType

    content: str

    source_text: str

    epistemic_status: EpistemicStatus

    provenance: Provenance

    confidence: Optional[float] = None

    rationale: Optional[str] = None


@dataclass
class ExtractionResult:
    """All candidate state updates derived from one human contribution."""

    raw_text: str

    candidates: List[ExtractionCandidate] = field(
        default_factory=list
    )

    requires_human_confirmation: bool = False

    extraction_notes: List[str] = field(
        default_factory=list
    )


class StateExtractor:
    """Abstract extraction interface.

    Future implementations may include:

    - manual extraction
    - rule-based extraction
    - LLM-assisted extraction
    - local-model extraction
    - hybrid extraction

    All implementations should return the same explicit contract.
    """

    def extract(
        self,
        text: str,
        state: DeliberationState,
    ) -> ExtractionResult:
        """Extract candidate state from one human contribution."""

        raise NotImplementedError


class ManualStateExtractor(StateExtractor):
    """Minimal no-inference baseline.

    This implementation treats the full human contribution as an observed
    claim and makes no additional cognitive inference.

    It is intentionally conservative.
    """

    def extract(
        self,
        text: str,
        state: DeliberationState,
    ) -> ExtractionResult:
        """Return the human text as one observed human-originated claim."""

        normalized = text.strip()

        if not normalized:
            return ExtractionResult(
                raw_text=text,
                candidates=[],
                requires_human_confirmation=False,
                extraction_notes=[
                    "No non-empty human contribution was available."
                ],
            )

        candidate = ExtractionCandidate(
            extraction_type=ExtractionType.CLAIM,
            content=normalized,
            source_text=normalized,
            epistemic_status=EpistemicStatus.OBSERVED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
            rationale=(
                "The candidate preserves the human contribution without "
                "introducing additional interpretation."
            ),
        )

        return ExtractionResult(
            raw_text=normalized,
            candidates=[candidate],
            requires_human_confirmation=False,
            extraction_notes=[
                "Manual extractor performed no semantic inference."
            ],
        )


def apply_extraction(
    state: DeliberationState,
    result: ExtractionResult,
) -> None:
    """Apply extraction candidates to active state.

    This helper intentionally applies only a minimal mapping.

    It should not silently promote inferred content into human-confirmed
    content.
    """

    for candidate in result.candidates:
        obj = CognitiveObject(
            content=candidate.content,
            epistemic_status=candidate.epistemic_status,
            provenance=candidate.provenance,
            confidence=candidate.confidence,
        )

        if candidate.extraction_type == ExtractionType.CLAIM:
            state.cognitive.current_claims.append(obj)

        elif candidate.extraction_type == ExtractionType.ASSUMPTION:
            state.cognitive.assumptions.append(obj)

        elif candidate.extraction_type == ExtractionType.CONTRADICTION:
            state.cognitive.contradictions.append(obj)

        elif (
            candidate.extraction_type
            == ExtractionType.UNRESOLVED_QUESTION
        ):
            state.cognitive.unresolved_questions.append(obj)

        elif candidate.extraction_type == ExtractionType.UNCERTAINTY:
            state.cognitive.uncertainty.append(obj)
