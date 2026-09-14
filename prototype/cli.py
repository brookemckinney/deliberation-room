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

from confirmation import (
    ConfirmationDecision,
    ConfirmationGate,
)
from extractor import (
    ExtractionCandidate,
    ExtractionResult,
    ExtractionType,
    ManualStateExtractor,
    apply_extraction,
)
from composition import (
    ArtifactType,
    AudienceModel,
    CompositionPlanner,
    LinguisticProfile,
    Register,
    RhetoricalTransposer,
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
    """Ask how settled the human's current thinking feels."""

    options = {
        "1": Stability.UNKNOWN,
        "2": Stability.LOW,
        "3": Stability.MODERATE,
        "4": Stability.HIGH,
    }

    print("\nHow settled does your thinking feel right now?")
    print("1. I don't know yet")
    print("2. Pretty unsettled")
    print("3. I mostly know what I mean")
    print("4. I'm clear on what I mean")

    while True:
        choice = input("Choose 1-4: ").strip()

        if choice in options:
            return options[choice]

        print("Please choose 1, 2, 3, or 4.")


def add_human_claim(state: DeliberationState) -> None:
    """Record the human's initial unfinished thought.

    The current prototype stores this in the claim field internally,
    but the user does not need to formulate or classify it as a claim.
    """

    starting_thought = prompt_nonempty(
        "\nWhat's the thing you're trying to figure out, decide, understand, "
        "write, or say?\n> "
    )

    state.record_human_claim(starting_thought)


def add_optional_assumption(state: DeliberationState) -> None:
    """Optionally record something the human already assumes may be true."""

    if not yes_no(
        "Is there something you're already assuming might be true?"
    ):
        return

    assumption = prompt_nonempty("What are you assuming? ")

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
    """Optionally record a tension or conflict already visible."""

    if not yes_no(
        "Is there any tension, conflict, or part that doesn't quite fit yet?"
    ):
        return

    contradiction = prompt_nonempty(
        "What's the tension or part that doesn't fit? "
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
    """Optionally record a question the human is still circling."""

    if not yes_no(
        "Is there a question you keep circling or can't answer yet?"
    ):
        return

    question = prompt_nonempty("What's the question? ")

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
    """Optionally preserve something the human genuinely does not know."""

    if not yes_no(
        "Is there anything you genuinely don't know yet and don't want "
        "the system to pretend you know?"
    ):
        return

    uncertainty = prompt_nonempty("What don't you know yet? ")

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
        "\nBring an unfinished thought, tension, question, decision, "
        "interpretation, or something you need to say. "
        "You do not need to turn it into a claim first."
    )

    add_human_claim(state)
    add_optional_assumption(state)
    add_optional_contradiction(state)
    add_optional_unresolved_question(state)
    add_optional_uncertainty(state)

    state.cognitive.conceptual_stability = choose_stability()

    state.composition_requested = yes_no(
        "\nDo you already know what you mean and just want help turning "
        "it into the exact thing to write or say?"
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
    response_text: str,
) -> None:
    """Collect a human response and apply an explicit state update."""

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

def review_pending_extractions(
    state: DeliberationState,
    gate: ConfirmationGate,
    pending: list[ExtractionCandidate],
) -> None:
    """Let the human review system-inferred state before policy can use it."""

    for candidate in pending:
        print("\n=== Pending System Inference ===")
        print(f"Type: {candidate.extraction_type.value}")
        print(f"Source text: {candidate.source_text}")
        print(f"System interpretation: {candidate.content}")

        if candidate.rationale:
            print(f"Rationale: {candidate.rationale}")

        if candidate.confidence is not None:
            print(f"Confidence: {candidate.confidence}")

        print("\nChoose:")
        print("1. Confirm")
        print("2. Revise")
        print("3. Reject")

        while True:
            choice = input("Choose 1-3: ").strip()

            if choice == "1":
                gate.confirm(
                    state=state,
                    candidate=candidate,
                )
                break

            if choice == "2":
                revised = prompt_nonempty(
                    "State the corrected interpretation: "
                )

                gate.revise(
                    state=state,
                    candidate=candidate,
                    revised_content=revised,
                )
                break

            if choice == "3":
                explanation = input(
                    "Optional explanation of what is wrong: "
                ).strip()

                gate.reject(
                    state=state,
                    candidate=candidate,
                    explanation=explanation or None,
                )
                break

            print("Please choose 1, 2, or 3.")

def extract_and_review_human_input(
    state: DeliberationState,
    text: str,
    extractor: ManualStateExtractor,
    gate: ConfirmationGate,
) -> ExtractionResult:
    """Extract candidate state and gate any inferred representations."""

    result = extractor.extract(
        text=text,
        state=state,
    )

    updated = apply_extraction(
        state=state,
        result=result,
    )

    if updated.pending_confirmation:
        review_pending_extractions(
            state=state,
            gate=gate,
            pending=updated.pending_confirmation,
        )

    return updated

def run_deliberation() -> None:
    """Run the multi-turn Deliberation Room loop."""
    state = collect_initial_state()

    controller = NextMoveController()
    realizer = MoveRealizer()
    updater = StateUpdater()
    extractor = ManualStateExtractor()
    confirmation_gate = ConfirmationGate()

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
            print("\n=== Composition Handoff ===")

            print("\nWhat are you making?")
            print("1. Message / text")
            print("2. Email")
            print("3. Essay")
            print("4. Discussion post")
            print("5. Memo")
            print("6. Feedback")
            print("7. Speech")
            print("8. Explanation")
            print("9. Other")

            artifact_options = {
                "1": ArtifactType.MESSAGE,
                "2": ArtifactType.EMAIL,
                "3": ArtifactType.ESSAY,
                "4": ArtifactType.DISCUSSION_POST,
                "5": ArtifactType.MEMO,
                "6": ArtifactType.FEEDBACK,
                "7": ArtifactType.SPEECH,
                "8": ArtifactType.EXPLANATION,
                "9": ArtifactType.OTHER,
            }

            while True:
                artifact_choice = input("Choose 1-9: ").strip()

                if artifact_choice in artifact_options:
                    artifact_type = artifact_options[artifact_choice]
                    break

                print("Please choose a number from 1 to 9.")

            purpose = prompt_nonempty(
                "\nWhat does this need to accomplish?\n> "
            )

            audience_description = prompt_nonempty(
                "\nWho is this for?\n> "
            )

            relationship = input(
                "\nWhat's your relationship to them? "
                "(optional — press Enter to skip)\n> "
            ).strip()

            role = input(
                "\nWhat role do they occupy here? "
                "(optional — press Enter to skip)\n> "
            ).strip()

            audience = AudienceModel(
                description=audience_description,
                role=role or None,
                relationship=relationship or None,
            )

            linguistic_profile = LinguisticProfile(
                register=Register.CONVERSATIONAL,
            )

            planner = CompositionPlanner()
            transposer = RhetoricalTransposer()

            contract = planner.build_contract(
                state=state,
                artifact_type=artifact_type,
                purpose=purpose,
                audience=audience,
                linguistic_profile=linguistic_profile,
            )

            result = transposer.compose(contract)

            print("\n=== Draft ===\n")
            print(result.text)

            if result.drift_flags:
                print("\n=== Drift Flags ===")

                for flag in result.drift_flags:
                    print(f"- {flag}")

            state.deliberation_complete = True
            break

        print("Please choose a number from 1 to 9.")

    purpose = prompt_nonempty(
        "\nWhat does this need to accomplish?\n> "
    )

    audience_description = prompt_nonempty(
        "\nWho is this for?\n> "
    )

    relationship = input(
        "\nWhat's your relationship to them? "
        "(optional — press Enter to skip)\n> "
    ).strip()

    role = input(
        "\nWhat role do they occupy here? "
        "(optional — press Enter to skip)\n> "
    ).strip()

    audience = AudienceModel(
        description=audience_description,
        role=role or None,
        relationship=relationship or None,
    )

    linguistic_profile = LinguisticProfile(
        register=Register.CONVERSATIONAL,
    )

    planner = CompositionPlanner()
    transposer = RhetoricalTransposer()

    contract = planner.build_contract(
        state=state,
        artifact_type=artifact_type,
        purpose=purpose,
        audience=audience,
        linguistic_profile=linguistic_profile,
    )

    result = transposer.compose(contract)

    print("\n=== Draft ===\n")
    print(result.text)

    if result.drift_flags:
        print("\n=== Drift Flags ===")
        for flag in result.drift_flags:
            print(f"- {flag}")

    state.deliberation_complete = True
    break

        if yes_no(
            "\nDo you want the system to compose instead of continuing?"
        ):
            state.composition_requested = True
            state.next_turn()
            continue

        human_text = prompt_nonempty("\nYou: ")

        extract_and_review_human_input(
            state=state,
            text=human_text,
            extractor=extractor,
            gate=confirmation_gate,
        )

        apply_human_update(
            state=state,
            updater=updater,
            system_action=selected.action,
            system_event_id=system_event_id,
            response_text=human_text,
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
