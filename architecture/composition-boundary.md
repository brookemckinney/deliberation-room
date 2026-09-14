# Composition Boundary

The Composition Boundary defines the transition between cognition-oriented interaction and artifact-oriented generation.

Deliberation Room separates two activities that conventional generative systems often collapse:

```text
DELIBERATION
What does the human think?

COMPOSITION
How should that thinking be represented?
```

The distinction is central to the architecture.

The system should not mistake its ability to produce a coherent artifact for evidence that the human has developed the judgment represented by that artifact.

---

## Core Principle

The default architecture is:

```text
HUMAN CONTRIBUTION
        ↓
DELIBERATION
        ↓
STABILIZED HUMAN JUDGMENT
        ↓
OPTIONAL COMPOSITION SUPPORT
        ↓
TRACEABLE ARTIFACT
```

Generation is therefore not the default terminal action of every interaction turn.

During deliberation, the system primarily attempts to preserve and elicit human cognition.

During composition, the system may take substantially more responsibility for linguistic realization.

The transition between those modes should be explicit enough to preserve provenance.

---

## Why the Boundary Exists

A fluent model can generate language that appears more conceptually stable than the human's underlying representation actually is.

For example:

```text
HUMAN STATE

"I think it has something to do with authority and maybe
how Creon thinks changing his mind makes him weak?"
```

A generative system could immediately produce:

> Creon's tragic failure arises from a conception of political authority
> in which revisability is mistaken for weakness, causing him to equate
> personal judgment with legitimate rule.

That may be an excellent sentence.

But its quality does not establish that the human:

- recognizes the distinction;
- understands its implications;
- can defend it;
- can connect it to evidence;
- would retain it under challenge;
- or could independently apply it elsewhere.

The generated artifact can therefore exceed the human cognitive state.

Deliberation Room treats that gap as architecturally important.

---

## Artifact Quality Is Not Cognitive Evidence

A polished artifact can conceal:

```text
UNRESOLVED ASSUMPTIONS
MISSING WARRANTS
UNEXAMINED CONTRADICTIONS
BORROWED CONCEPTS
UNRECOGNIZED SYSTEM PROPOSALS
SEMANTIC DRIFT
FALSE CERTAINTY
```

Therefore:

> **Artifact quality should not be used as a proxy for human understanding.**

This becomes especially important in educational settings, where the artifact may be evaluated as evidence of learning.

---

## Two Different Optimization Targets

During deliberation, the architecture optimizes approximately for:

> **What should the human be able to do next?**

During composition, the objective changes toward:

> **How can the human's stabilized judgment be represented effectively for its intended purpose?**

Possible composition objectives include:

- organization;
- clarity;
- rhetorical effectiveness;
- compression;
- elaboration;
- audience adaptation;
- genre conformity;
- accessibility;
- stylistic realization;
- semantic preservation;
- and linguistic precision.

These objectives are legitimate.

They are simply not the same objective as cognition elicitation.

---

## The Boundary Is Not a Moral Ranking

Deliberation is not inherently superior to composition.

Composition support can:

- reduce low-level friction;
- support accessibility;
- externalize working memory;
- improve clarity;
- enable rhetorical experimentation;
- reduce unnecessary linguistic labor;
- and allow humans to focus attention on higher-value judgment.

The architectural concern is not:

```text
AI writing = bad
```

It is:

```text
AI composition should not be mistaken for human cognition.
```

---

## Transition Conditions

A transition to composition may occur when one or more of the following are true:

### Human explicitly requests composition

Examples:

> "Write this."

> "Turn this into an email."

> "Okay, now make the argument."

> "Give me the polished version."

> "I know what I mean. Help me say it."

Human control can override the default deliberative mode.

### Sufficient conceptual stability

The current model has survived enough relevant testing for the task.

Possible indicators include:

- central claim is explicit;
- key distinctions are represented;
- major assumptions are visible;
- relevant warrants have been examined;
- important contradictions have been addressed;
- uncertainty is represented;
- the human has recognized material system proposals;
- and further elicitation has low expected value.

### Remaining uncertainty is external

The remaining uncertainty may depend primarily on:

- another person's future response;
- unavailable evidence;
- future events;
- empirical observation;
- or information the human cannot reasonably access through further reflection.

A useful stopping heuristic is:

> **The remaining uncertainty belongs primarily to the other person, the world, or future evidence — not to an unresolved defect in the current human model.**

### Deliberation is no longer useful

Additional questioning may begin to produce:

- repetition;
- rumination;
- diminishing information gain;
- frustration;
- unnecessary disclosure;
- or artificial complexity.

The architecture should not require endless cognition before granting composition support.

---

## Explicit Human Override

The human may request composition before the architecture would otherwise recommend it.

For example:

> "I don't want to think through this right now. Just draft it."

The system should generally honor that request.

Cognition preservation should not become paternalism.

The system may still preserve the resulting provenance:

```text
conceptual_source:
PARTIALLY_RESOLVED

composition_source:
SYSTEM-GENERATED
```

The architecture should distinguish:

```text
ALLOWING GENERATION
```

from:

```text
PRETENDING THE RESULT WAS HUMAN-DEVELOPED
```

---

## Composition Readiness Is Task-Relative

There is no universal amount of deliberation required before composition.

The threshold should depend on:

- purpose;
- stakes;
- domain;
- audience;
- reversibility;
- evaluation context;
- human request;
- and consequences of error.

For example:

```text
casual text message
```

may require very little conceptual stabilization.

A:

```text
high-stakes professional recommendation
```

may require more.

An:

```text
educational artifact intended as evidence of student reasoning
```

may require substantially stronger provenance.

The architecture should therefore avoid a universal "readiness score."

---

## Composition Contract

At the transition boundary, the system can construct a provisional **composition contract**.

This specifies what the composition layer is allowed to preserve, alter, or introduce.

A conceptual representation might be:

```yaml
composition_contract:

  purpose:
    type: professional_email

  audience:
    relationship: colleague

  preserve:
    - central_claim
    - uncertainty
    - key_distinction
    - user_position
    - factual_qualifications

  may_transform:
    - organization
    - syntax
    - concision
    - register
    - rhetorical sequencing

  may_not_introduce_without_confirmation:
    - new substantive claims
    - new factual assertions
    - stronger certainty
    - new motives attributed to others
    - new commitments
    - new emotional states

  target:
    concise
    warm
    direct
```

This schema is illustrative.

Its purpose is to make rhetorical transformation inspectable.

---

## Rhetorical Transposition

Composition is better understood as **rhetorical transposition** than simple rewriting.

The system attempts to preserve the underlying human model while adapting its expression for:

- audience;
- purpose;
- medium;
- genre;
- role;
- register;
- stakes;
- and interactional context.

Conceptually:

```text
STABILIZED HUMAN MODEL
          ↓
RHETORICAL CONDITIONS
          ↓
TRANSPOSITION
          ↓
ARTIFACT
```

The objective is not lexical similarity.

It is preservation of relevant meaning across changed rhetorical conditions.

---

## Semantic Invariants

Before composition, the architecture may identify semantic invariants.

These are elements that should survive rhetorical transposition.

For example:

```text
INVARIANT 1
The user is not objecting to unequal effort itself.

INVARIANT 2
The user is objecting to lack of mutual attentiveness.

INVARIANT 3
The user does not claim to know the recipient's motives.

INVARIANT 4
The user wants to invite response rather than demand agreement.
```

Many possible surface realizations could preserve those invariants.

A composition that violates one of them has changed the underlying model.

---

## Constraints Versus Invariants

A useful distinction is:

```text
INVARIANT
Something about the human's meaning that must survive.

CONSTRAINT
A condition governing how the artifact may be realized.
```

For example:

```text
INVARIANT
"I am uncertain about her motive."

CONSTRAINT
"Do not make the email longer than 200 words."
```

Both matter.

But they play different architectural roles.

---

## Semantic Drift

Semantic drift occurs when composition changes the underlying representation.

Example:

```text
HUMAN MODEL
"I don't think she doesn't care. I don't know where I fit
into her decisions."
```

System composition:

> "I feel uncared for when you exclude me from your decisions."

This introduces at least two changes:

```text
UNKNOWN MOTIVE / RELATIONAL POSITION
        ↓
CLAIM ABOUT CARE

UNCERTAINTY
        ↓
ASSERTION
```

