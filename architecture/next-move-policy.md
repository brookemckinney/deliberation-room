# Next-Move Policy

The Next-Move Policy is the decision mechanism at the center of Deliberation Room.

It consumes the current interaction state and selects an intervention intended to create the most useful next cognitive possibility for the human.

Its central question is:

> **Given what is currently represented about the human, the reasoning state, the language environment, and the interaction, what should the human be able to do next?**

This differs fundamentally from a conventional conversational objective:

> **What should the model say next?**

The distinction is architectural.

Deliberation Room does not begin by assuming that the correct response to human input is more generated content.

It first determines **what kind of intervention, if any, should occur**.

---

## Policy Inputs

At time `t`, the policy receives the current interaction state:

```text
S_t = {
    C_t,
    P_t,
    L_t,
    I_t
}
```

where:

```text
C_t = Cognitive State Model
P_t = Person / Reasoning Model
L_t = Linguistic / Sociolinguistic Model
I_t = Interaction Model
```

It also receives:

```text
G_t = current human goal
K   = governing principles
H_t = relevant interaction history or compressed state
```

Conceptually:

```text
A_t = π(S_t, G_t, K, H_t)
```

where:

```text
π   = next-move policy
A_t = selected action
```

This notation is conceptual rather than an implemented algorithm.

---

## The Policy Selects Actions, Not Answers

The policy's first output is an **action class**.

Candidate actions may include:

```text
ASK
CLARIFY
DISTINGUISH
REFLECT
CHALLENGE
COUNTEREXAMPLE
TEST
REFRAME
COMPARE
REQUEST_EVIDENCE
SURFACE_ASSUMPTION
SURFACE_CONTRADICTION
SURFACE_UNCERTAINTY
INVITE_PERSPECTIVE
SUMMARIZE_PROVISIONALLY
CONFIRM_STABILITY
WITHHOLD
TRANSITION_TO_COMPOSITION
```

This action space is deliberately broader than:

```text
ANSWER
```

and broader than:

```text
ASK_SOCRATIC_QUESTION
```

The system may sometimes ask a question.

It may sometimes offer a candidate distinction.

It may sometimes reflect what the human has already established.

It may sometimes challenge.

It may sometimes say almost nothing.

And when the relevant human cognition is sufficiently stable, it may transition to composition.

---

## Minimum Viable System Move

A central policy heuristic is:

> **Choose the smallest intervention likely to produce meaningful cognitive progress while preserving maximum human response latitude.**

This can be summarized as:

```text
MINIMUM VIABLE SYSTEM MOVE
            +
MAXIMUM HUMAN RESPONSE LATITUDE
```

The system should not perform three cognitive operations when one would be sufficient.

For example, if the current problem is an ambiguous distinction, the system may need only:

> "Are those actually the same thing to you?"

rather than:

1. defining both concepts;
2. proposing the distinction;
3. explaining why the distinction matters;
4. giving an example;
5. and supplying a revised conclusion.

The latter may be more impressive as model output while creating less space for human cognition.

---

## Candidate Policy Objective

A conceptual objective for candidate move `m` might be represented as:

```text
VALUE(m) =

  expected_cognitive_value
+ expected_information_gain
+ human_agency_preserved
+ response_latitude
+ correctability
+ semantic_fit
+ interactional_fit

- cognitive_substitution_risk
- intrusion_cost
- disclosure_pressure
- interactional_risk
- premature_certainty
- unnecessary_system_content
```

This is not currently a validated scoring formula.

It identifies variables the architecture proposes may matter.

One purpose of implementation and evaluation is to determine which of these dimensions can actually be estimated usefully.

---

## Expected Cognitive Value

A move has cognitive value when it creates a meaningful opportunity for the human to perform relevant reasoning.

Possible outcomes include:

- noticing;
- recalling;
- distinguishing;
- connecting;
- explaining;
- hypothesizing;
- generating evidence;
- testing a warrant;
- encountering a counterexample;
- revising;
- comparing;
- representing uncertainty;
- evaluating;
- deciding;
- or recognizing that a conclusion is not yet justified.

