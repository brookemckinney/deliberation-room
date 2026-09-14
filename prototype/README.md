# Prototype

This directory defines the first executable prototype of Deliberation Room.

The prototype is intentionally narrow.

Its purpose is not to implement the full research architecture.

Its purpose is to test one central claim:

> **Can a stateful controller select a useful cognition-preserving next move instead of defaulting directly to unrestricted answer generation?**

---

## Prototype Goal

Build the smallest system capable of:

```text
HUMAN INPUT
      ↓
EXTRACT MINIMAL REASONING STATE
      ↓
GENERATE CANDIDATE NEXT MOVES
      ↓
RANK CANDIDATES
      ↓
SELECT ONE MOVE OR WITHHOLD
      ↓
HUMAN RESPONDS
      ↓
UPDATE STATE
      ↺
```

The prototype should preserve the distinction between:

```text
WHAT THE HUMAN SAID

WHAT THE SYSTEM INFERRED

WHAT THE SYSTEM PROPOSED

WHAT THE HUMAN LATER RECOGNIZED OR REJECTED
```

---

## What This Prototype Is Testing

The first prototype should answer a narrow question:

> **Does explicit next-move selection produce meaningfully different human reasoning behavior from a simpler generative or generic-questioning baseline?**

It does not need to demonstrate:

- full sociolinguistic modeling;
- persistent personalization;
- local inference;
- full cognitive provenance;
- domain-general performance;
- production privacy architecture;
- or validated metacognitive feedback.

Those belong to later phases.

---

# Minimal State

The first implementation should use only a small subset of the full state architecture.

Candidate minimal state:

```yaml
cognitive_state:

  current_claims: []

  assumptions: []

  contradictions: []

  unresolved_questions: []

  uncertainty: []

  conceptual_stability:
    status: unknown
```

The prototype may add additional fields only when they are required for a tested behavior.

The burden of proof is on complexity.

---

# Minimal Epistemic Status

Every represented object should preserve whether it is:

```text
OBSERVED

SYSTEM-INFERRED

SYSTEM-PROPOSED

HUMAN-CONFIRMED

HUMAN-REJECTED

UNKNOWN
```

This prevents the controller from quietly treating its own interpretation as the human's belief.

---

# Minimal Action Space

The first controller should choose from a deliberately small action set:

```text
CLARIFY

DISTINGUISH

REQUEST_EVIDENCE

COUNTEREXAMPLE

REFLECT

WITHHOLD

TRANSITION_TO_COMPOSITION
```

Do not add additional actions until a real interaction exposes a need.

---

# Action Definitions

## CLARIFY

Use when the meaning of a human representation is materially ambiguous.

Example:

> "When you say 'dramatic,' do you mean emotionally exaggerated or inaccurate to what you actually mean?"

The objective is uncertainty reduction.

---

## DISTINGUISH

Use when two concepts may be collapsed.

Example:

> "Are being noticed and being included actually the same thing to you?"

The controller should prefer eliciting the distinction when the human appears capable of producing it.

---

## REQUEST_EVIDENCE

Use when a claim lacks visible support relevant to the task.

Example:

> "What are you basing that on?"

The controller should not automatically supply the evidence.

---

## COUNTEREXAMPLE

Use when a claim appears to rely on a general rule or assumption that can be tested by changing one relevant condition.

Example:

> "Would your claim still hold if the law itself were just?"

A counterexample should test the representation without embedding the preferred conclusion.

---

## REFLECT

Use when a compressed representation would make the current model easier for the human to inspect.

Example:

> "So far, you seem certain about X, unsure about Y, and the connection between them is what keeps changing."

Reflection should not add substantive claims.

---

## WITHHOLD

Use when another system intervention is unlikely to create enough value to justify itself.

Possible triggers:

- the human can continue independently;
- another question would be redundant;
- the controller's inference is too uncertain;
- intervention would likely substitute for useful human reasoning;
- or the current state is already sufficiently stable.

`WITHHOLD` is a successful policy action.

---

## TRANSITION_TO_COMPOSITION

Use when:

- the human explicitly requests composition;

or

- the relevant judgment appears sufficiently stable and the current task requires an artifact.

The transition must remain explicit.

---

# Candidate Move Representation

Each candidate move should minimally contain:

```yaml
candidate_move:

  action: null

  target: null

  rationale: null

  expected_information_gain: null

  cognitive_substitution_risk: null

  confidence: null
```

This is not intended as a final machine-learning feature set.

It is enough to make policy decisions inspectable.

---

# Candidate Ranking

The initial prototype can use a simple qualitative policy.

For each candidate, estimate:

```text
EXPECTED COGNITIVE VALUE

EXPECTED INFORMATION GAIN

COGNITIVE SUBSTITUTION RISK

CURRENT MODEL CONFIDENCE
```

A rough preference rule:

```text
prefer a move when:

cognitive value is high
AND
substitution risk is acceptably low
AND
the move targets a real unresolved state
```

The first prototype does not require a learned reward model.

---

# Example Selection

Current state:

