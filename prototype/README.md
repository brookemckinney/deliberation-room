# Deliberation Room Prototype

This directory contains the **first executable slice** of Deliberation Room.

It is intentionally incomplete.

The current prototype is a transparent control-core scaffold for testing:

```text
STATE
→ CANDIDATE NEXT MOVES
→ POLICY SELECTION
→ HUMAN RESPONSE
→ STATE UPDATE
```

It is **not yet the full Deliberation Room system**.

The complete target architecture includes two coupled engines:

```text
ENGINE 1
METACOGNITIVE DELIBERATION

ENGINE 2
RHETORICAL COMPILATION
```

with an evidence layer supporting both.

---

# What the Current Prototype Implements

The current code implements:

- minimal structured cognitive state;
- explicit epistemic status;
- conceptual provenance;
- basic next-move selection;
- candidate move ranking;
- `WITHHOLD` as a valid policy action;
- explicit transition to composition;
- separation of move selection from linguistic realization;
- multi-turn state updates;
- explicit human correction;
- extraction contracts;
- pending confirmation for system inference;
- and tests protecting several core architectural invariants.

The current prototype is deliberately inspectable.

It uses simple rules and templates so that policy behavior can be observed directly.

---

# What the Current Prototype Does Not Yet Implement

The current executable prototype does **not yet** implement the full conceptual architecture.

In particular, it does not yet implement:

```text
LIVE METACOGNITIVE PROCESS INFERENCE

ADAPTIVE SELF-PROMPTING

DISCIPLINARY WALKING RULES

FULL SOCIOLINGUISTIC ANALYSIS

EMPIRICAL IDIOLECT MODELING

SPEECH / TEXT FEATURE EXTRACTION

AUDIENCE-SPECIFIC LANGUAGE MODELING

CLASSICAL RHETORICAL COMPILATION

GENRE-SPECIFIC WRITING CONVENTIONS

OPTIONAL WEB / RETRIEVAL SUPPORT

CURRENT CULTURAL / IDIOMATIC RETRIEVAL

SEMANTIC DRIFT DETECTION

INTERACTIONAL DRIFT DETECTION

FULL COMPOSITION OUTPUT

LOCAL / ON-DEVICE INFERENCE
```

These are target components, not implemented claims.

---

# Why the Prototype Is Narrow

The first engineering question is:

> **Can explicit next-move selection be made inspectable and testable before a powerful generative model is allowed to absorb the entire architecture into one hidden prompt?**

The current implementation therefore intentionally separates:

```text
STATE

POLICY

REALIZATION

UPDATE

CONFIRMATION
```

before introducing richer AI inference.

This creates a baseline against which later model-backed components can be evaluated.

---

# Target Product Behavior

A mature Deliberation Room should support interactions more like:

```text
USER

"I need to write her back but I keep explaining the idea
instead of saying the thing I actually want her to feel."

        ↓

ENGINE 1 — METACOGNITIVE DELIBERATION

What is the actual judgment?

What cognitive operation is currently productive?

What should remain for the human to discover?

        ↓

HUMAN JUDGMENT

"I want her to feel loved and like she belongs inside the idea
because I love the way her mind cares about people."

        ↓

ENGINE 2 — RHETORICAL COMPILATION

Exigence:
communicate affection and belonging

Audience:
intimate relationship

Shared context:
high

Rhetorical requirement:
compress rather than explain

Sociolinguistic evidence:
speaker's actual relational register

Interactional requirement:
preserve intimacy and response latitude

        ↓

EXACT FINAL OUTPUT

"You're in it because I love the way your mind loves people."
```

The final output may be highly system-generated linguistically while remaining traceable to human-developed judgment.

---

# Target Architecture

Conceptually:

```text
                        HUMAN INPUT
                             │
                             ▼
                 ┌─────────────────────┐
                 │ COGNITIVE STATE     │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │ METACOGNITIVE       │
                 │ PROCESS MODEL       │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │ SOCIOLINGUISTIC     │
                 │ MODEL               │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │ INTERACTION MODEL   │
                 └──────────┬──────────┘
                            │
                            ▼
                 METACOGNITIVE CONTROLLER
                            │
                            ▼
                     HUMAN RESPONDS
                            │
                            └──────────────↺

                      HUMAN JUDGMENT
                            │
                            ▼
                    COMPOSITION HANDOFF
                            │
                            ▼
                 ┌─────────────────────┐
                 │ EVIDENCE /          │
                 │ RETRIEVAL LAYER     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ RHETORICAL          │
                 │ COMPILER            │
                 └──────────┬──────────┘
                            │
                            ▼
                 SEMANTIC / SOCIAL CHECK
                            │
                            ▼
                   EXACT FINAL OUTPUT
```