The objective is not maximum difficulty.

It is **productive cognitive responsibility**.

---

## Information Gain

Sometimes the system cannot select a useful intervention because its current model is too uncertain.

In that case, the best move may be the one expected to distinguish among competing representations.

Suppose the system currently has:

```text
HYPOTHESIS A
The user objects to the underlying idea.

HYPOTHESIS B
The user accepts the idea but rejects the wording.

HYPOTHESIS C
The idea is correct generally but wrong for this audience.
```

A poor strategy might request broad background.

A higher-information move might be:

> "Is the problem the idea itself, or that this wording changes what you mean?"

One answer may eliminate several hypotheses.

The policy therefore values **uncertainty reduction per unit of intrusion**.

---

## High-Information / Low-Intrusion Selection

The policy should prefer:

```text
high expected information gain
------------------------------
low disclosure / interaction cost
```

when elicitation is necessary.

This does not mean every question should maximize formal information theory.

It means the system should avoid gathering personal information merely because it might be useful later.

Ask what is necessary to select the next move.

Do not build a biography when one distinction will do.

---

## Cognitive Substitution Risk

Every candidate move should be evaluated for the possibility that the system is about to perform cognition the human should still perform.

For example, suppose the human has:

```text
evidence
+
a tentative claim
+
an unresolved contradiction
```

The system could say:

> "The real distinction is X versus Y, which means your argument should actually be Z."

That may resolve the problem efficiently.

It may also remove the central cognitive work.

A lower-substitution move might be:

> "Can both of those claims be true at the same time?"

or:

> "What changes if you separate X from Y?"

The architecture does not prohibit system proposals.

It asks whether supplying one **now** is the best intervention.

---

## Proposal Threshold

Sometimes a system proposal is appropriate.

Possible reasons include:

- repeated elicitation has failed to produce useful movement;
- the human explicitly requests possibilities;
- the human lacks prerequisite vocabulary;
- the distinction is unlikely to be independently discoverable from available information;
- the system can offer several competing representations without privileging one;
- or a proposal itself creates a useful object for human evaluation.

When proposing, the system should preserve provenance:

```text
SYSTEM-PROPOSED
```

and create an opportunity for the human to:

```text
RECOGNIZE
REJECT
REVISE
QUALIFY
APPLY
COUNTEREXAMPLE
```

A system proposal should not silently enter the human cognitive state as established understanding.

---

## Challenge Threshold

Challenge is appropriate when the current representation may benefit from stress testing.

Possible triggers include:

- contradiction;
- unsupported generalization;
- missing warrant;
- ignored counterevidence;
- overconfidence;
- unstable category boundary;
- unexplored alternative explanation;
- or mismatch between stated principle and application.

But challenge should not be selected merely because disagreement is possible.

The policy should consider:

```text
Is the challenge cognitively relevant?
Is the human ready to act on it?
Is this the appropriate stage?
What form of challenge is productive for this person?
What interactional cost does the challenge create?
Can disagreement remain low-cost?
```

---

## Counterexample Selection

Counterexamples are especially useful when the human appears to be relying on a general rule.

For example:

```text
HUMAN
"The problem is that Creon's law is unjust."

SYSTEM
"Would your argument still work if Creon had made a good law?"
```

The system has not supplied the conclusion.

It has altered the test environment.

The human must determine what survives.

A useful counterexample should:

- target a relevant assumption;
- preserve enough of the original situation to isolate the variable;
- avoid smuggling in the desired conclusion;
- and leave interpretation to the human.

---

## Distinction Selection

A `DISTINGUISH` move is useful when two concepts appear to have been collapsed.

The system may either:

### Elicit the distinction

> "Are those the same problem to you?"

or:

### Propose a candidate distinction

> "I'm wondering whether you're separating being noticed from being included."

The choice matters.

If the human appears capable of generating the distinction, elicitation may preserve more cognitive responsibility.

If the human lacks the vocabulary necessary to make progress, a provisional proposal may be more useful.

---

## Reflect

`REFLECT` returns a compressed representation of what the system currently believes the human has established.

Example:

> "So far, you seem certain about X, unsure about Y, and the part that keeps changing is the connection between them."

Reflection can:

- make the model inspectable;
- expose misrepresentation;
- reduce working-memory burden;
- allow correction;
- or establish a stable platform for the next move.

Reflection should not quietly add conclusions the human has not established.

---

## Reframe

`REFRAME` changes the representation of the problem without necessarily changing its substantive content.

Possible reframes include:

```text
chronological → causal
individual → relational
binary → dimensional
outcome → process
position → underlying value
event → recurring pattern
abstract → concrete
concrete → structural
```

Because reframing can materially alter what becomes visible, it should usually be treated as a system proposal requiring human recognition.

---

## Surface Assumption

`SURFACE_ASSUMPTION` makes an implicit dependency visible.

Example:

> "It sounds like this only works if changing your mind counts as weakness. Is that assumption actually part of your argument?"

The system should distinguish:

```text
I observed you say X.
```

from:

```text
Your reasoning appears to require Y.
```

The latter is an inference.

---

## Surface Contradiction

`SURFACE_CONTRADICTION` identifies represented propositions that appear difficult to hold simultaneously.

The move should preserve the possibility that the system has misunderstood.

Prefer:

> "I may be missing a distinction, but these two claims look incompatible to me."

when uncertainty is meaningful.

The objective is not to catch the human being inconsistent.

It is to make the model inspectable.

---

## Surface Uncertainty

Sometimes the most useful intervention is to make uncertainty explicit.

For example:

> "We seem to know why X matters to you, but not yet whether Y actually causes it."

This can prevent premature closure.

Uncertainty is not merely missing information awaiting system completion.

It can be part of a stable human judgment.

---

## Request Evidence

`REQUEST_EVIDENCE` asks the human to connect a proposition to support.

Possible forms include:

> "What are you basing that on?"

> "What in the text makes you think that?"

> "What's the strongest evidence for that interpretation?"

> "What would you expect to observe if that were true?"

The appropriate realization depends on the four-model interaction state.

---

## Invite Perspective

`INVITE_PERSPECTIVE` can help a human inspect a problem from another plausible vantage point.

However, the system should distinguish:

```text
MODELING A PLAUSIBLE PERSPECTIVE
```

from:

```text
CLAIMING TO KNOW WHAT ANOTHER PERSON THINKS
```

For example:

> "What's one plausible way she could interpret that sentence?"

preserves uncertainty.

> "She'll interpret that as rejection."

manufactures certainty about another mind.

Perspective modeling should expand the model, not impersonate unavailable knowledge.

---

## Compare

`COMPARE` places two representations beside one another to make a difference inspectable.

For example:

```text
A: "I want equal effort."

B: "I want evidence that we're both noticing each other."
```

The move may then ask:

> "Do those ask for the same thing?"

Comparison can be especially useful when lexical similarity is obscuring a conceptual distinction.

---

## Ask

`ASK` is the general elicitation action.

But questions are not automatically cognition-preserving.

A question can:

- over-scaffold;
- imply a preferred answer;
- demand unnecessary disclosure;
- narrow the problem prematurely;
- create social pressure;
- or simply waste the human's time.

Questions should therefore be selected using the same policy criteria as any other intervention.

---

## Withhold

`WITHHOLD` is a first-class policy action.

The architecture should be capable of determining:

> **The human already has enough to continue. More system content would reduce agency or add little value.**

Withholding may be appropriate when:

- the human is actively reasoning without needing intervention;
- the next distinction is available to the human;
- the system's inference is too uncertain;
- further questioning would become intrusive;
- the system would merely repeat established information;
- a proposed answer would replace useful human work;
- or the human has indicated a desire to continue independently.

A system that cannot choose not to generate is structurally biased toward intervention.

---

## Human Request for Direct Help

Cognition preservation does not mean refusing direct assistance.

The human may say:

> "Just tell me."

> "Give me examples."

> "Write it."

> "I don't want to deliberate this."

That request is interaction-state evidence.

The architecture should respect human control over the process.

However, the system may still preserve provenance and distinguish:

```text
HUMAN-DEVELOPED
```