```text
human claim:
"The problem is that Creon's law is bad."

unresolved:
whether the claim depends only on the law's moral quality

confidence:
moderate
```

Candidates:

```text
A. Explain why Creon's authority is the deeper issue.

B. Ask for more textual evidence.

C. Test the claim with a morally good law.

D. Summarize the claim.

E. Withhold.
```

Possible controller decision:

```yaml
selected_move:

  action: COUNTEREXAMPLE

  target: "claim depends on moral quality of law"

  rationale:
    - "directly tests unresolved assumption"
    - "preserves learner judgment"
    - "low need for system-generated interpretation"

  expected_information_gain: high

  cognitive_substitution_risk: low

  confidence: moderate
```

Realization:

> "Would your argument still work if Creon had made a good law but reasoned about his authority in exactly the same way?"

---

# Human Response Update

Suppose the human replies:

> "Then I think I'd still have a problem with him because he acts like being king means nobody can tell him he's wrong."

The system should update:

```text
NEW HUMAN-ORIGINATED DISTINCTION

authority
≠
infallibility
```

The system must preserve:

```text
trigger:
SYSTEM COUNTEREXAMPLE

conceptual source:
HUMAN
```

The fact that the system caused the opportunity does not make the human-generated distinction system-originated.

---

# Prototype Provenance

The first prototype does not need full cognitive provenance.

It should preserve only enough event history to distinguish:

```text
HUMAN-ORIGINATED

SYSTEM-PROPOSED

SYSTEM-PROPOSED → HUMAN-RECOGNIZED

SYSTEM-PROPOSED → HUMAN-REVISED

SYSTEM-PROPOSED → HUMAN-REJECTED
```

This is sufficient to begin testing whether provenance can be tracked at all.

---

# Prototype Trace

A minimal trace might look like:

```yaml
events:

  - actor: human
    type: claim
    content: "Creon's problem is the bad law."
    provenance: human_originated

  - actor: system
    type: counterexample
    target: claim_1

  - actor: human
    type: distinction
    content:
      left: authority
      right: infallibility
    provenance: human_originated
    triggered_by: event_2
```

Do not preserve more event detail unless the evaluation requires it.

---

# Stopping Rule

The controller should stop intervening when:

```text
central claim is explicit

major unresolved distinction has been addressed

relevant contradiction is no longer active

remaining uncertainty is visible

another intervention has low expected value
```

The controller should also stop when the human explicitly says they are done.

---

# Human Override

At any time, the human may say:

```text
"Just tell me."

"Write it."

"Give me the answer."

"Stop asking questions."
```

The prototype should honor the request.

A cognition-preserving architecture must preserve human control over whether deliberation continues.

The resulting content should simply retain accurate provenance.

---

# First Baselines

The first prototype should eventually be compared against:

## Baseline A — Unrestricted generation

Instruction:

> Respond as a generally helpful AI assistant.

## Baseline B — Generic Socratic interaction

Instruction:

> Do not give the answer. Ask the user questions that help them reason through the problem.

## Condition C — Deliberation Room prototype

Uses explicit:

```text
state
+
candidate move generation
+
next-move selection
+
state update
```

This comparison matters because the architecture must outperform more than a bad baseline.

---

# First Task Type

The initial implementation should use a bounded reasoning task where:

- the human can begin with an incomplete claim;
- a relevant assumption can be tested;
- revisions can be observed;
- there is no requirement for one predetermined answer;
- and later independent explanation can be evaluated.

A strong first domain is:

```text
short literary or argument interpretation
```

because the interaction can naturally include:

```text
claim
evidence
assumption
counterexample
revision
distinction
```

without requiring a large external knowledge base.

---

# First Evaluation

After the assisted interaction, remove the system.

Ask the human to complete:

```text
1. State the final claim in your own words.

2. Explain what changed from your initial claim.

3. Identify the most important distinction you made.

4. Respond to one new counterexample.

5. Identify anything you are still uncertain about.
```

This begins testing:

```text
INDEPENDENT EXPLANATION

REASONING RECONSTRUCTION

DISTINCTION RETENTION

COUNTEREXAMPLE RESPONSE

UNCERTAINTY REPRESENTATION
```

---

# What Not to Implement Yet

Do not begin the prototype with:

- persistent user profiles;
- relationship memory;
- demographic inference;
- full sociolinguistic modeling;
- vector databases;
- complex agent orchestration;
- a learned policy model;
- fine-tuning;
- automated authorship percentages;
- education dashboards;
- or production deployment.

Those components may become useful later.

They are not required to test the core claim.

---

# Prototype Success

The first prototype is successful if it becomes possible to test:

> **Does explicit state-aware next-move selection change the quality and ownership of the human reasoning that follows?**

It is not successful merely because:

- the conversation feels intelligent;
- the questions sound Socratic;
- the final artifact is good;
- or the controller is architecturally elaborate.

The first implementation should be small enough that if a simple prompt performs just as well, the project can discover that quickly.

---

# Engineering Principle

> **Implement the smallest architecture capable of being wrong.**

The purpose of the prototype is not to prove Deliberation Room.

It is to turn the architecture into something that can fail clearly enough to learn from.
