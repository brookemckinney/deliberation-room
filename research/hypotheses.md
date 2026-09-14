# Research Hypotheses

Deliberation Room is currently a conceptual interaction architecture and research program.

The claims in this repository should not be treated as established merely because the architecture makes them plausible.

This document identifies the primary hypotheses the project is intended to test.

Each hypothesis should be capable of being weakened, revised, or rejected by evidence.

---

## H1 — Cognition-Preserving Interaction

> **Constrained next-move selection can preserve more human cognitive responsibility than unrestricted generative assistance.**

The central claim of Deliberation Room is not that less generation is always better.

It is that an architecture which explicitly selects cognition-preserving moves may produce different cognitive outcomes from a system that defaults to unrestricted generation.

### Prediction

Compared with unrestricted generative assistance, users interacting with a cognition-preserving next-move controller may demonstrate stronger:

- independent explanation;
- reconstruction of reasoning;
- transfer to new cases;
- response to counterexamples;
- ability to distinguish assumptions from evidence;
- awareness of uncertainty;
- revision quality;
- retention of conceptual distinctions;
- and ability to identify which ideas originated with themselves versus the system.

### Important qualification

Better final artifacts would not by themselves support H1.

The relevant outcome is **human cognition**, not only artifact quality.

---

## H2 — Adaptive Elicitation

> **State-adaptive elicitation can outperform generic Socratic questioning for relevant deliberative tasks.**

Generic Socratic systems often rely on broadly useful moves such as:

```text
Why do you think that?

What evidence supports that?

What is another perspective?

How could you revise your answer?
```

These may be valuable.

Deliberation Room proposes that question quality can improve when move selection depends on a structured representation of:

```text
Cognitive State
+
Person / Reasoning Model
+
Linguistic / Sociolinguistic Model
+
Interaction Model
```

### Prediction

State-adaptive interaction may produce:

- fewer redundant questions;
- greater information gain per intervention;
- more human-originated distinctions;
- fewer system-supplied conclusions;
- better calibrated challenge;
- faster detection of misunderstandings;
- greater response latitude;
- and fewer interactions in which the human satisfies the questioning pattern without meaningfully revising the model.

### Possible comparison conditions

```text
1. Unrestricted generative assistant

2. Generic Socratic prompting

3. Cognitive-state-only controller

4. Cognitive state + person/reasoning adaptation

5. Full four-model Deliberation Room controller
```

This hypothesis should be tested rather than inferred from architectural complexity.

---

## H3 — Joint Move Selection

> **Selecting cognitive function, linguistic realization, and interactional affordance jointly may outperform architectures that select a cognitive operation first and style it afterward.**

A conventional architecture might operate as:

```text
select cognitive action
        ↓
generate wording
        ↓
apply style / safety / tone
```

Deliberation Room proposes that this separation may sometimes be inadequate because linguistic realization can change the effective cognitive and social function of a move.

### Prediction

Jointly modeled moves may produce better outcomes on:

- perceived permission to disagree;
- response latitude;
- willingness to revise;
- face preservation;
- pragmatic interpretation;
- cognitive accessibility;
- social appropriateness;
- and continued independent reasoning.

### Example

These may all nominally instantiate `CHALLENGE`:

```text
"What evidence supports that conclusion?"

"Wait — does that still work if the opposite is true?"

"Okay, try to break your own rule."
```

But they need not be cognitively or interactionally equivalent.

---

## H4 — Sociolinguistically Informed Move Selection

> **Sociolinguistic information can improve action selection when used as evidence about interaction rather than merely as post-generation style adaptation.**

The linguistic/sociolinguistic model is not intended merely to make outputs sound more like the user.

It represents how meaning operates in the discourse environment.

### Prediction

Compared with systems that perform semantic reasoning first and tone adaptation afterward, sociolinguistically informed action selection may improve:

- interpretation of stance;
- recognition of irony;
- interpretation of mitigation;
- local semantic understanding;
- repair handling;
- register selection;
- humor calibration;
- relational fit;
- and identification of when a form should be understood but not reproduced.

### Failure evidence

H4 would be weakened if equivalent outcomes can be achieved without explicit sociolinguistic state or if the state introduces more stereotyping and misclassification than useful interactional information.

---

## H5 — High-Information / Low-Intrusion Elicitation