from:

```text
SYSTEM-SUPPLIED
```

A cognition-preserving architecture should not become a paternalistic architecture.

---

## Joint Move Selection

The policy should not necessarily select cognitive function independently from linguistic realization.

Instead, a candidate move may be represented as:

```text
M_t = {
    cognitive_function,
    linguistic_realization,
    interactional_affordance
}
```

For example:

```text
cognitive_function:
CHALLENGE

linguistic_realization:
"Wait — does that rule survive the opposite case?"

interactional_affordance:
- low formality
- moderate challenge
- high permission to disagree
- low disclosure pressure
```

The same cognitive function could have multiple candidate realizations.

The policy may need to rank the **joint move**, not merely the abstract cognitive operation.

---

## Why Linguistic Information Enters Before Generation

Suppose the Cognitive State Model indicates:

```text
unexamined contradiction
```

A conventional architecture might select:

```text
CHALLENGE
```

and only afterward decide how to phrase it.

Deliberation Room proposes that this separation may sometimes be inadequate.

The wording can change:

- whether the move is perceived as a challenge;
- whether revision is face-threatening;
- whether disagreement appears permitted;
- whether the human understands the intended distinction;
- whether humor reduces or increases ambiguity;
- and whether the human continues reasoning.

Therefore:

> **Linguistic realization can alter cognitive function.**

Sociolinguistic information is consequently part of move selection, not merely response styling.

---

## Why Interaction Information Enters Before Generation

The same principle applies to interactional context.

A useful cognitive move may become inappropriate because of:

- power;
- role;
- intimacy;
- disclosure pressure;
- evaluation risk;
- audience;
- or relational history.

The policy should therefore ask not only:

> "Would this move advance the reasoning?"

but also:

> "What position would this move place the human in?"

A cognitively elegant question that makes refusal socially costly may be a poor intervention.

---

## Candidate Generation and Ranking

An implementation may separate policy operation into:

```text
1. IDENTIFY CURRENT COGNITIVE NEED

2. GENERATE PLAUSIBLE ACTION CLASSES

3. GENERATE PLAUSIBLE REALIZATIONS

4. ESTIMATE COGNITIVE + INTERACTIONAL EFFECTS

5. REMOVE MOVES THAT VIOLATE GOVERNING PRINCIPLES

6. RANK REMAINING MOVES

7. SELECT MINIMUM SUFFICIENT MOVE

8. OBSERVE HUMAN RESPONSE

9. UPDATE STATE
```

For example:

```text
CURRENT STATE
Unstable causal claim

CANDIDATES
A. explain the causal mechanism
B. ask for the mechanism
C. provide counterexample
D. compare two causal explanations
E. withhold

POLICY ESTIMATE
A = high substitution risk
B = high agency, moderate information gain
C = high testing value
D = potentially premature
E = insufficient intervention

SELECT
B
```

This is the kind of decision Deliberation Room seeks to make explicit.

---

## Policy as a Controller

The architecture can therefore be understood as a controller operating over a partially observed human-interaction state.

Conceptually:

```text
                 ┌─────────────────────┐
                 │ INTERACTION STATE   │
                 │                     │
                 │ C  P  L  I          │
                 └─────────┬───────────┘
                           │
                           ↓
                 ┌─────────────────────┐
                 │ NEXT-MOVE POLICY    │
                 │                     │
                 │ generate candidates │
                 │ estimate effects    │
                 │ apply principles    │
                 │ rank / withhold     │
                 └─────────┬───────────┘
                           │
                           ↓
                 ┌─────────────────────┐
                 │ JOINT MOVE          │
                 │                     │
                 │ cognitive function  │
                 │ linguistic form     │
                 │ affordance          │
                 └─────────┬───────────┘
                           │
                           ↓
                        HUMAN
                           │
                           ↓
                     STATE UPDATE
                           ↺
```

The system's intelligence is therefore expressed partly through **selection and restraint**, not merely generation quality.

---

## Policy Adaptation

Human responses provide evidence about policy quality.

Suppose:

```text
SYSTEM MOVE
Direct contradiction

HUMAN RESPONSE
Defensive repetition
```

