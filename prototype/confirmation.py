"""Human-confirmation gate for inferred Deliberation Room state.

The extractor may generate candidate interpretations of human reasoning.

Those candidates should not automatically become active human-confirmed
state merely because the system inferred them.

This module provides a small confirmation layer:

    system inference
        ↓
    pending candidate
        ↓
    human confirms / revises / rejects
        ↓
    active state or discarded candidate

The first prototype keeps this process explicit and inspectable.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from extractor import (
    ExtractionCandidate,
    ExtractionType,
)
from state import (
    CognitiveObject,
    DeliberationState,
    EpistemicStatus,
    Provenance,
    TraceEvent,
)


class ConfirmationDecision(str, Enum):
    """Possible human responses to an inferred candidate."""

    CONFIRM = "confirm"
    REVISE = "revise"
    REJECT = "reject"


@dataclass
class ConfirmationResult:
    """Outcome of human review of one inferred candidate."""

    decision: ConfirmationDecision

    original_candidate: ExtractionCandidate

    final_content: Optional[str] = None

    trace_event_id: Optional[int] = None


class ConfirmationGate:
    """Apply human review before inferred state becomes confirmed state."""

    def confirm(
        self,
        state: DeliberationState,
        candidate: ExtractionCandidate,
    ) -> ConfirmationResult:
        """Confirm the candidate as part of the human's represented state."""

        confirmed = CognitiveObject(
            content=candidate.content,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=(
                Provenance.SYSTEM_PROPOSED_HUMAN_RECOGNIZED
            ),
            confidence=candidate.confidence,
        )

        self._route_object(
            state=state,
            extraction_type=candidate.extraction_type,
            obj=confirmed,
        )

        event_id = state.add_event(
            TraceEvent(
                actor="human",
                event_type="recognition",
                content=candidate.content,
                provenance=(
                    Provenance.SYSTEM_PROPOSED_HUMAN_RECOGNIZED
                ),
                epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            )
        )

        return ConfirmationResult(
            decision=ConfirmationDecision.CONFIRM,
            original_candidate=candidate,
            final_content=candidate.content,
            trace_event_id=event_id,
        )

    def revise(
        self,
        state: DeliberationState,
        candidate: ExtractionCandidate,
        revised_content: str,
    ) -> ConfirmationResult:
        """Accept the candidate only after substantive human revision."""

        revised = CognitiveObject(
            content=revised_content,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=(
                Provenance.SYSTEM_PROPOSED_HUMAN_REVISED
            ),
            confidence=1.0,
        )

        self._route_object(
            state=state,
            extraction_type=candidate.extraction_type,
            obj=revised,
        )

        event_id = state.add_event(
            TraceEvent(
                actor="human",
                event_type="revision",
                content=revised_content,
                provenance=(
                    Provenance.SYSTEM_PROPOSED_HUMAN_REVISED
                ),
                epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            )
        )

        return ConfirmationResult(
            decision=ConfirmationDecision.REVISE,
            original_candidate=candidate,
            final_content=revised_content,
            trace_event_id=event_id,
        )

    def reject(
        self,
        state: DeliberationState,
        candidate: ExtractionCandidate,
        explanation: Optional[str] = None,
    ) -> ConfirmationResult:
        """Reject the candidate without adding it to active cognitive state."""

        content = explanation or candidate.content

        event_id = state.add_event(
            TraceEvent(
                actor="human",
                event_type="rejection",
                content=content,
                provenance=(
                    Provenance.SYSTEM_PROPOSED_HUMAN_REJECTED
                ),
                epistemic_status=EpistemicStatus.HUMAN_REJECTED,
            )
        )

        return ConfirmationResult(
            decision=ConfirmationDecision.REJECT,
            original_candidate=candidate,
            final_content=None,
            trace_event_id=event_id,
        )

    @staticmethod
    def requires_confirmation(
        candidate: ExtractionCandidate,
    ) -> bool:
        """Return True when a candidate should not silently enter active state."""

        return (
            candidate.epistemic_status
            in {
                EpistemicStatus.SYSTEM_INFERRED,
                EpistemicStatus.SYSTEM_PROPOSED,
            }
            or candidate.provenance
            == Provenance.SYSTEM_PROPOSED
        )

    @staticmethod
    def _route_object(
        state: DeliberationState,
        extraction_type: ExtractionType,
        obj: CognitiveObject,
    ) -> None:
        """Route a confirmed object into the appropriate active state list."""

        if extraction_type == ExtractionType.CLAIM:
            state.cognitive.current_claims.append(obj)

        elif extraction_type == ExtractionType.ASSUMPTION:
            state.cognitive.assumptions.append(obj)

        elif extraction_type == ExtractionType.CONTRADICTION:
            state.cognitive.contradictions.append(obj)

        elif (
            extraction_type
            == ExtractionType.UNRESOLVED_QUESTION
        ):
            state.cognitive.unresolved_questions.append(obj)

        elif extraction_type == ExtractionType.UNCERTAINTY:
            state.cognitive.uncertainty.append(obj)

        else:
            raise ValueError(
                f"Unsupported extraction type: {extraction_type}"
            )