The sentence may sound rhetorically clean.

It is nevertheless a poor transposition.

---

## Drift Detection

A future composition layer may compare the artifact against represented semantic invariants.

Candidate checks include:

```text
CLAIM PRESERVATION
UNCERTAINTY PRESERVATION
WARRANT PRESERVATION
DISTINCTION PRESERVATION
COMMITMENT PRESERVATION
AGENCY PRESERVATION
ATTRIBUTION PRESERVATION
STANCE PRESERVATION
```

A composition should be flagged when it:

- strengthens a claim;
- removes meaningful uncertainty;
- introduces a motive;
- collapses a distinction;
- adds a commitment;
- changes who is responsible for an action;
- or converts a possibility into a fact.

---

## Linguistic Change Is Not Necessarily Semantic Change

Consider:

```text
HUMAN
"I don't care if we do equal amounts. I care whether we're
both noticing each other."
```

System composition:

> "The issue isn't strict reciprocity; it's mutual attentiveness."

The wording changes substantially.

The underlying distinction may remain intact.

Therefore:

```text
TOKEN DIFFERENCE
≠
SEMANTIC DIFFERENCE
```

This distinction is essential for both composition and provenance.

---

## Conceptual and Linguistic Provenance

Composition should preserve at least two provenance dimensions.

### Conceptual provenance

Who introduced or developed the substantive idea?

Possible states include:

```text
HUMAN-ORIGINATED
SYSTEM-PROPOSED → HUMAN-RECOGNIZED
SYSTEM-PROPOSED → HUMAN-REVISED
JOINTLY-DEVELOPED
SYSTEM-SUPPLIED / HUMAN-UPTAKE-UNRESOLVED
```

### Linguistic provenance

Who supplied the artifact's verbal realization?

Possible states include:

```text
HUMAN-PRESERVED
HUMAN-EDITED
SYSTEM-TRANSPOSED
SYSTEM-GENERATED
JOINTLY-REFINED
```

These dimensions should not be collapsed.

---

## Example Provenance

Consider:

```text
HUMAN
"I think the problem isn't the law exactly. It's like he thinks
being king means his judgment and the state's interest are the same."
```

Later composition:

> Creon's failure is not reducible to unjust law; it emerges from his
> inability to distinguish his own judgment from the interests of the state.

A useful provenance representation might be:

```yaml
claim:
  conceptual_provenance: HUMAN-ORIGINATED
  linguistic_provenance: SYSTEM-TRANSPOSED
  semantic_preservation: supported
```

The model helped write the sentence.

It did not originate the distinction.

---

## System-Introduced Content During Composition

Composition may occasionally require content not already represented in the stabilized model.

Examples include:

- transitions;
- genre conventions;
- explanatory context;
- headings;
- examples;
- definitions;
- citations;
- or rhetorical framing.

The system should distinguish between:

```text
STRUCTURAL / RHETORICAL ADDITION
```

and:

```text
SUBSTANTIVE COGNITIVE ADDITION
```

A transition such as:

> "However, this distinction matters for a second reason."

is different from introducing an entirely new reason.

Material substantive additions should preserve provenance and may require human review.

---

## Composition Can Return to Deliberation

The boundary is not one-way.

Composition itself can expose instability.

For example, while drafting, the system may discover:

```text
Two stabilized claims cannot be expressed together without contradiction.
```

or the human may say:

> "No. Seeing it written like that, I don't actually believe the second part."

The architecture should permit:

```text
DELIBERATION
     ↓
COMPOSITION
     ↓
INSTABILITY DISCOVERED
     ↓
RETURN TO DELIBERATION
     ↓
REVISED MODEL
     ↓
COMPOSITION
```

Composition can therefore function as another form of model inspection.

---

## Human Rejection During Composition

A rejected sentence is not merely failed copy.

It may reveal:

- semantic drift;
- incorrect register;
- incorrect stance;
- wrong interactional assumptions;
- an unstable concept;
- a previously hidden distinction;
- or a new constraint.

For example:

> "No, that's prettier, but it makes me sound more certain than I am."

updates:

```text
LINGUISTIC MODEL
Preferred realization preserves epistemic tentativeness.

COGNITIVE MODEL
Uncertainty is substantive, not incidental.

COMPOSITION CONTRACT
Do not increase certainty.
```

Rejection remains information.

---

## Rhetorical Transposition and the Four Models

Composition continues to use all four models.

### Cognitive State Model

What substantive representation must survive?

### Person / Reasoning Model

What established conceptual structures or explanatory forms remain useful?

### Linguistic / Sociolinguistic Model

How should meaning be realized in this discourse environment?

### Interaction Model

What will the artifact do between these participants in this situation?

Composition is therefore not:

```text
COGNITIVE OUTPUT
      ↓
STYLE FILTER
```

It remains a situated interaction problem.

---

## Composition Modes

Future implementations might expose different levels of composition assistance.

For example:

### Preserve

Maintain most human wording while improving mechanics.

```text
grammar
clarity
formatting
minor syntax
```

### Transpose

Preserve the human model while substantially changing rhetorical realization.

```text
audience
register
organization
genre
concision
```

### Collaborate

Human and system iteratively develop the artifact while preserving provenance of substantive additions.

### Generate

System produces a complete artifact from the available model.

These modes could make the degree of linguistic system contribution explicit.

---

## Educational Composition Boundary

The boundary becomes especially important when an artifact is intended as evidence of learning.

A learner might enter with:

> "Antigone is about whether you should follow laws."

Through deliberation:

```text
INITIAL CLAIM
        ↓
COUNTEREXAMPLE
        ↓
REVISION
        ↓
DISTINCTION
        ↓
EVIDENCE
        ↓
STABILIZED JUDGMENT
```

The learner eventually establishes:

> "The problem isn't only whether Creon's law is just. His conception
> of authority makes him unable to treat disagreement as information."

The system may then help compose an essay.

The resulting artifact can be connected to a trace showing that the substantive judgment developed through human reasoning.

---

## Cognitive Provenance Versus AI Detection

This suggests a different educational question.

Instead of:

> **Did AI write this?**

ask:

> **Can the learner account for the judgments embodied in this artifact?**

A learner who participated in the reasoning can potentially explain:

- where the claim came from;
- what challenged it;
- what changed;
- which evidence mattered;
- which system proposals were rejected;
- which distinctions were retained;
- and what remains uncertain.

This is evidence of intellectual accountability.

It does not require pretending that every final token was manually produced by the learner.

---

## Traceable Artifact

A traceable artifact may link final substantive elements to their deliberative histories.

Conceptually:

```text
FINAL CLAIM
    │
    ├── originated: HUMAN
    │
    ├── challenged by: COUNTEREXAMPLE #4
    │
    ├── revised at: STATE 7
    │
    ├── evidence linked: E2, E5
    │
    ├── stabilized: STATE 11
    │
    └── final wording: SYSTEM-TRANSPOSED
```

The goal is not surveillance.

The goal is to preserve enough provenance to distinguish **cognitive development** from **surface production**.

---

## Data Minimization at the Boundary

The composition boundary may also create an opportunity for data minimization.

Once a stable abstract representation exists, an implementation may not need the complete raw deliberation history for every subsequent operation.

Conceptually:

```text
RAW INTERACTION
       ↓
STRUCTURED STATE
       ↓
STABILIZED MODEL
       ↓
MINIMAL COMPOSITION CONTRACT
       ↓
COMPOSITION
```

Whether raw interaction can safely be discarded depends on:

- audit requirements;
- user preference;
- provenance requirements;
- error recovery;
- and implementation design.

But the architecture should investigate whether useful state abstraction can reduce reliance on persistent raw conversation history.

---

## Local Composition

The separation between deliberation state and composition also creates an implementation question:

> **How much generative capability is actually required at each stage?**

Possible architectures might use:

```text
SMALL / LOCAL CONTROLLER
        +
STRUCTURED STATE
        +
OPTIONAL LARGER COMPOSITION MODEL
```

or:

```text
FULLY LOCAL DELIBERATION
        +
USER-SELECTED COMPOSITION SERVICE
```

or:

```text
LOCAL STATE + POLICY
        +
REMOTE GENERATION WITH MINIMIZED CONTEXT
```