That does not automatically mean direct challenge is always bad.

The update may instead be:

```yaml
policy_observation:
  move: direct_challenge
  context:
    domain: personal_deliberation
    stage: early_exploration
  observed_effect:
    productive_revision: false
    response_latitude: reduced
  generalizability: unknown
```

Repeated evidence can update the Person / Reasoning Model and influence future selection.

---

## Rejection Is Policy Feedback

When the human rejects a move, several things may have gone wrong.

Possible failure sources include:

```text
WRONG COGNITIVE TARGET
WRONG INFERENCE
WRONG QUESTION
WRONG LINGUISTIC REALIZATION
WRONG REGISTER
WRONG INTERACTIONAL PERMISSION
WRONG TIMING
TOO MUCH SCAFFOLDING
TOO LITTLE SCAFFOLDING
UNNECESSARY INTERVENTION
```

The architecture should attempt to identify which component failed rather than simply regenerate.

For example:

> "No, I understand the distinction. That's not what I'm stuck on."

is valuable policy feedback.

It indicates that another clarification question may be the wrong next move.

---

## Avoiding the Hidden-Destination Problem

Many nominally Socratic systems effectively operate as:

```text
SYSTEM KNOWS TARGET ANSWER
        ↓
ASK QUESTION
        ↓
HUMAN DOES NOT PRODUCE TARGET
        ↓
ASK MORE LEADING QUESTION
        ↓
HUMAN APPROACHES TARGET
```

Deliberation Room should not assume that the system's preferred answer is the destination.

Instead:

```text
HUMAN MODEL
        ↓
TEST
        ↓
OBSERVE WHAT SURVIVES
        ↓
UPDATE
        ↓
TEST AGAIN IF USEFUL
```

The human may arrive at:

- the system's initial hypothesis;
- a modified version;
- an alternative;
- several competing representations;
- or justified uncertainty.

The policy is responsible for **quality of inspection**, not convergence on a hidden answer.

---

## Exploration Versus Exploitation

The Person / Reasoning Model may suggest that a particular move tends to work well for the human.

Always choosing that move, however, risks creating a self-reinforcing interaction.

The policy may therefore balance:

```text
EXPLOIT
Use a move already supported as productive.

EXPLORE
Try another plausible move when the expected risk is low.
```

Exploration may help discover that:

- another representation works better;
- preferences have changed;
- a strategy is domain-specific;
- or the current model has overgeneralized.

Exploration should remain proportionate to stakes and should not turn the human into an involuntary experiment.

---

## Stopping Deliberation

A good policy needs a stopping rule.

The system should not assume:

```text
more deliberation = better deliberation
```

Possible stopping indicators include:

- the human can articulate the current judgment;
- central distinctions are stable;
- material contradictions have been addressed;
- important warrants are visible;
- relevant counterexamples have been considered;
- remaining uncertainty is explicit;
- further questions produce little information gain;
- the human indicates readiness;
- or the remaining uncertainty belongs primarily to information unavailable within the interaction.

A particularly important heuristic is:

> **The remaining uncertainty belongs primarily to the other person, the world, or future evidence — not to an unresolved defect in the human's current model.**

At that point, continued deliberation may become rumination rather than productive inspection.

---

## Transition to Composition

When sufficient stability exists, the policy may select:

```text
TRANSITION_TO_COMPOSITION
```

This does not mean:

```text
the model now owns the artifact
```

It means the interaction objective changes.

Conceptually:

```text
DELIBERATION POLICY
        ↓
STABILITY / HUMAN READINESS
        ↓
TRANSITION
        ↓
COMPOSITION SUPPORT
```

The next architectural document specifies this boundary in detail.

---

## Trace Events

Every policy decision can contribute to the deliberation trace.

For example:

```yaml
event:
  state_issue:
    type: unsupported_generalization

  candidate_moves:
    - explain
    - request_evidence
    - counterexample
    - withhold

  selected_move:
    cognitive_function: counterexample

  rationale:
    expected_cognitive_value: high
    substitution_risk: low
    interactional_risk: low

  realization:
    source: system
    text: "Would that rule still work if the opposite case were true?"

  human_response:
    type: substantive_revision

  state_update:
    claim_revision: true
```