> **A policy that explicitly optimizes for useful information gain while minimizing unnecessary disclosure can support effective personalization with less personal-data acquisition.**

Many conversational systems improve personalization by accumulating broad interaction history.

Deliberation Room proposes a narrower target:

> **Acquire the smallest amount of information likely to materially change the next move.**

### Prediction

A high-information / low-intrusion policy may achieve comparable or better deliberative performance while requiring:

- fewer personal questions;
- less biography;
- fewer identity inferences;
- less raw conversational history;
- and lower disclosure burden.

### Possible measures

- questions asked before useful state resolution;
- disclosure quantity;
- sensitivity of disclosed information;
- model accuracy;
- user correction frequency;
- next-move quality;
- task success.

---

## H6 — Constrained-Model Feasibility

> **The narrower task of next-move selection may permit useful performance using substantially smaller models than unrestricted general-purpose generation.**

This is a central implementation and privacy hypothesis.

Deliberation Room does **not** currently claim that small or local models are sufficient.

The hypothesis is that they may be sufficient because the task is constrained.

Instead of producing arbitrary open-ended output, portions of the system may need to:

- classify current state;
- generate a small candidate move set;
- rank moves;
- estimate uncertainty;
- detect contradiction;
- select whether to ask, challenge, reflect, or withhold;
- and update structured representations.

### Possible architectures

```text
SMALL LOCAL CONTROLLER
+
OPTIONAL LARGE COMPOSITION MODEL
```

or:

```text
LOCAL STATE TRACKING
+
LOCAL NEXT-MOVE RANKING
+
REMOTE GENERATION ONLY WHEN NEEDED
```

or:

```text
SMALL LANGUAGE MODEL
+
RULE / CLASSIFIER HYBRID
+
STRUCTURED STATE
```

### Prediction

Useful controller performance may remain acceptable at smaller model sizes even if open-ended composition quality declines.

### Measures

- expert agreement on move selection;
- cognitive outcome;
- model size;
- memory requirement;
- latency;
- energy use;
- local-device feasibility;
- privacy exposure;
- and intervention quality.

---

## H7 — Data-Minimized Personalization

> **Abstracted interaction-state representations may support useful personalization while reducing reliance on raw conversational history.**

For example, a controller may benefit from retaining:

```text
counterexamples productive in argument testing
high abstraction tolerance in rhetoric tasks
current claim confidence: moderate
unresolved issue: causal warrant
shared local term: "walking the orb"
```

without retaining every conversation from which those patterns emerged.

### Prediction

Structured state may preserve enough personalization value to support useful next-move selection with:

- less raw text retention;
- less sensitive contextual exposure;
- more inspectable personalization;
- easier correction;
- easier deletion;
- and more targeted persistence.

### Comparison conditions

```text
FULL RAW HISTORY

SUMMARIZED HISTORY

STRUCTURED STATE ONLY

EPHEMERAL SESSION STATE

NO PERSONALIZATION
```

### Important qualification

Abstracted state is still personal data.

It may sometimes be more sensitive than the source conversation.

H7 concerns **data minimization**, not elimination of privacy risk.

---

## H8 — Corrigible Personalization

> **Personalization becomes safer and more accurate when humans can inspect and correct important persistent representations about how they reason and communicate.**

Current personalization systems can make hidden assumptions difficult to contest.

Deliberation Room proposes a negotiated model.

A human might be shown:

```text
The system currently believes:

- direct counterexamples are often productive for you in argument testing;
- you usually prefer high abstraction in rhetoric tasks;
- analogy has been useful during exploration but less useful during stabilization.
```

The human could:

```text
CONFIRM
REVISE
LIMIT TO CONTEXT
MARK TEMPORARY
DELETE
```

### Prediction

Corrigibility may reduce:

- overgeneralization;
- personalization lock-in;
- identity misclassification;
- inappropriate strategy transfer;
- and long-term model drift.

It may also improve trust calibration.

---

## H9 — Cognitive Provenance

> **Structured traces of reasoning development may provide more meaningful evidence of intellectual accountability than token-level provenance alone.**

Token provenance can answer:

> Who generated these words?

It cannot fully answer:

> Who developed the judgment represented by them?

### Prediction

A cognitive provenance trace may better predict whether a human can:

- explain a claim;
- reconstruct how it changed;
- identify relevant evidence;
- respond to a new counterexample;
- distinguish system proposals from their own reasoning;
- and transfer the concept to a novel case.