---

# Engine 1 — Metacognitive Deliberation

Engine 1 asks:

> **What should the human be able to do next?**

It should eventually model not only:

```text
WHAT THE HUMAN THINKS
```

but:

```text
HOW PRODUCTIVE COGNITIVE MOVEMENT IS CURRENTLY HAPPENING
```

Candidate operations include:

- compare;
- contrast;
- analogize;
- instantiate;
- abstract;
- classify;
- test a counterfactual;
- generate a counterexample;
- expose an assumption;
- construct a warrant;
- evaluate evidence;
- isolate a variable;
- shift perspective;
- identify an invariant;
- synthesize;
- revise;
- reject;
- stabilize judgment.

The system should use the human's responses as evidence about what kinds of intervention are currently productive.

That evidence can recursively alter the next system instruction.

For example:

```text
CURRENT TASK EVIDENCE

counterfactuals:
productive

open-ended explanation:
low-value

contrast:
productive

SYSTEM PROPOSALS:
frequently revised rather than accepted
```

may generate an internal control instruction:

```text
Use one single-variable counterfactual.

Do not name the likely distinction.

Ask what remains invariant.

Avoid another open-ended explanation prompt.
```

This is the intended adaptive metacognitive behavior.

The current prototype does not yet infer this automatically.

---

# Engine 2 — Rhetorical Compilation

Engine 2 asks:

> **Given what this human means, what exactly should this human say or write to this audience, for this purpose, in this situation?**

The compiler should eventually combine:

```text
STABILIZED HUMAN JUDGMENT

CLASSICAL RHETORICAL SITUATION

AUDIENCE

EXIGENCE

PURPOSE

ETHOS

PATHOS

LOGOS

KAIROS

CONSTRAINTS

AVAILABLE MEANS

INTERACTIONAL CONDITIONS

POWER

ROLE

FACE

BELONGING

RESPONSE LATITUDE

LINGUISTIC / SOCIOLINGUISTIC EVIDENCE

OBSERVED SPEECH / TEXT BEHAVIOR

GENRE CONVENTIONS

DISCIPLINARY CONVENTIONS

RELEVANT EXTERNAL EVIDENCE
```

to produce:

```text
THE EXACT FINAL UTTERANCE
```

The intended architecture is therefore not:

```text
reason
→ generic prose
→ tone adjustment
```

It is:

```text
human judgment
× rhetorical situation
× audience
× relationship
× discourse environment
× idiolect
× observed language behavior
× genre
× evidence
        ↓
situated rhetorical realization
```

---

# Linguistic and Sociolinguistic Layer

The target system should eventually use actual linguistic evidence rather than generic style labels.

Possible evidence includes:

```text
lexical choices

syntax

sentence length

cadence

punctuation

capitalization

discourse markers

directness

compression

elaboration

repair behavior

humor

irony

code-switching

register

stance

role language

discourse-community conventions

shared relational language

local semantic meanings

idiom
```

The system should distinguish:

```text
UNDERSTAND A FORM
```

from:

```text
HAVE PERMISSION TO PERFORM A FORM
```

For example:

```text
the system may understand that "bro" is affiliative here

without concluding that the system or speaker should use "bro"
```

---

# Evidence and Retrieval

The target prototype should eventually support an evidence router.

Possible sources include:

```text
CURRENT INTERACTION

HUMAN CORRECTION

USER-PROVIDED SPEECH / TEXT

RELATIONSHIP HISTORY

REASONING HISTORY

DOMAIN SOURCES

GENRE CONVENTIONS

BASE-MODEL KNOWLEDGE

CURRENT PRIMARY SOURCES

OPTIONAL WEB / RETRIEVAL

LINGUISTIC / CULTURAL SOURCES
```

Evidence should remain source-aware.

The architecture should not collapse:

```text
the human said X
```

with:

```text
the model inferred X
```

or:

```text
a source says X
```

---

# Optional Retrieval

Retrieval should be used only when it materially improves:

- factual accuracy;
- disciplinary support;
- rhetorical credibility;
- genre fit;
- audience fit;
- linguistic interpretation;
- or final wording.

The system should be capable of decisions such as:

```text
NO RETRIEVAL

VERIFY ONE FACT

CHECK CURRENT TERMINOLOGY

FIND ONE PRIMARY SOURCE

CHECK GENRE CONVENTION

CHECK CURRENT CULTURAL / IDIOMATIC USE

BROAD RESEARCH REQUIRED
```

Retrieval should be query-bounded rather than exploratory by default.

---

# Current Code Structure

The current prototype includes:

```text
state.py
```

Minimal active cognitive state and provenance representation.

```text
controller.py
```

Transparent rule-based next-move policy.

```text
realizer.py
```

Separates move selection from surface realization.

```text
updater.py
```

Explicit state update after human response.

```text
extractor.py
```

Defines the natural-language-to-state extraction contract.

```text
confirmation.py
```

Prevents system-inferred state from becoming human-confirmed state without review.

```text
cli.py
```

Runnable multi-turn control-core demonstration.

```text
composition.py
```

Early composition-contract scaffold.

The current composition module is not the final Rhetorical Compiler.

It exists to establish an explicit handoff between deliberation and composition.

---

# Current Tests

The test suite protects several architectural invariants.

Examples include:

```text
explicit human content remains human-originated

observed content is not mislabeled as system inference

system-inferred state requires confirmation

rejected system inference does not enter active state

system-triggered human cognition may remain human-originated

WITHHOLD remains a valid action

explicit composition request is respected

move selection remains separate from realization
```

Run:

```bash
pytest -v
```

from the `prototype` directory.

---

# Running the Current Prototype

From the `prototype` directory:

```bash
python cli.py
```

The current CLI asks the human to expose or classify some internal state manually.

This is **not the intended final user experience**.

It is an instrumentation interface for observing the controller before model-based state inference is introduced.

---

# Current UX Is Not the Product UX

A mature Deliberation Room should not require normal users to answer questions such as:

```text
"Conceptual stability: low, moderate, or high?"
```

or manually classify:

```text
"I just generated a distinction."
```

Those controls currently exist because the prototype is testing state transitions explicitly.

A future AI-backed system should infer candidate state from natural language and then expose only uncertainty or high-impact interpretations for correction when necessary.

---

# Next AI-Backed Prototype

The next major implementation phase should introduce model-backed components behind explicit interfaces.

Conceptually:

```text
NATURAL LANGUAGE
        ↓
MODEL-ASSISTED STATE EXTRACTION
        ↓
CONFIRMATION GATE WHEN NEEDED
        ↓
METACOGNITIVE CONTROLLER
        ↓
MODEL-ASSISTED MOVE REALIZATION
        ↓
HUMAN RESPONSE
        ↓
STATE-CHANGE INFERENCE
        ↺
```

and, after composition transition:

```text
HUMAN JUDGMENT
        ↓
EVIDENCE ROUTER
        ↓
RHETORICAL SITUATION MODEL
        ↓
SOCIOLINGUISTIC / IDIOLECT MODEL
        ↓
GENRE / DISCIPLINARY MODEL
        ↓
RHETORICAL COMPILER
        ↓
SEMANTIC / INTERACTIONAL DRIFT CHECK
        ↓
EXACT FINAL ARTIFACT
```

---

# AI Model Role

A future implementation may use one or more AI models for:

```text
state extraction

metacognitive operation inference

candidate move generation

candidate move ranking

linguistic analysis

speech/text feature abstraction

retrieval-query generation

genre analysis

rhetorical planning

artifact generation

semantic drift checking

interactional drift checking

provenance alignment
```

The architecture does not require every function to use the same model.

Some functions may eventually be suitable for:

```text
small local models

rule-based components

embedding models

specialized classifiers

retrieval systems

frontier generative models
```

This decomposition is intentional.

---

# Local / On-Device Hypothesis

A research hypothesis of Deliberation Room is that some controller and personalization functions may not require unrestricted frontier-model generation.

Candidate local functions include:

```text
idiolect feature extraction

recent-state summarization

operation classification

provenance matching

semantic similarity

language-feature extraction

reasoning-history updates
```

Whether these functions can perform adequately on smaller or local models is an empirical question.

---

# Final Target

The final experience should eventually feel simple.

A person should be able to say:

> "Help me figure out what I actually mean and then tell me exactly what to say."

The complexity should remain primarily behind the interface.

Internally, the system may be modeling:

```text
cognition
metacognition
rhetoric
language
culture
genre
evidence
audience
interaction
provenance
```

Externally, the human should experience:

```text
a small number of unusually useful questions
        ↓
recognition
        ↓
clearer judgment
        ↓
the exact artifact they actually needed
```

The target is not maximum visible machinery.

It is:

> **maximum precision with minimum necessary intervention.**

---

# Prototype Status

The current code should therefore be interpreted as:

```text
EXECUTABLE CONTROL-CORE SCAFFOLD
```

not:

```text
COMPLETE DELIBERATION ROOM IMPLEMENTATION
```

Its purpose is to make the architecture testable one component at a time.

The specification deliberately remains ahead of the executable prototype.
