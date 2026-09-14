"""Command-line demo for the minimal Deliberation Room prototype.

Run from the prototype directory:

    python cli.py

This demo is intentionally narrow.

It does not infer a rich cognitive state from natural language.
Instead, it lets a human explicitly enter a small amount of structured
state so the next-move controller can be inspected before an LLM is added.
"""

from controller import NextMoveController
from realizer import MoveRealizer
from state import (
    CognitiveObject,
    DeliberationState,
    EpistemicStatus,
    Provenance,
    Stability,
    TraceEvent,
)


def prompt_nonempty(label: str) -> str:
    """Prompt until the user enters non-empty text."""

    while True:
        value = input(label).strip()

        if value:
            return value

        print("Please enter something.")


def yes_no(label: str) -> bool:
    """Return True for yes and False for no."""

    while True:
        value = input(f"{label} [y/n]: ").strip().lower()

        if value in {"y", "yes"}:
            return True

        if value in {"n", "no"}:
            return False

        print("Please enter y or n.")


def choose_stability() -> Stability:
    """Ask the user for a provisional conceptual-stability state."""

    options = {
        "1": Stability.UNKNOWN,
        "2": Stability.LOW,
        "3": Stability.MODERATE,
        "4": Stability.HIGH,
    }

    print("\nConceptual stability")
    print("1. unknown")
    print("2. low")
    print("3. moderate")
    print("4. high")

    while True:
        choice = input("Choose 1-4: ").strip()

        if choice in options:
            return options[choice]

        print("Please choose 1, 2, 3, or 4.")


def add_human_claim(state: DeliberationState) -> None:
    """Record a human-originated claim."""

    claim = prompt_nonempty("\nCurrent claim: ")

    state.record_human_claim(claim)


def add_optional_assumption(state: DeliberationState) -> None:
    """Optionally record an assumption currently under inspection."""

    if not yes_no(
        "Is there an assumption you want the controller to inspect?"
    ):
        return

    assumption = prompt_nonempty("Assumption: ")

    state.cognitive.assumptions.append(
        CognitiveObject(
            content=assumption,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )
    )

    state.add_event(
        TraceEvent(
            actor="human",
            event_type="assumption",
            content=assumption,
            provenance=Provenance.HUMAN_ORIGINATED,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
        )
    )


def add_optional_contradiction(state: DeliberationState) -> None:
    """Optionally record a contradiction or tension."""

    if not yes_no(
        "Is there a contradiction or tension already visible?"
    ):
        return

    contradiction = prompt_nonempty(
        "Describe the contradiction/tension: "
    )

    state.cognitive.contradictions.append(
        CognitiveObject(
            content=contradiction,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )
    )

    state.add_event(
        TraceEvent(
            actor="human",
            event_type="contradiction",
            content=contradiction,
            provenance=Provenance.HUMAN_ORIGINATED,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
        )
    )


def add_optional_unresolved_question(
    state: DeliberationState,
) -> None:
    """Optionally record an unresolved question."""

    if not yes_no("Is there a specific unresolved question?"):
        return

    question = prompt_nonempty("Unresolved question: ")

    state.cognitive.unresolved_questions.append(
        CognitiveObject(
            content=question,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )
    )

    state.add_event(
        TraceEvent(
            actor="human",
            event_type="unresolved_question",
            content=question,
            provenance=Provenance.HUMAN_ORIGINATED,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
        )
    )


def add_optional_uncertainty(state: DeliberationState) -> None:
    """Optionally record uncertainty that should remain explicit."""

    if not yes_no("Is there uncertainty you want to preserve?"):
        return

    uncertainty = prompt_nonempty("Uncertainty: ")

    state.cognitive.uncertainty.append(
        CognitiveObject(
            content=uncertainty,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
            provenance=Provenance.HUMAN_ORIGINATED,
            confidence=1.0,
        )
    )

    state.add_event(
        TraceEvent(
            actor="human",
            event_type="uncertainty",
            content=uncertainty,
            provenance=Provenance.HUMAN_ORIGINATED,
            epistemic_status=EpistemicStatus.HUMAN_CONFIRMED,
        )
    )


def collect_initial_state() -> DeliberationState:
    """Collect the deliberately minimal state used by the prototype."""

    state = DeliberationState()

    print("\n=== Deliberation Room: Minimal Prototype ===")
    print(
        "\nThis demo asks you to expose a tiny amount of reasoning state "
        "so the controller's next-move decision can be inspected."
    )

    add_human_claim(state)
    add_optional_assumption(state)
    add_optional_contradiction(state)
    add_optional_unresolved_question(state)
    add_optional_uncertainty(state)

    state.cognitive.conceptual_stability = choose_stability()

    state.composition_requested = yes_no(
        "\nDo you want to move directly to composition?"
    )

    return state


def print_candidate_moves(decision) -> None:
    """Show all candidate moves considered by the controller."""

    print("\n=== Candidate Moves ===")

    for index, move in enumerate(
        decision.candidates,
        start=1,
    ):
        print(f"\n{index}. {move.action.value.upper()}")
        print(f"   target: {move.target}")
        print(f"   rationale: {move.rationale}")
        print(
            "   expected cognitive value: "
            f"{move.expected_cognitive_value}"
        )
        print(
            "   expected information gain: "
            f"{move.expected_information_gain}"
        )
        print(
            "   cognitive substitution risk: "
            f"{move.cognitive_substitution_risk}"
        )
        print(f"   confidence: {move.confidence}")


def record_system_move(
    state: DeliberationState,
    action: str,
    text: str | None,
) -> int:
    """Record the selected system move in the trace."""

    content = text if text is not None else "[WITHHOLD]"

    return state.add_event(
        TraceEvent(
            actor="system",
            event_type=action,
            content=content,
            provenance=Provenance.SYSTEM_PROPOSED,
            epistemic_status=EpistemicStatus.SYSTEM_PROPOSED,
        )
    )


def print_trace(state: DeliberationState) -> None:
    """Print the minimal deliberation trace."""

    print("\n=== Trace ===")

    for index, event in enumerate(state.trace):
        print(
            f"{index}: "
            f"{event.actor} | "
            f"{event.event_type} | "
            f"{event.provenance.value}"
        )
        print(f"   {event.content}")


def main() -> None:
    """Run a single inspectable controller turn."""

    state = collect_initial_state()

    controller = NextMoveController()
    realizer = MoveRealizer()

    decision = controller.select_next_move(state)

    print_candidate_moves(decision)

    selected = decision.selected

    print("\n=== Selected Move ===")
    print(selected.action.value.upper())
    print(selected.rationale)

    realized = realizer.realize(
        selected,
        state,
    )

    record_system_move(
        state=state,
        action=selected.action.value,
        text=realized.text,
    )

    print("\n=== Realization ===")

    if realized.is_silent():
        print("[WITHHOLD — no user-facing text emitted]")
    else:
        print(realized.text)

    print_trace(state)

    print(
        "\nThis prototype currently stops after one controller decision. "
        "The next implementation step will update state from the human's "
        "response and run the policy again."
    )


if __name__ == "__main__":
    main()