### Candidate trace events

```text
human-originated claim
human-originated distinction
system proposal
human recognition
human rejection
human revision
counterexample
warrant articulation
uncertainty retained
stabilized judgment
composition transition
```

---

## H10 — Conceptual and Linguistic Provenance Are Distinct

> **Separating conceptual provenance from linguistic provenance produces more accurate descriptions of human-system contribution than treating final wording as a proxy for idea ownership.**

Example:

```text
HUMAN CONCEPT

"I don't care if we do equal amounts.
I care whether we're both noticing each other."

SYSTEM COMPOSITION

"The issue is not strict reciprocity but mutual attentiveness."
```

Possible classification:

```text
conceptual provenance:
HUMAN-ORIGINATED

linguistic provenance:
SYSTEM-TRANSPOSED
```

### Prediction

Independent coding of conceptual and linguistic contribution may explain human understanding better than:

- token counts;
- percentage AI wording;
- edit distance;
- or AI-detection labels.

---

## H11 — Recognition Is More Informative Than Acceptance

> **Evidence that a human has recognized, revised, applied, or challenged a system proposal is more informative about cognitive uptake than simple agreement.**

Compare:

```text
SYSTEM
"The distinction may be authority versus infallibility."

HUMAN
"Yes."
```

with:

```text
SYSTEM
"The distinction may be authority versus infallibility."

HUMAN
"Sort of. It's not that he thinks he's literally infallible.
It's that disagreement becomes evidence of disloyalty."
```

The second response provides substantially stronger evidence of cognitive uptake.

### Prediction

Recognition measures based on:

- restatement;
- application;
- qualification;
- counterexample;
- extension;
- or revision

may correlate more strongly with independent reasoning than binary acceptance.

---

## H12 — Rejection Is Productive Evidence

> **Human rejection of system interpretations can provide high-value information for state updating and future move selection.**

Current systems often treat rejection as failed output.

Deliberation Room treats repair as evidence.

Examples include:

```text
"That's not what I mean."

"Those are actually the same thing to me."

"That's technically correct but too strong."

"The idea is right; the wording is wrong."

"I understand that already. That's not where I'm stuck."
```

### Prediction

Explicitly modeling the reason for rejection may reduce repeated misinterpretation and improve later move selection.

---

## H13 — Metacognitive Feedback

> **Deliberation traces can support useful metacognitive feedback about how reasoning developed during a task.**

Examples might include:

> "Most of your substantive revisions followed counterexamples."

> "You generated claims independently but needed more elicitation around warrants."

> "You rejected more system interpretations than you accepted."

> "Concrete comparison preceded three major distinctions."

### Prediction

Trace-derived metacognitive feedback may improve:

- future strategy selection;
- self-monitoring;
- independent revision;
- uncertainty calibration;
- transfer;
- and awareness of where AI assistance entered the process.

---

## H14 — Task-Level Metacognitive Description Is Safer Than Cognitive Typing

> **Describing observed reasoning patterns within a task may be more accurate and less reductive than assigning stable cognitive types.**

Prefer:

```text
"Counterexamples were productive in this deliberation."
```

over:

```text
"You are a counterexample thinker."
```

### Prediction

Context-bounded feedback may produce fewer erroneous generalizations and may be easier for humans to correct.

This hypothesis also applies to the Person / Reasoning Model more broadly.

---

## H15 — Composition Gating

> **Separating deliberation from composition may produce artifacts whose substantive judgments are more explainable by the human than artifacts generated during unresolved reasoning.**

A conventional assistant can transform an unstable idea into polished prose immediately.

Deliberation Room introduces an explicit transition:

```text
DELIBERATION
     ↓
STABILIZED HUMAN JUDGMENT
     ↓
OPTIONAL COMPOSITION
```

### Prediction

Composition after stabilization may improve:

- explanation of claims;
- semantic consistency;
- uncertainty preservation;
- provenance clarity;
- and resistance to semantic drift.

### Important qualification

This hypothesis does not imply that every task requires prolonged deliberation.

---

## H16 — Composition Can Reveal Instability

> **Composition itself can function as a diagnostic representation that reveals unresolved cognition and appropriately returns the interaction to deliberation.**

For example:

> "Seeing it written that way, I don't actually believe the second part."

