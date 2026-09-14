"""Minimal next-move controller for Deliberation Room.

This controller is intentionally simple and inspectable.

It does not attempt to implement the full research architecture.
Its purpose is to make explicit next-move selection executable before
introducing an LLM or learned policy.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from state import DeliberationState, Stability


class Action(str, Enum):
    """Minimal action space for the first prototype."""

    CLARIFY = "clarify"
    DISTINGUISH = "distinguish"
    REQUEST_EVIDENCE = "request_evidence"
    COUNTEREXAMPLE = "counterexample"
    REFLECT = "reflect"
    WITHHOLD = "withhold"
    TRANSITION_TO_COMPOSITION = "transition_to_composition"


@dataclass
class CandidateMove:
    """A candidate next move considered by the controller."""

    action: Action
    target: Optional[str]
    rationale: str

    expected_cognitive_value: str
    expected_information_gain: str
    cognitive_substitution_risk: str

    confidence: str = "moderate"


@dataclass
class PolicyDecision:
    """The controller's selected action plus the candidate set."""

    selected: CandidateMove
    candidates: List[CandidateMove]


class NextMoveController:
    """A minimal rule-based controller.

    This class is intentionally conservative.

    The first research question is not whether a sophisticated model can
    generate impressive questions. It is whether making next-move selection
    explicit changes the interaction in a useful way.
    """

    def generate_candidates(
        self,
        state: DeliberationState,
    ) -> List[CandidateMove]:
        """Generate plausible moves from the current minimal state."""

        cognitive = state.cognitive
        candidates: List[CandidateMove] = []

        # Explicit human request for composition overrides the default
        # deliberative preference.
        if state.composition_requested:
            candidates.append(
                CandidateMove(
                    action=Action.TRANSITION_TO_COMPOSITION,
                    target=None,
                    rationale="The human explicitly requested composition.",
                    expected_cognitive_value="appropriate",
                    expected_information_gain="low",
                    cognitive_substitution_risk="accepted_by_user",
                    confidence="high",
                )
            )
            return candidates

        # Contradictions are strong candidates for inspection.
        if cognitive.contradictions:
            target = cognitive.contradictions[-1].content

            candidates.append(
                CandidateMove(
                    action=Action.DISTINGUISH,
                    target=target,
                    rationale=(
                        "The current state contains a contradiction that may "
                        "depend on a missing distinction."
                    ),
                    expected_cognitive_value="high",
                    expected_information_gain="high",
                    cognitive_substitution_risk="low",
                )
            )

            candidates.append(
                CandidateMove(
                    action=Action.REFLECT,
                    target=target,
                    rationale=(
                        "Reflecting the contradiction may allow the human to "
                        "inspect whether the controller represented it correctly."
                    ),
                    expected_cognitive_value="moderate",
                    expected_information_gain="moderate",
                    cognitive_substitution_risk="low",
                )
            )

        # Explicit assumptions are good targets for testing.
        if cognitive.assumptions:
            target = cognitive.assumptions[-1].content

            candidates.append(
                CandidateMove(
                    action=Action.COUNTEREXAMPLE,
                    target=target,
                    rationale=(
                        "The current representation contains an assumption that "
                        "can potentially be tested without supplying a conclusion."
                    ),
                    expected_cognitive_value="high",
                    expected_information_gain="high",
                    cognitive_substitution_risk="low",
                )
            )

        # Unresolved questions should usually be clarified before additional
        # substantive content is introduced.
        if cognitive.unresolved_questions:
            target = cognitive.unresolved_questions[-1].content

            candidates.append(
                CandidateMove(
                    action=Action.CLARIFY,
                    target=target,
                    rationale=(
                        "An unresolved question is preventing a stable reading "
                        "of the current reasoning state."
                    ),
                    expected_cognitive_value="moderate",
                    expected_information_gain="high",
                    cognitive_substitution_risk="low",
                )
            )

        # If the human has a claim but no visible evidence or assumption to
        # inspect, evidence request is a low-substitution default.
        if (
            cognitive.current_claims
            and not cognitive.assumptions
            and not cognitive.contradictions
        ):
            target = cognitive.current_claims[-1].content

            candidates.append(
                CandidateMove(
                    action=Action.REQUEST_EVIDENCE,
                    target=target,
                    rationale=(
                        "A current claim is represented without an explicit "
                        "evidence connection."
                    ),
                    expected_cognitive_value="moderate",
                    expected_information_gain="moderate",
                    cognitive_substitution_risk="low",
                )
            )

        # Moderate or high stability makes reflection or withholding plausible.
        if cognitive.conceptual_stability in {
            Stability.MODERATE,
            Stability.HIGH,
        }:
            candidates.append(
                CandidateMove(
                    action=Action.REFLECT,
                    target=None,
                    rationale=(
                        "The model appears relatively stable; a concise reflection "
                        "may make the current representation inspectable."
                    ),
                    expected_cognitive_value="moderate",
                    expected_information_gain="low",
                    cognitive_substitution_risk="low",
                )
            )

            candidates.append(
                CandidateMove(
                    action=Action.WITHHOLD,
                    target=None,
                    rationale=(
                        "The current representation may be stable enough that "
                        "another intervention adds little value."
                    ),
                    expected_cognitive_value="appropriate",
                    expected_information_gain="low",
                    cognitive_substitution_risk="none",
                )
            )

        # Always permit withholding as a candidate.
        if not any(
            move.action == Action.WITHHOLD
            for move in candidates
        ):
            candidates.append(
                CandidateMove(
                    action=Action.WITHHOLD,
                    target=None,
                    rationale=(
                        "Withholding remains available when no intervention "
                        "clearly improves the human's next cognitive move."
                    ),
                    expected_cognitive_value="unknown",
                    expected_information_gain="none",
                    cognitive_substitution_risk="none",
                    confidence="low",
                )
            )

        return candidates

    def rank_candidates(
        self,
        candidates: List[CandidateMove],
    ) -> List[CandidateMove]:
        """Rank candidates using a deliberately simple heuristic."""

        cognitive_value = {
            "high": 3,
            "moderate": 2,
            "appropriate": 2,
            "low": 1,
            "unknown": 0,
        }

        information_gain = {
            "high": 3,
            "moderate": 2,
            "low": 1,
            "none": 0,
        }

        substitution_penalty = {
            "none": 0,
            "low": 0,
            "moderate": 2,
            "high": 4,
            "accepted_by_user": 0,
        }

        def score(move: CandidateMove) -> int:
            return (
                cognitive_value.get(
                    move.expected_cognitive_value,
                    0,
                )
                + information_gain.get(
                    move.expected_information_gain,
                    0,
                )
                - substitution_penalty.get(
                    move.cognitive_substitution_risk,
                    0,
                )
            )

        return sorted(
            candidates,
            key=score,
            reverse=True,
        )

    def select_next_move(
        self,
        state: DeliberationState,
    ) -> PolicyDecision:
        """Generate, rank, and select the next move."""

        candidates = self.generate_candidates(state)
        ranked = self.rank_candidates(candidates)

        if not ranked:
            selected = CandidateMove(
                action=Action.WITHHOLD,
                target=None,
                rationale="No justified intervention was available.",
                expected_cognitive_value="unknown",
                expected_information_gain="none",
                cognitive_substitution_risk="none",
                confidence="low",
            )

            return PolicyDecision(
                selected=selected,
                candidates=[selected],
            )

        return PolicyDecision(
            selected=ranked[0],
            candidates=ranked,
        )
