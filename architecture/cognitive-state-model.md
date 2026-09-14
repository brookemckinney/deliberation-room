# Cognitive State Model

The Cognitive State Model represents what the human currently appears to understand, believe, distinguish, question, or remain uncertain about with respect to the current problem.

Its purpose is not to estimate general intelligence, personality, or stable ability.

Its unit of analysis is the current deliberative state.

The central question is:

> **What does the human currently appear to understand?**

---

## Why this model exists

Generative systems frequently collapse several different things into one conversational context:

- what the human explicitly said;
- what the system inferred;
- what the system proposed;
- what the human accepted;
- what the human rejected;
- what remains uncertain;
- and what the system itself currently believes is likely.

Deliberation Room separates these because they have different epistemic status.

A system-generated interpretation should not become part of the human's represented cognition merely because it was plausible or well phrased.

The Cognitive State Model therefore tracks both **content** and **provenance**.

---

## Candidate State Dimensions

Possible represented features include:

- observations;
- candidate claims;
- stabilized claims;
- distinctions;
- assumptions;
- warrants;
- evidence;
- counterevidence;
- contradictions;
- competing explanations;
- counterexamples;
- unresolved questions;
- missing information;
- uncertainty;
- confidence;
- conceptual dependencies;
- revision history;
- conceptual stability.

These dimensions are provisional.

Part of the research program is determining the minimum representation necessary for useful next-move selection.

---

## Epistemic Status

Every represented element should preserve its epistemic status.

At minimum:

```text
OBSERVED
INFERRED
HYPOTHESIZED
USER-CONFIRMED
CONTRADICTED
UNKNOWN
```

For example:

```text
OBSERVED
The user said: "I think the problem is the law."

HYPOTHESIZED
The user's argument may depend on the assumption that a just law
would remove the central conflict.

UNKNOWN
Whether the user has considered a counterexample involving a just law.

USER-CONFIRMED
"Yeah, actually, if the law were good I still think Creon would be
the problem."

CONTRADICTED
The earlier representation that the user's claim was fundamentally
about unjust law.
```

The system should never silently promote:

```text
HYPOTHESIZED → USER-CONFIRMED
```

without interactional evidence.

---

## Source Provenance

Epistemic status and source provenance are related but distinct.

A representation may also record where it originated.

Possible source labels include:

```text
HUMAN-ORIGINATED
SYSTEM-PROPOSED
JOINTLY-DEVELOPED
EXTERNAL-EVIDENCE
UNKNOWN
```

For example:

```text
claim:
  content: "Creon's failure concerns how he understands authority."
  source: HUMAN-ORIGINATED
  epistemic_status: USER-CONFIRMED
```

versus:

```text
claim:
  content: "Creon's failure concerns how he understands authority."
  source: SYSTEM-PROPOSED
  epistemic_status: HYPOTHESIZED
```

Those states should not be treated as equivalent.

---

## Conceptual Units

The model should distinguish among different kinds of cognitive objects.

### Observation

A statement about what has been noticed, encountered, measured, or experienced.

Example:

> "Creon refuses to change course even after multiple warnings."

### Interpretation

A proposed meaning assigned to observations.

Example:

> "He thinks changing his mind would weaken his authority."

### Claim

A proposition the human may eventually defend.

Example:

> "Creon's political failure comes from treating authority as incompatible with revisability."

### Assumption

A proposition currently required by a claim but not yet established.

Example:

> "A ruler who revises publicly will necessarily lose legitimacy."

### Warrant

The reasoning connecting evidence to a claim.

Example:

```text
Evidence:
Creon treats disagreement as disloyalty.

Warrant:
A ruler who equates disagreement with disloyalty cannot use dissent
as corrective information.

Claim:
Creon's conception of authority makes his judgment less reliable.
```

### Distinction

A conceptual separation that changes the structure of the problem.

Example:

```text
legitimacy of a law
≠
quality of a ruler's judgment
```

### Counterexample

A case capable of testing the current representation.

Example:

> What if Creon had enacted a morally defensible law but reasoned about his authority in exactly the same way?

### Contradiction

Two represented propositions that cannot both remain true in their current form.

### Uncertainty

A known area where the human does not currently have sufficient grounds for a stable judgment.

Uncertainty should be represented rather than automatically resolved.

---

## Distinctions as High-Value Events

A major function of deliberation is often the production of distinctions.

For example:

```text
being ignored
≠
being selectively attended to
```

or:

```text
law versus morality
≠
authority versus fallibility
```

A new distinction can restructure several other state elements at once.

It may:

- invalidate an earlier claim;
- resolve a contradiction;
- expose a new assumption;
- alter what evidence is relevant;
- or produce a new question.

Distinctions should therefore be represented as first-class state changes rather than merely text appearing in conversation.

---

## Revision

The architecture should preserve how substantive representations change.

A revision event may include:

```text
ORIGINAL CLAIM
        ↓
TRIGGERING MOVE
        ↓
HUMAN RESPONSE
        ↓
REVISED CLAIM
```

For example:

```text
Original:
"The issue is that Creon creates an unjust law."

Trigger:
Counterexample involving a just law.

Human response:
"Wait, I think I would still have the same problem with him."

Revision:
"The issue may be how Creon understands authority rather than the
moral quality of this particular law."
```

This transition is more informative than storing only the final claim.

---

## Conceptual Stability

Conceptual stability describes how well a current representation has survived relevant opportunities for testing.

It does **not** mean:

- objective truth;
- high confidence;
- agreement with the system;
- or absence of uncertainty.

Possible factors include whether the representation has encountered:

- clarification;
- competing explanations;
- counterexamples;
- contradiction checks;
- evidence requests;
- warrant testing;
- perspective shifts;
- explicit uncertainty.

A representation may be stable while remaining conditional.

For example:

> "X currently explains A and B better than Y, but I cannot distinguish them on C."

may be more stable than:

> "Definitely X."

---

## Candidate Stability Representation

A possible implementation might represent:

```yaml
conceptual_stability:
  status: low | emerging | moderate | high
  tested_against:
    - counterexample
    - competing_explanation
    - evidence
    - contradiction
  unresolved:
    - "causal warrant"
  user_confidence: moderate
  system_confidence_in_model: moderate
```

This is illustrative, not a final schema.

The architecture should avoid pretending that a single scalar "stability score" is inherently valid.

---

## Human Correction

Human correction should be treated as a high-value state update.

Examples include:

> "No, that's not what I mean."

> "Those are the same thing to me."

> "I said that badly."

> "Actually, that example breaks my argument."

> "That's true, but it's not relevant."

> "I'm less certain now."

Each can update different parts of the model.

For example:

```text
"That's true, but it's not relevant."
```

may indicate:

- factual acceptance;
- rejection of relevance;
- unchanged claim;
- refined task boundary.

A system that treats this merely as negative preference feedback loses useful cognitive information.

---

## Human Recognition of System Proposals

When the system proposes a concept, the model should track what happens next.

Possible states include:

```text
SYSTEM-PROPOSED → UNRESOLVED
SYSTEM-PROPOSED → HUMAN-RECOGNIZED
SYSTEM-PROPOSED → HUMAN-REVISED
SYSTEM-PROPOSED → HUMAN-REJECTED
```

Recognition should require more than passive continuation when possible.

Evidence of recognition may include:

- restating the idea in the human's own terms;
- applying it to a new case;
- distinguishing it from a nearby concept;
- revising it;
- defending it;
- rejecting part of it;
- or using it coherently in later reasoning.

This directly supports the governing principle:

> **The system may propose. The human must recognize.**

---

## Human-Originated Cognitive Events

The system should explicitly preserve events in which the human introduces substantive structure.

Examples include:

```text
HUMAN-ORIGINATED CLAIM
HUMAN-ORIGINATED DISTINCTION
HUMAN-ORIGINATED COUNTEREXAMPLE
HUMAN-ORIGINATED WARRANT
HUMAN-ORIGINATED QUESTION
HUMAN-IDENTIFIED CONTRADICTION
HUMAN-RETAINED UNCERTAINTY
```

These events matter for:

- cognitive provenance;
- metacognitive feedback;
- educational assessment;
- and evaluation of cognitive agency.

---

## Metacognitive Signal Extraction

The Cognitive State Model can also contribute evidence for later metacognitive feedback.

For example, repeated state transitions may reveal that during a specific deliberation:

- the human revised claims after counterexamples;
- distinctions emerged through analogy;
- uncertainty increased after evidence checking;
- claims appeared quickly but warrants emerged slowly;
- the human generated more productive questions than the system;
- or the human repeatedly corrected semantic framing before conceptual progress occurred.

These should initially be treated as **task-level observed patterns**.

For example:

> "Counterexamples were productive in this deliberation."

is better supported than:

> "You are a counterexample thinker."

Broader claims require broader evidence and should remain corrigible by the human.

---

## Example State

```yaml
cognitive_state:
  observations:
    - id: o1
      content: "Creon refuses multiple opportunities to revise his decision."
      source: HUMAN-ORIGINATED
      epistemic_status: USER-CONFIRMED

  claims:
    - id: c1
      content: "Creon's problem is that he makes an unjust law."
      source: HUMAN-ORIGINATED
      epistemic_status: CONTRADICTED

    - id: c2
      content: "Creon's conception of authority makes revision appear illegitimate."
      source: JOINTLY-DEVELOPED
      epistemic_status: USER-CONFIRMED

  distinctions:
    - id: d1
      content:
        left: "moral quality of the law"
        right: "Creon's model of authority"
      source: HUMAN-ORIGINATED
      epistemic_status: USER-CONFIRMED

  assumptions:
    - id: a1
      content: "Public revision necessarily weakens authority."
      source: INFERRED
      epistemic_status: HYPOTHESIZED

  unresolved_questions:
    - "Does the play generalize this model of authority beyond Creon?"

  uncertainty:
    - topic: "authorial scope"
      level: high

  conceptual_stability:
    status: moderate
    rationale:
      - "central claim survived counterexample"
      - "major distinction explicit"
      - "warrant still requires evidence"
```

The schema is illustrative.

Its purpose is to demonstrate what the architecture needs to preserve conceptually.

---

## What This Model Must Not Do

The Cognitive State Model should not:

- treat system-generated language as human understanding;
- infer stable intelligence from task performance;
- collapse confidence into correctness;
- erase uncertainty;
- convert acceptance into authorship;
- assume rejection means misunderstanding;
- treat the final answer as the only useful state;
- or retain unnecessary cognitive data indefinitely.

---

## Research Questions

Key open questions include:

1. What is the minimum cognitive representation needed for useful next-move selection?
2. Which state variables can be inferred reliably from dialogue?
3. What interactional evidence is sufficient to classify human recognition?
4. How should conflicting claims coexist before resolution?
5. How should revision history be compressed without losing meaningful provenance?
6. Can conceptual stability be measured reliably across domains?
7. How should uncertainty in the system's cognitive-state model itself be represented?
8. Which cognitive events most strongly predict independent human explanation or transfer?
9. Can state transitions support useful metacognitive feedback without overgeneralizing from limited evidence?
10. How much of this state can remain ephemeral rather than persistent?
