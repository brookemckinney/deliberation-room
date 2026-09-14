# Roadmap

Deliberation Room is currently a **research specification and conceptual interaction architecture**.

The project is intentionally ahead of implementation.

The next phase is not to add substantially more conceptual surface area. It is to test whether the architecture can be implemented simply enough to remain useful, inspectable, privacy-aware, and empirically defensible.

---

## Current State

The repository currently specifies:

- governing principles;
- a four-model interaction state;
- a cognition-preserving next-move policy;
- a composition boundary;
- conceptual and linguistic provenance;
- deliberation traces;
- metacognitive feedback;
- provisional state schemas;
- privacy and misuse risks;
- research hypotheses;
- an evaluation framework;
- related-work positioning;
- and initial application domains.

These components are **architectural proposals**, not validated production mechanisms.

No implementation should be assumed correct merely because it conforms to the current specification.

---

# Phase 1 — Specification Stabilization

## Goal

Make the architecture internally coherent enough to prototype without adding unnecessary complexity.

### Current priorities

- [x] Define governing principles.
- [x] Define the four interacting models.
- [x] Define the next-move policy.
- [x] Define the composition boundary.
- [x] Define cognitive provenance.
- [x] Define provisional interaction-state representation.
- [x] Define provisional deliberation-trace representation.
- [x] Define major failure modes.
- [x] Define privacy threat model.
- [x] Define research hypotheses.
- [x] Define evaluation dimensions.
- [x] Map major related-work traditions.
- [x] Provide communication and education examples.
- [ ] Complete terminology and naming consistency audit.
- [ ] Harden primary-source citations in related work.
- [ ] Identify the smallest architecture that can support a useful prototype.

### Exit criterion

The specification is stable enough that implementation decisions can be made without inventing major missing concepts during coding.

---

# Phase 2 — Minimal Controller Prototype

## Goal

Build the smallest executable system capable of demonstrating the central architectural claim:

> **The system can select a cognition-preserving next move instead of defaulting directly to unrestricted answer generation.**

The first prototype should be deliberately narrow.

It does **not** need to implement the entire architecture.

---

## Minimal prototype scope

A first controller may represent only:

```text
CURRENT CLAIM

UNRESOLVED ASSUMPTION

CONTRADICTION

UNCERTAINTY

CONCEPTUAL STABILITY
```

and select among a constrained action set such as:

```text
CLARIFY
DISTINGUISH
REQUEST_EVIDENCE
COUNTEREXAMPLE
REFLECT
WITHHOLD
TRANSITION_TO_COMPOSITION
```

This is enough to begin testing whether explicit next-move selection changes the interaction.

---

## Initial implementation questions

- [ ] What is the minimum useful state representation?
- [ ] How should state extraction work?
- [ ] How should candidate moves be generated?
- [ ] How should candidate moves be ranked?
- [ ] What evidence should trigger `WITHHOLD`?
- [ ] What evidence should trigger `TRANSITION_TO_COMPOSITION`?
- [ ] How should state updates preserve epistemic status?
- [ ] How should human rejection update the controller?
- [ ] How should system proposals remain distinguishable from human cognition?

---

## Prototype constraint

The first implementation should resist the temptation to reproduce every field currently represented in the research schemas.

The question is not:

> **Can we implement the entire specification?**

It is:

> **What is the smallest implementation capable of testing the central architecture?**

---

# Phase 3 — Baseline Comparison

## Goal

Compare the controller against simpler alternatives.

At minimum:

```text
A. unrestricted generative assistant

B. generic Socratic assistant

C. Deliberation Room controller
```

Potential early tasks should be narrow enough to code and evaluate reliably.

Candidate domains:

- short argument evaluation;
- literary interpretation;
- explanation of a reasoning problem;
- low-stakes communication deliberation.

---

## Early outcomes

The first study does not need to prove the entire research program.

Priority measures should include:

```text
INDEPENDENT EXPLANATION

HUMAN-ORIGINATED DISTINCTIONS

SUBSTANTIVE REVISION

QUESTION-RESOLUTION ATTRIBUTION

RESPONSE TO NEW COUNTEREXAMPLE

SYSTEM COGNITIVE SUBSTITUTION
```

Secondary measures may include:

```text
artifact quality

task time

frustration

perceived usefulness
```

---

# Phase 4 — Provenance Prototype

## Goal

Test whether meaningful reasoning development can be represented without reducing contribution to token origin.

The initial trace should focus on a small number of event types.

Possible events:

```text
HUMAN_CLAIM

SYSTEM_CHALLENGE

HUMAN_REVISION

HUMAN_DISTINCTION

SYSTEM_PROPOSAL

HUMAN_RECOGNITION

HUMAN_REJECTION

UNCERTAINTY_RETAINED

COMPOSITION_TRANSITION
```

---

## Initial provenance questions

- [ ] Can human coders agree on conceptual provenance?
- [ ] Can system classification approximate human coding?
- [ ] What counts as meaningful recognition?
- [ ] When should an idea be classified as jointly developed?
- [ ] Can conceptual provenance remain separate from linguistic provenance?
- [ ] Which trace events predict later independent explanation?

---

# Phase 5 — Metacognitive Feedback

## Goal

