"""Minimal state representation for the Deliberation Room prototype.

This module intentionally implements only the state required to test the
first controller. It is not an implementation of the full research schema.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class EpistemicStatus(str, Enum):
    """How the controller currently knows or represents an object."""

    OBSERVED = "observed"
    SYSTEM_INFERRED = "system_inferred"
    SYSTEM_PROPOSED = "system_proposed"
    HUMAN_CONFIRMED = "human_confirmed"
    HUMAN_REJECTED = "human_rejected"
    UNKNOWN = "unknown"


class Provenance(str, Enum):
    """Where a substantive representation originated."""

    HUMAN_ORIGINATED = "human_originated"
    SYSTEM_PROPOSED = "system_proposed"
    SYSTEM_PROPOSED_HUMAN_RECOGNIZED = (
        "system_proposed_human_recognized"
    )
    SYSTEM_PROPOSED_HUMAN_REVISED = (
        "system_proposed_human_revised"
    )
    SYSTEM_PROPOSED_HUMAN_REJECTED = (
        "system_proposed_human_rejected"
    )
    UNKNOWN = "unknown"


class Stability(str, Enum):
    """Current estimate of conceptual stability."""

    UNKNOWN = "unknown"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"


@dataclass
class CognitiveObject:
    """A single represented cognitive object.

    `content` stores the representation itself.

    `epistemic_status` records the evidence status of that representation.

    `provenance` records where the substantive content originated.

    These fields remain separate intentionally. A system inference about
    human reasoning is not automatically a human-originated idea.
    """

    content: str
    epistemic_status: EpistemicStatus
    provenance: Provenance
    confidence: Optional[float] = None


@dataclass
class CognitiveState:
    """Minimal cognitive state used by the first prototype."""

    current_claims: List[CognitiveObject] = field(default_factory=list)
    assumptions: List[CognitiveObject] = field(default_factory=list)
    contradictions: List[CognitiveObject] = field(default_factory=list)
    unresolved_questions: List[CognitiveObject] = field(default_factory=list)
    uncertainty: List[CognitiveObject] = field(default_factory=list)

    conceptual_stability: Stability = Stability.UNKNOWN


@dataclass
class TraceEvent:
    """A meaningful event in the deliberation trace.

    The prototype stores meaningful state transitions rather than treating
    the raw transcript itself as cognitive provenance.
    """

    actor: str
    event_type: str
    content: str

    provenance: Provenance = Provenance.UNKNOWN
    epistemic_status: EpistemicStatus = EpistemicStatus.UNKNOWN

    triggered_by: Optional[int] = None


@dataclass
class DeliberationState:
    """Complete state required by the minimal controller."""

    cognitive: CognitiveState = field(default_factory=CognitiveState)
    trace: List[TraceEvent] = field(default_factory=list)

    turn_number: int = 0
    composition_requested: bool = False
    deliberation_complete: bool = False

    def add_event(self, event: TraceEvent) -> int:
        """Append a trace event and return its event index."""

        self.trace.append(event)
        return len(self.trace) - 1

    def record_human_claim(self, content: str) -> int:
        """Record a claim explicitly introduced by the human."""

        claim = CognitiveObject(
            content=content,
            epistemic_status=EpistemicStatus.OBSERVED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )

        self.cognitive.current_claims.append(claim)

        return self.add_event(
            TraceEvent(
                actor="human",
                event_type="claim",
                content=content,
                provenance=Provenance.HUMAN_ORIGINATED,
                epistemic_status=EpistemicStatus.OBSERVED,
            )
        )

    def next_turn(self) -> None:
        """Advance the interaction counter."""

        self.turn_number += 1
