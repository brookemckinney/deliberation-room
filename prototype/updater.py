"""Minimal state updater for the Deliberation Room prototype.

The updater converts a human response after a system move into an explicit
state change.

This first version is intentionally conservative.

It does not attempt to infer rich cognition from arbitrary natural language.
Instead, it asks the human to classify what changed so the architecture's
state-update loop can be tested before introducing an LLM-based extractor.
"""

from controller import Action
from state import (
    CognitiveObject,
    DeliberationState,
    EpistemicStatus,
    Provenance,
    Stability,
    TraceEvent,
)


class StateUpdater:
    """Update deliberation state after a human response."""

    def record_human_response(
        self,
        state: DeliberationState,
        system_action: Action,
        system_event_id: int,
        response_text: str,
        response_type: str,
    ) -> int:
        """Record the raw human response as a trace event."""

        return state.add_event(
            TraceEvent(
                actor="human",
                event_type=response_type,
                content=response_text,
                provenance=Provenance.HUMAN_ORIGINATED,
                epistemic_status=EpistemicStatus.OBSERVED,
                triggered_by=system_event_id,
            )
        )

    def add_human_claim(
        self,
        state: DeliberationState,
        content: str,
        triggered_by: int,
    ) -> int:
        """Add a new human-originated claim."""

        obj = CognitiveObject(
            content=content,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )

        state.cognitive.current_claims.append(obj)

        return state.add_event(
            TraceEvent(
                actor="human",
                event_type="claim",
                content=content,
                provenance=Provenance.HUMAN_ORIGINATED,
                epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
                triggered_by=triggered_by,
            )
        )

    def add_human_distinction(
        self,
        state: DeliberationState,
        content: str,
        triggered_by: int,
    ) -> int:
        """Record a human-generated distinction.

        The minimal prototype does not yet store distinctions in a dedicated
        state field, so the distinction is preserved in the trace.
        """

        return state.add_event(
            TraceEvent(
                actor="human",
                event_type="distinction",
                content=content,
                provenance=Provenance.HUMAN_ORIGINATED,
                epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
                triggered_by=triggered_by,
            )
        )

    def add_assumption(
        self,
        state: DeliberationState,
        content: str,
        triggered_by: int,
    ) -> int:
        """Add an assumption exposed by the human."""

        obj = CognitiveObject(
            content=content,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )

        state.cognitive.assumptions.append(obj)

        return state.add_event(
            TraceEvent(
                actor="human",
                event_type="assumption",
                content=content,
                provenance=Provenance.HUMAN_ORIGINATED,
                epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
                triggered_by=triggered_by,
            )
        )

    def add_uncertainty(
        self,
        state: DeliberationState,
        content: str,
        triggered_by: int,
    ) -> int:
        """Add uncertainty explicitly preserved by the human."""

        obj = CognitiveObject(
            content=content,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )

        state.cognitive.uncertainty.append(obj)

        return state.add_event(
            TraceEvent(
                actor="human",
                event_type="uncertainty",
                content=content,
                provenance=Provenance.HUMAN_ORIGINATED,
                epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
                triggered_by=triggered_by,
            )
        )

    def reject_system_move(
        self,
        state: DeliberationState,
        explanation: str,
        triggered_by: int,
    ) -> int:
        """Record human rejection of the system's framing or move."""

        return state.add_event(
            TraceEvent(
                actor="human",
                event_type="rejection",
                content=explanation,
                provenance=Provenance.SYSTEM_PROPOSED_HUMAN_REJECTED,
                epistemic_status=EpistemicStatus.HUMAN_REJECTED,
                triggered_by=triggered_by,
            )
        )

    def revise_current_claim(
        self,
        state: DeliberationState,
        revised_content: str,
        triggered_by: int,
    ) -> int:
        """Replace the most recent active claim with a human revision."""

        if state.cognitive.current_claims:
            state.cognitive.current_claims.pop()

        revised = CognitiveObject(
            content=revised_content,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )

        state.cognitive.current_claims.append(revised)

        return state.add_event(
            TraceEvent(
                actor="human",
                event_type="revision",
                content=revised_content,
                provenance=Provenance.HUMAN_ORIGINATED,
                epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
                triggered_by=triggered_by,
            )
        )

    def resolve_assumption(
        self,
        state: DeliberationState,
    ) -> None:
        """Remove the most recently represented assumption."""

        if state.cognitive.assumptions:
            state.cognitive.assumptions.pop()

    def resolve_contradiction(
        self,
        state: DeliberationState,
    ) -> None:
        """Remove the most recently represented contradiction."""

        if state.cognitive.contradictions:
            state.cognitive.contradictions.pop()

    def resolve_question(
        self,
        state: DeliberationState,
    ) -> None:
        """Remove the most recently represented unresolved question."""

        if state.cognitive.unresolved_questions:
            state.cognitive.unresolved_questions.pop()

    def set_stability(
        self,
        state: DeliberationState,
        stability: Stability,
    ) -> None:
        """Update provisional conceptual stability."""

        state.cognitive.conceptual_stability = stability