Determine whether the trace can generate useful feedback about how reasoning developed.

Examples:

> Counterexamples preceded most substantive revisions in this task.

> Claims emerged independently, while warrants required more elicitation.

> Several system interpretations were rejected before the final distinction stabilized.

The first objective is **descriptive accuracy**, not psychological profiling.

---

## Required safeguards

- [ ] Feedback remains task-level by default.
- [ ] Generalizations preserve confidence and scope.
- [ ] Human correction is supported.
- [ ] Fixed cognitive "types" are avoided.
- [ ] Feedback is tested for usefulness, not merely plausibility.

---

# Phase 6 — Four-Model Ablation

## Goal

Determine whether all four models materially improve next-move selection.

Compare the full architecture against versions removing:

```text
PERSON / REASONING MODEL

LINGUISTIC / SOCIOLINGUISTIC MODEL

INTERACTION MODEL

PROVENANCE-AWARE POLICY
```

If a component does not improve relevant outcomes, simplify the architecture.

---

# Phase 7 — Sociolinguistic and Interactional Policy

## Goal

Test the claim that language and social meaning can affect which cognitive move should be selected, not merely how a chosen move should be worded.

Candidate tasks should vary:

- role;
- familiarity;
- power;
- register;
- humor;
- discourse community;
- and interactional permissions.

Priority question:

> **Does modeling situated social meaning improve action selection enough to justify the added complexity and privacy cost?**

---

# Phase 8 — Data-Minimized Personalization

## Goal

Compare personalization using:

```text
FULL RAW HISTORY

SUMMARIZED HISTORY

STRUCTURED STATE

SESSION-ONLY STATE

NO PERSONALIZATION
```

Evaluate:

- next-move quality;
- correction rate;
- privacy exposure;
- model accuracy;
- storage volume;
- and reconstruction risk.

---

# Phase 9 — Small / Local Model Feasibility

## Goal

Test whether the constrained control problem can be handled by smaller or local models.

Candidate functions include:

```text
STATE EXTRACTION

MOVE CLASSIFICATION

MOVE RANKING

CONTRADICTION DETECTION

UNCERTAINTY ESTIMATION

PROVENANCE CLASSIFICATION

COMPOSITION-READINESS DETECTION
```

The relevant comparison is not whether a small model can match frontier-model prose generation.

It is whether a smaller model can perform the **controller functions** adequately.

---

# Phase 10 — Composition and Semantic Preservation

## Goal

Implement the deliberation-to-composition boundary.

Test whether a composition layer can preserve:

```text
CLAIM

DISTINCTION

UNCERTAINTY

WARRANT

COMMITMENT

STANCE

ATTRIBUTION
```

while substantially changing wording, structure, genre, or register.

Priority failure mode:

```text
SEMANTIC DRIFT
```

---

# Phase 11 — Domain Policies

## Goal

Develop domain-specific walking rules without changing the general control architecture.

Candidate domains:

```text
LITERATURE

HISTORY

SCIENCE

DESIGN

ETHICS

RHETORIC

PROFESSIONAL COMMUNICATION
```

Each domain should define:

```text
WHAT COUNTS AS EVIDENCE

WHAT MUST BE TESTED

WHAT ALTERNATIVES MATTER

WHAT UNCERTAINTY IS LEGITIMATE

WHAT MAKES JUDGMENT STABLE
```

---

# Phase 12 — Longitudinal Evaluation

## Goal

Determine whether repeated use changes human capability.

Important outcomes include whether users become more able to independently:

- generate counterexamples;
- identify assumptions;
- articulate warrants;
- preserve uncertainty;
- revise claims;
- and recognize when further deliberation is unnecessary.

A particularly important possibility is:

```text
USER NEEDS LESS SYSTEM INTERVENTION OVER TIME
```

That outcome should be tested rather than assumed.

---

# What Not to Build Yet

The project should avoid prematurely building:

- a giant universal user profile;
- a complex vector-memory system;
- a proprietary "cognitive type" classifier;
- an automated AI-authorship percentage;
- a production-grade educational dashboard;
- broad institutional surveillance;
- a full-domain ontology;
- or a large agentic platform.

Those systems would introduce substantial complexity before the core claim has been tested.

---

# Immediate Next Milestone

The immediate engineering milestone is:

> **A minimal stateful controller that can inspect one bounded reasoning task, choose among a small set of next moves, preserve the distinction between system and human contribution, and stop when further intervention has little value.**

A useful first prototype should make this loop executable:

```text
HUMAN INPUT
      ↓
EXTRACT MINIMAL STATE
      ↓
GENERATE CANDIDATE MOVES
      ↓
RANK MOVES
      ↓
SELECT / WITHHOLD
      ↓
HUMAN RESPONSE
      ↓
UPDATE STATE
      ↺
```

If that loop cannot outperform a much simpler prompt, the architecture should become simpler.

That result would be useful.

---

# Research Discipline

At every phase, preserve the distinction among:

```text
ARCHITECTURAL COMMITMENT

WORKING HYPOTHESIS

IMPLEMENTATION PROPOSAL

EMPIRICAL FINDING
```

The roadmap should change as evidence accumulates.

The goal is not to prove the current architecture correct.

The goal is to make it concrete enough to discover where it is wrong.