This should not be treated merely as copy-edit feedback.

It may reveal that the underlying model was not stable.

### Prediction

Allowing composition to return to deliberation may reduce semantic drift and false stabilization.

---

## H17 — Cognitive Provenance Can Support Education Better Than AI Detection Alone

> **In educational contexts, evidence of reasoning development may be more instructionally useful than attempts to classify an artifact as AI-generated or human-generated.**

Possible instructor questions include:

> Why is this claim here?

> What changed after this counterexample?

> Which system proposal did you reject?

> Apply this distinction to a new case.

> What uncertainty did you preserve?

### Prediction

Provenance-aware assessment may provide better evidence of:

- understanding;
- transfer;
- conceptual revision;
- evidence use;
- and intellectual accountability

than AI-detection labels alone.

---

## H18 — Domain-Specific Deliberation Policies

> **A general cognition-preserving controller can be improved by domain-specific definitions of responsible deliberation.**

The general control loop may remain:

```text
notice
→ model
→ test
→ revise
→ stabilize
→ express
```

while the relevant epistemic objects vary.

For example:

### Literature

```text
textual evidence
ambiguity
interpretation
counterreading
form
```

### History

```text
source
perspective
causation
chronology
contingency
```

### Science

```text
observation
hypothesis
mechanism
evidence
confound
falsification
```

### Design

```text
stakeholder
constraint
tradeoff
iteration
consequence
```

### Ethics

```text
stakeholders
values
duties
consequences
competing principles
```

### Prediction

Domain-sensitive policy may improve both cognitive relevance and evaluation validity compared with one generic questioning strategy.

---

# Cross-Hypothesis Evaluation Principle

Several hypotheses could appear supported if evaluation relies only on:

```text
user preference
artifact quality
conversation length
task completion
```

Those outcomes are insufficient.

Evaluation should separately consider:

```text
COGNITIVE OUTCOME
INTERACTION QUALITY
ARTIFACT QUALITY
AGENCY
PROVENANCE
PRIVACY
MODEL COST
```

The architecture may improve one while worsening another.

Those tradeoffs should remain visible.

---

# Falsification

A useful research program must permit the possibility that Deliberation Room is wrong.

Evidence against major parts of the architecture might include findings that:

- unrestricted generation produces equal or better cognitive outcomes;
- generic Socratic prompting performs as well as state-adaptive policy;
- the four-model representation adds complexity without meaningful benefit;
- sociolinguistic state increases stereotyping more than interaction quality;
- structured personalization performs substantially worse than raw-history personalization;
- small models cannot perform move selection adequately;
- conceptual provenance cannot be classified reliably;
- provenance traces fail to predict independent understanding;
- metacognitive feedback causes inaccurate cognitive self-labeling;
- composition gating creates friction without cognitive benefit;
- users circumvent the controller rather than reason through it;
- or the architecture produces more dependence rather than less.

Such results should alter the model.

---

# Research Stance

The architecture should maintain explicit distinctions among:

```text
ARCHITECTURAL COMMITMENT
WORKING HYPOTHESIS
IMPLEMENTATION PROPOSAL
EMPIRICAL FINDING
```

For example:

```text
ARCHITECTURAL COMMITMENT
Conceptual and linguistic provenance should be represented separately.

WORKING HYPOTHESIS
That separation predicts intellectual accountability better than token provenance.

IMPLEMENTATION PROPOSAL
Represent provenance at proposition level.

EMPIRICAL FINDING
Not yet established.
```

These categories should not be collapsed.

---

# Current Research Program

The core research program can be summarized as:

```text
HUMAN COGNITION
        ↓
Can AI support it without prematurely replacing it?

ADAPTIVE INTERACTION
        ↓
Can explicit next-move selection outperform generic generation
or generic questioning?

SITUATED MEANING
        ↓
Does modeling linguistic and interactional meaning improve
which cognitive move is selected?

PROVENANCE
        ↓
Can reasoning development be represented meaningfully without
reducing authorship to tokens?

METACOGNITION
        ↓
Can traces help humans understand how they reasoned?

PRIVACY
        ↓
Can useful personalization operate over less raw personal data?

MODEL SCALE
        ↓
Does the constrained controller permit useful local or
on-device inference?
```

The project is not complete when those questions sound plausible.

It becomes useful when they can be tested.