The exact schema remains an implementation question.

But policy decisions should be inspectable enough to support evaluation.

---

## Policy-Level Evaluation

A cognition-preserving controller should not be evaluated solely on whether users like its responses.

Candidate metrics may include:

```text
HUMAN-ORIGINATED COGNITIVE EVENTS
SUBSTANTIVE HUMAN REVISIONS
HUMAN-GENERATED DISTINCTIONS
HUMAN-GENERATED COUNTEREXAMPLES
WARRANT ARTICULATION
UNCERTAINTY CALIBRATION
TRANSFER TO NEW CASES
INDEPENDENT EXPLANATION
RESPONSE LATITUDE
QUESTION EFFICIENCY
DISCLOSURE REQUIRED
SYSTEM COGNITIVE SUBSTITUTION
TIME TO STABILITY
UNNECESSARY INTERVENTIONS
```

These measures would require empirical validation.

A system that asks more questions is not necessarily more cognition-preserving.

A system that produces less language is not necessarily better.

The relevant question is whether its interventions improve **human cognitive agency and capability**.

---

## Failure Modes

### Over-scaffolding

The system decomposes the problem so thoroughly that the human performs little meaningful reasoning.

### Under-scaffolding

The system withholds support even when the human lacks the representation necessary to continue.

### Question treadmill

The system mistakes asking questions for preserving cognition and continues eliciting after useful information gain has collapsed.

### Hidden steering

Questions are selected to move the human toward a system-preferred conclusion.

### Proposal capture

A system-generated concept enters the human model without meaningful recognition.

### Interaction blindness

The cognitively optimal move is selected without considering power, face, belonging, or response latitude.

### Style-after-reasoning

The policy chooses an abstract cognitive move and assumes linguistic realization cannot alter its function.

### Personalization lock-in

The policy repeatedly uses historically successful strategies and stops testing whether the model remains accurate.

### Engagement optimization

The system continues interaction because continued conversation is treated as success.

### Premature composition

The system begins drafting before the underlying human judgment is sufficiently stable.

### Deliberation trap

The system continues testing a model after remaining uncertainty can no longer be resolved through further reflection.

### False restraint

The system withholds useful information merely to force the human to perform unnecessary work.

Cognition preservation is not maximization of effort.

---

## What This Policy Must Not Do

The Next-Move Policy should not:

- assume generation is always required;
- assume questioning is always better than proposing;
- optimize for conversation length;
- optimize for agreement;
- optimize for user dependence;
- maximize disclosure;
- hide system uncertainty;
- convert system hypotheses into human beliefs;
- steer toward an unstated preferred conclusion;
- treat every contradiction as requiring resolution;
- treat every uncertainty as a defect;
- continue deliberation after its value has collapsed;
- or refuse useful direct assistance merely to preserve an ideology of effort.

---

## Research Questions

Key open questions include:

1. What action space is sufficient for useful deliberative control?
2. How should candidate moves be generated?
3. Which policy variables can be estimated reliably?
4. Can expected cognitive value be operationalized?
5. Can cognitive substitution risk be measured?
6. How should information gain be balanced against disclosure cost?
7. How can response latitude be measured?
8. When should the policy elicit a distinction versus propose one?
9. What evidence is sufficient to justify direct challenge?
10. Can linguistic realization and cognitive function be jointly ranked?
11. How should interactional risk alter otherwise useful cognitive moves?
12. How should the policy learn from rejection without overfitting?
13. How should exploration versus exploitation work in personalized elicitation?
14. What constitutes sufficient conceptual stability?
15. How can the system distinguish productive deliberation from rumination?
16. When should the policy withhold entirely?
17. How should explicit requests for direct generation override the default deliberative policy?
18. Can a constrained next-move controller perform adequately using substantially smaller models than unrestricted generative systems?
19. Does adaptive next-move selection preserve more human cognitive responsibility than generic Socratic prompting?
20. Which policy-level metrics best predict later independent human reasoning?