These are hypotheses, not claims about current performance.

The architectural separation makes them testable.

---

## Composition Without Raw Personal History

If the system can construct a sufficiently informative composition contract, a composition model may receive something closer to:

```yaml
purpose: personal_message

audience:
  relationship: close_friend

semantic_invariants:
  - "user wants closeness"
  - "user is not demanding commitment"
  - "uncertainty about future should remain explicit"

interactional_constraints:
  - "low pressure"
  - "high response latitude"
  - "do not imply obligation"

linguistic_requirements:
  - "informal"
  - "warm"
  - "established shared vocabulary permitted"
```

rather than an entire personal conversation history.

Whether this abstraction preserves sufficient quality is an empirical question.

If successful, it could materially reduce disclosure to the composition model.

---

## Boundary Failures

### Premature composition

The system generates polished language before the human model is sufficiently developed.

### Hidden composition

The system effectively supplies the conclusion while presenting the interaction as deliberation.

### Provenance collapse

System-originated concepts are represented as human-originated because they appear in the final artifact.

### Semantic drift

Rhetorical transformation changes the human's substantive meaning.

### Certainty inflation

Composition removes meaningful uncertainty.

### Attribution inflation

The artifact claims knowledge of another person's motive, state, or intention that the human did not possess.

### Commitment inflation

The artifact makes promises or commitments beyond the human's established intent.

### Style substitution

The system's preferred rhetorical form replaces the user's intended stance.

### Composition lock-in

Once drafting begins, the system fails to return to deliberation when instability becomes visible.

### Friction ideology

The system refuses useful composition support because it treats effort itself as evidence of cognition.

---

## What This Boundary Must Preserve

Across the transition from deliberation to composition, the architecture should preserve:

```text
HUMAN AGENCY
SEMANTIC INTENT
EPISTEMIC STATUS
MATERIAL UNCERTAINTY
CONCEPTUAL PROVENANCE
LINGUISTIC PROVENANCE
ABILITY TO REVISE
ABILITY TO RETURN TO DELIBERATION
```

The final artifact should not erase the process by which its substantive judgments emerged.

---

## Architectural Summary

```text
                    DELIBERATION
                         │
                         ↓
               COGNITIVE STATE MODEL
                         │
                         ↓
              CONCEPTUAL STABILITY?
                    ↙         ↘
                  NO           YES
                  │             │
             NEXT MOVE      HUMAN READY?
                  │          ↙       ↘
                  ↺        NO         YES
                            │           │
                            ↺           ↓
                              COMPOSITION CONTRACT
                                       │
                                       ↓
                              RHETORICAL TRANSPOSITION
                                       │
                                       ↓
                                DRIFT CHECK
                                  ↙        ↘
                              FAILED       PASSED
                                │             │
                         DELIBERATION /       ↓
                         REVISION        TRACEABLE ARTIFACT
```

The human may explicitly request composition at any point.

In that case, the system can cross the boundary while preserving the actual state of conceptual and linguistic provenance.

---

## Research Questions

Key open questions include:

1. What evidence is sufficient to classify a human judgment as conceptually stable?
2. How should stability thresholds vary by task and stakes?
3. How can explicit human readiness be incorporated into the transition policy?
4. What semantic invariants can be extracted reliably?
5. How should a composition contract be represented?
6. Can semantic drift be detected reliably across substantial rhetorical transposition?
7. How should uncertainty preservation be evaluated?
8. Can conceptual and linguistic provenance be tracked independently at useful granularity?
9. How should system-introduced substantive content during composition be handled?
10. When should composition automatically return to deliberation?
11. Can a traceable artifact provide meaningful evidence of human intellectual accountability?
12. Which provenance signals correlate with later independent explanation or transfer?
13. Can structured state replace raw conversation history for composition without unacceptable quality loss?
14. How much personal information does a composition model actually require?
15. Can deliberation and composition be distributed across models of different sizes or locations?
16. Can local state abstraction materially reduce disclosure to remote generative models?
17. How should composition support differ when the artifact itself is being used as evidence of learning?
18. How can the architecture preserve accessibility benefits of generation without conflating reduced production labor with reduced cognition?
