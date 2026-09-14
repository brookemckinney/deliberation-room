"""Minimal linguistic realizer for Deliberation Room.

The controller decides which cognitive action to take.

The realizer decides how that selected action is expressed.

Keeping those functions separate lets later prototypes compare:

    policy quality

against:

    language-generation quality

without allowing a language model to silently become the policy.
"""

from dataclasses import dataclass
from typing import Optional

from controller import Action, CandidateMove
from state import DeliberationState


@dataclass
class RealizedMove:
    """A selected cognitive move plus its surface realization."""

    action: Action
    text: Optional[str]
    target: Optional[str]

    realization_source: str = "template"

    def is_silent(self) -> bool:
        """Return True when the selected policy intentionally emits no text."""

        return self.text is None


class MoveRealizer:
    """Template-based realization for the minimal controller.

    These templates are intentionally generic.

    The first prototype is testing explicit action selection, not whether
    sophisticated generation can produce especially elegant dialogue.
    """

    def realize(
        self,
        move: CandidateMove,
        state: DeliberationState,
    ) -> RealizedMove:
        """Turn a selected policy action into a human-facing utterance."""

        if move.action == Action.WITHHOLD:
            return RealizedMove(
                action=move.action,
                text=None,
                target=move.target,
            )

        if move.action == Action.CLARIFY:
            return RealizedMove(
                action=move.action,
                text=self._clarify(move.target),
                target=move.target,
            )

        if move.action == Action.DISTINGUISH:
            return RealizedMove(
                action=move.action,
                text=self._distinguish(move.target),
                target=move.target,
            )

        if move.action == Action.REQUEST_EVIDENCE:
            return RealizedMove(
                action=move.action,
                text=self._request_evidence(move.target),
                target=move.target,
            )

        if move.action == Action.COUNTEREXAMPLE:
            return RealizedMove(
                action=move.action,
                text=self._counterexample(move.target),
                target=move.target,
            )

        if move.action == Action.REFLECT:
            return RealizedMove(
                action=move.action,
                text=self._reflect(state),
                target=move.target,
            )

        if move.action == Action.TRANSITION_TO_COMPOSITION:
            return RealizedMove(
                action=move.action,
                text=(
                    "Your current judgment looks ready enough to use as the "
                    "basis for composition. What would you like to make from it?"
                ),
                target=move.target,
            )

        raise ValueError(
            f"Unsupported action: {move.action}"
        )

    @staticmethod
    def _clarify(target: Optional[str]) -> str:
        """Realize a clarification request."""

        if target:
            return (
                "I want to make sure I am not filling this in for you. "
                f"What exactly do you mean by: {target!r}?"
            )

        return (
            "What part of the current idea still feels unclear or underspecified?"
        )

    @staticmethod
    def _distinguish(target: Optional[str]) -> str:
        """Realize a distinction move without supplying the distinction."""

        if target:
            return (
                "I may be collapsing two things that are different for you. "
                f"What distinction is missing in this tension: {target!r}?"
            )

        return (
            "Are there two different ideas here that are currently being "
            "treated as the same thing?"
        )

    @staticmethod
    def _request_evidence(target: Optional[str]) -> str:
        """Ask the human to connect a claim to evidence."""

        if target:
            return (
                f"What are you basing this claim on: {target!r}?"
            )

        return "What evidence is doing the most work in your current conclusion?"

    @staticmethod
    def _counterexample(target: Optional[str]) -> str:
        """Request a human-generated counterexample.

        The first template implementation does not fabricate a scenario from
        the target because doing that well requires semantic reasoning.

        A later realizer can generate a concrete counterexample while the
        policy remains responsible for deciding that COUNTEREXAMPLE is the
        correct cognitive function.
        """

        if target:
            return (
                "Try to construct a case where this assumption would fail: "
                f"{target!r}. What would have to be different?"
            )

        return (
            "Can you construct a case that would break your current rule "
            "without changing the whole problem?"
        )

    @staticmethod
    def _reflect(state: DeliberationState) -> str:
        """Reflect only state already represented as human content."""

        claims = [
            item.content
            for item in state.cognitive.current_claims
        ]

        uncertainties = [
            item.content
            for item in state.cognitive.uncertainty
        ]

        parts = []

        if claims:
            parts.append(
                "Your current claim is: "
                + "; ".join(claims)
            )

        if uncertainties:
            parts.append(
                "You are still uncertain about: "
                + "; ".join(uncertainties)
            )

        if not parts:
            return (
                "I do not yet have enough human-confirmed state to reflect "
                "without adding my own interpretation."
            )

        return " ".join(parts)
