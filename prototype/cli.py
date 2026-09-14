"""Multi-turn command-line demo for the Deliberation Room prototype.

Run from the prototype directory:

    python cli.py

This version implements the actual loop:

    state
      ↓
    select move
      ↓
    realize move
      ↓
    human responds
      ↓
    update state
      ↺

The prototype still asks the human to classify state changes manually.
That is deliberate: natural-language state extraction is a separate
research problem and should not be hidden inside the first controller test.
"""

from controller import Action, NextMoveController
from realizer import MoveRealizer
from state import (
    CognitiveObject,
    DeliberationState,
    EpistemicStatus,
    Provenance,
    Stability,
    TraceEvent,
)
from updater import StateUpdater


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
    """Record the initial human-originated claim."""

    claim = prompt_nonempty("\nCurrent claim: ")
    state.record_human_claim(claim)


def add_optional_assumption(state: DeliberationState) -> None:
    """Optionally record an assumption already visible to the human."""

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
    """Optionally record an already-visible contradiction."""

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
    """Collect the deliberately minimal starting state."""

    state = DeliberationState()

    print("\n=== Deliberation Room: Minimal Prototype ===")
    print(
        "\nThis demo asks you to expose a small amount of reasoning state "
        "so the controller's decisions remain inspectable."
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
        trigger = (
            f" triggered_by={event.triggered_by}"
            if event.triggered_by is not None
            else ""
        )

        print(
            f"{index}: "
            f"{event.actor} | "
            f"{event.event_type} | "
            f"{event.provenance.value}"
            f"{trigger}"
        )
        print(f"   {event.content}")


def print_state_summary(state: DeliberationState) -> None:
    """Print the current structured cognitive state."""

    print("\n=== Current State ===")

    print("Claims:")
    if state.cognitive.current_claims:
        for item in state.cognitive.current_claims:
            print(f"  - {item.content}")
    else:
        print("  - none")

    print("Assumptions:")
    if state.cognitive.assumptions:
        for item in state.cognitive.assumptions:
            print(f"  - {item.content}")
    else:
        print("  - none")

    print("Contradictions:")
    if state.cognitive.contradictions:
        for item in state.cognitive.contradictions:
            print(f"  - {item.content}")
    else:
        print("  - none")

    print("Unresolved questions:")
    if state.cognitive.unresolved_questions:
        for item in state.cognitive.unresolved_questions:
            print(f"  - {item.content}")
    else:
        print("  - none")

    print("Uncertainty:")
    if state.cognitive.uncertainty:
        for item in state.cognitive.uncertainty:
            print(f"  - {item.content}")
    else:
        print("  - none")

    print(
        "Conceptual stability: "
        f"{state.cognitive.conceptual_stability.value}"
    )


def choose_response_type() -> str:
    """Ask the human what kind of cognitive event occurred."""

    options = {
        "1": "response_only",
        "2": "new_claim",
        "3": "revision",
        "4": "distinction",
        "5": "new_assumption",
        "6": "new_uncertainty",
        "7": "rejection",
        "8": "no_change",
    }

    print("\nWhat happened cognitively?")
    print("1. response only / not sure yet")
    print("2. I formed a new claim")
    print("3. I revised my current claim")
    print("4. I made a distinction")
    print("5. I identified an assumption")
    print("6. I identified uncertainty")
    print("7. I reject the system's framing or move")
    print("8. No meaningful state change")

    while True:
        choice = input("Choose 1-8: ").strip()

        if choice in options:
            return options[choice]

        print("Please choose a number from 1 to 8.")


def apply_human_update(
    state: DeliberationState,
    updater: StateUpdater,
    system_action: Action,
    system_event_id: int,
) -> None:
    """Collect a human response and apply an explicit state update."""

    response_text = prompt_nonempty("\nYou: ")

    response_type = choose_response_type()

    updater.record_human_response(
        state=state,
        system_action=system_action,
        system_event_id=system_event_id,
        response_text=response_text,
        response_type=response_type,
    )

    if response_type == "new_claim":
        updater.add_human_claim(
            state=state,
            content=prompt_nonempty(
                "State the new claim clearly: "
            ),
            triggered_by=system_event_id,
        )

    elif response_type == "revision":
        updater.revise_current_claim(
            state=state,
            revised_content=prompt_nonempty(
                "State the revised claim clearly: "
            ),
            triggered_by=system_event_id,
        )

    elif response_type == "distinction":
        updater.add_human_distinction(
            state=state,
            content=prompt_nonempty(
                "State the distinction clearly: "
            ),
            triggered_by=system_event_id,
        )

    elif response_type == "new_assumption":
        updater.add_assumption(
            state=state,
            content=prompt_nonempty(
                "State the assumption clearly: "
            ),
            triggered_by=system_event_id,
        )

    elif response_type == "new_uncertainty":
        updater.add_uncertainty(
            state=state,
            content=prompt_nonempty(
                "State the uncertainty clearly: "
            ),
            triggered_by=system_event_id,
        )

    elif response_type == "rejection":
        updater.reject_system_move(
            state=state,
            explanation=prompt_nonempty(
                "What did the system get wrong? "
            ),
            triggered_by=system_event_id,
        )

    if yes_no(
        "\nDid this resolve the most recent assumption?"
    ):
        updater.resolve_assumption(state)

    if yes_no(
        "Did this resolve the most recent contradiction?"
    ):
        updater.resolve_contradiction(state)

    if yes_no(
        "Did this resolve the most recent unresolved question?"
    ):
        updater.resolve_question(state)

    updater.set_stability(
        state,
        choose_stability(),
    )

    state.next_turn()


def run_deliberation() -> None:
    """Run the multi-turn Deliberation Room loop."""

    state = collect_initial_state()

    controller = NextMoveController()
    realizer = MoveRealizer()
    updater = StateUpdater()

    while not state.deliberation_complete:
        print_state_summary(state)

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

        system_event_id = record_system_move(
            state=state,
            action=selected.action.value,
            text=realized.text,
        )

        print("\n=== System ===")

        if realized.is_silent():
            print("[WITHHOLD — no user-facing text emitted]")

            if yes_no(
                "Do you want to continue deliberating anyway?"
            ):
                state.next_turn()
                continue

            state.deliberation_complete = True
            break

        print(realized.text)

        if (
            selected.action
            == Action.TRANSITION_TO_COMPOSITION
        ):
            state.deliberation_complete = True
            break

        if yes_no(
            "\nDo you want the system to compose instead of continuing?"
        ):
            state.composition_requested = True
            state.next_turn()
            continue

        apply_human_update(
            state=state,
            updater=updater,
            system_action=selected.action,
            system_event_id=system_event_id,
        )

        if yes_no(
            "\nAre you done deliberating?"
        ):
            state.deliberation_complete = True

    print("\n=== Deliberation Complete ===")
    print_state_summary(state)
    print_trace(state)


def main() -> None:
    """Entry point."""

    run_deliberation()


if __name__ == "__main__":
    main()
