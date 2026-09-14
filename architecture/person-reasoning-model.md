# Person / Reasoning Model

The Person / Reasoning Model represents recurring, interaction-relevant evidence about how this human appears to reason productively.

Its purpose is to improve elicitation.

It is not intended to become a covert personality profile, demographic classifier, psychological diagnosis, or fixed theory of the person.

The central question is:

> **How does this human productively think?**

---

## Why this model exists

Two people can hold similar knowledge and face the same conceptual problem while responding very differently to the same intervention.

One person may make progress through:

- direct counterexample;
- abstraction;
- analogy;
- explicit structure;
- adversarial testing;
- comparison;
- concrete cases;
- visual or spatial representation;
- narrative;
- procedural decomposition;
- or reflective paraphrase.

Another may find the same move unhelpful.

A system concerned with cognition preservation therefore needs more than a representation of **what the human currently thinks**.

It also needs a provisional representation of **which kinds of cognitive moves appear to help this human continue thinking for themselves**.

---

## Distinction from the Cognitive State Model

The Cognitive State Model asks:

> **What does the human currently appear to understand?**

The Person / Reasoning Model asks:

> **What patterns currently appear relevant to how this human productively operates on ideas?**

For example:

```text
COGNITIVE STATE
The current claim depends on an untested causal assumption.

PERSON / REASONING
This human has repeatedly clarified causal claims more effectively
through concrete comparison than through abstract definition.
```

The first represents the state of the problem.

The second may influence the form of the next move.

---

## Candidate Dimensions

Possible representations include:

- domain expertise;
- prior knowledge;
- conceptual vocabulary;
- abstraction tolerance;
- preferred level of specificity;
- analogical habits;
- preference for concrete examples;
- preference for categorical distinctions;
- preference for relational or spatial models;
- narrative reasoning;
- procedural reasoning;
- response to counterexamples;
- response to contradiction;
- response to direct challenge;
- response to tentative hypotheses;
- preferred degree of scaffolding;
- preferred pacing;
- tendency to externalize reasoning;
- need for intermediate synthesis;
- productive question types;
- recurring reasoning shortcuts;
- previously established conceptual structures;
- tolerance for ambiguity;
- patterns of revision;
- patterns of evidence use;
- patterns of uncertainty representation.

These are candidate state features, not stable human traits by default.

---

## Behavior Before Category

The architecture should prefer direct interaction evidence over unnecessary identity explanation.

Prefer:

```text
The user has repeatedly responded productively to concrete counterexamples
when testing general claims.
```

over:

```text
The user is a concrete thinker.
```

Prefer:

```text
In this domain, analogies have repeatedly helped the user identify
structural relationships.
```

over:

```text
The user is an analogical learner.
```

Prefer:

```text
The user requested less scaffolding after demonstrating independent control
of the distinction.
```

over:

```text
The user is advanced.
```

The first form remains grounded, contextual, and revisable.

The second risks converting interaction evidence into a fixed person-category.

---

## Context Matters

A productive reasoning pattern may be specific to:

- domain;
- task;
- stakes;
- emotional context;
- familiarity with the material;
- interaction partner;
- current cognitive load;
- or stage of deliberation.

For example:

```text
counterexample
```

may be productive during argument testing but less useful during initial idea generation.

Likewise:

```text
analogy
```

may be useful for exploration while becoming misleading during final stabilization.

The model should therefore preserve context.

A more precise representation is:

```yaml
observed_pattern:
  strategy: counterexample
  effect: productive
  context:
    domain: argument evaluation
    stage: testing
  confidence: high
  generalizability: unknown
```

rather than:

```yaml
user_type: counterexample_thinker
```

---

## Task-Level Before Trait-Level

The architecture should begin with the narrowest supported claim.

For example:

> "Counterexamples were productive in this deliberation."

is better supported than:

> "Counterexamples are generally productive for this person."

And that is better supported than:

> "This person is a counterexample thinker."

Generalization should require repeated evidence across relevant contexts.

Even then, the representation should remain corrigible.

---

## Productive Reasoning Patterns

A productive reasoning pattern is an observed relationship between an intervention or representational form and a useful cognitive outcome.

Examples:

```text
MOVE
Concrete comparison

OBSERVED OUTCOME
Human generated a previously missing distinction.
```

```text
MOVE
Direct contradiction

OBSERVED OUTCOME
Human became defensive and repeated the original claim without
engaging the contradiction.
```

```text
MOVE
Tentative paraphrase

OBSERVED OUTCOME
Human corrected one phrase and thereby clarified the conceptual
difference that mattered.
```

```text
MOVE
Analogy

OBSERVED OUTCOME
Human mapped the structure successfully to a new case.
```

The goal is not to maximize user preference alone.

A preferred intervention may not be cognitively productive.

Likewise, a slightly uncomfortable intervention may still be valuable if it preserves agency and supports real reasoning.

The model should therefore distinguish:

```text
LIKED
```

from:

```text
PRODUCTIVE
```

when possible.

---

## Preferred Challenge Modes

Challenge can be realized in multiple ways.

For example:

### Direct challenge

> "That claim contradicts what you said earlier."

### Tentative challenge

> "I think those two claims may be pulling in different directions. Do they feel different to you?"

### Counterexample

> "Would your rule still hold in this case?"

### Role reversal

> "What would someone who disagreed with you say is missing?"

### Boundary test

> "Where would you stop applying that rule?"

### Evidence test

> "What would count as evidence against this interpretation?"

The Person / Reasoning Model may track which challenge forms have previously produced:

- deeper reasoning;
- defensive repetition;
- productive uncertainty;
- meaningful revision;
- disengagement;
- or independent counterargument.

This information can inform future next-move selection.

---

## Representation Preferences

Humans may reason more effectively when a problem is represented in a particular form.

Candidate representation modes include:

- verbal;
- spatial;
- relational;
- comparative;
- chronological;
- hierarchical;
- causal;
- tabular;
- narrative;
- analogical;
- procedural;
- visual;
- categorical.

For example, a user may struggle with:

> "What are the major tensions in this problem?"

but immediately engage when represented as:

```text
VALUE A
    ↘
     CONFLICT
    ↗
VALUE B
```

This should not be reduced to simplistic "learning style" classification.

The relevant evidence is whether a representation **actually supported reasoning in the observed interaction**.

---

## Expertise and Prior Knowledge

The model may represent task-relevant expertise.

For example:

```yaml
domain_knowledge:
  rhetoric:
    level: advanced
    source: repeated_observation
    confidence: high

  machine_learning:
    level: developing
    source: current_interaction
    confidence: medium
```

Expertise should influence next-move selection.

An expert may benefit from:

- compressed language;
- disciplinary terminology;
- higher-level counterexamples;
- fewer explanatory steps;
- more direct challenge.

A novice may benefit from:

- concrete examples;
- intermediate distinctions;
- explicit definitions;
- additional representation support.

The architecture should not assume that expertise is global.

Someone may be highly expert in one domain and novice in another.

---

## Prior Conceptual Structures

The system may also represent conceptual frameworks the human already uses productively.

Examples:

```text
"productive friction"
"response latitude"
"artifact versus cognition"
"authority versus judgment"
```

If the user has demonstrated stable understanding of a framework, later reasoning may legitimately build on it.

However, the architecture should preserve whether the concept was:

- human-originated;
- system-proposed;
- jointly developed;
- or externally sourced.

Previously available vocabulary should not erase provenance.

---

## Correction of the Person Model

The human must be able to reject the system's model of how they think.

For example:

> "I don't actually like analogies generally. That one just happened to work."

> "I only want direct challenge when I'm testing an argument, not when I'm brainstorming."

> "Don't simplify the terminology for me."

> "I know this part already."

> "The questions are slowing me down now."

These are not merely preference statements.

They are evidence about the boundaries of the Person / Reasoning Model.

The architecture should update accordingly.

---

## Metacognitive Feedback

The Person / Reasoning Model may eventually support explicit metacognitive feedback.

This feedback should describe observed patterns rather than declare fixed cognitive types.

For example:

> "You revised four of your five major claims after encountering a counterexample."

> "You generated claims independently, while most of the system's useful interventions involved asking for warrants."

> "Your strongest distinctions emerged when you compared two concrete cases."

> "You became more precise after rejecting system paraphrases than after answering broad questions."

> "You preserved uncertainty rather than forcing closure in two places."

This can help the human inspect their own reasoning process.

---

## Metacognitive Feedback Is Also a Proposal

A metacognitive observation is itself an inference.

Therefore it should obey the same governing principle as other system interpretations:

> **The system may propose. The human must recognize.**

For example:

```text
SYSTEM
"Counterexamples seemed especially productive for you here."

HUMAN
"Only because this was an argument problem."

UPDATE
Counterexample effectiveness:
  supported in argument testing
  broader generalization rejected
```

The human's response improves the model.

Metacognition therefore becomes another deliberative loop rather than a one-way diagnostic report.

---

## Candidate Metacognitive Signals

Future implementations might derive patterns such as:

### Revision behavior

- number of substantive revisions;
- triggers associated with revision;
- degree of revision;
- whether revision originated independently or after system challenge.

### Claim generation

- human-originated claims;
- system-proposed claims;
- jointly developed claims;
- claims retained after testing.

### Distinction generation

- human-originated distinctions;
- system-proposed distinctions;
- distinctions revised by the human;
- distinctions generalized to new cases.

### Evidence behavior

- evidence introduced independently;
- evidence requested by the system;
- counterevidence considered;
- evidence rejected as irrelevant;
- warrant gaps identified.

### Uncertainty behavior

- uncertainty introduced by human;
- uncertainty surfaced by system;
- uncertainty retained through composition;
- uncertainty prematurely collapsed.

### Question behavior

- questions generated by the human;
- clarifying questions;
- causal questions;
- boundary questions;
- counterexample questions;
- questions that materially changed the model.

These are candidate signals, not validated measures.

---

## Questions Answered by the Human

The architecture may also track which cognitive questions were actually resolved by the human rather than merely answered by the system.

For example:

```text
QUESTION:
What distinguishes X from Y?

SOURCE:
System elicitation

RESOLUTION:
Human-originated distinction

STATUS:
Stabilized
```

or:

```text
QUESTION:
What evidence supports the causal claim?

SOURCE:
System elicitation

RESOLUTION:
System supplied evidence

HUMAN UPTAKE:
Unresolved
```

Those outcomes are different.

This distinction can contribute to both metacognitive feedback and cognitive provenance.

---

## Human / System Contribution

The Person / Reasoning Model should not reduce intellectual contribution to a binary "AI versus human" measure.

Possible events include:

```text
HUMAN-ORIGINATED
SYSTEM-PROPOSED → HUMAN-RECOGNIZED
SYSTEM-PROPOSED → HUMAN-REVISED
SYSTEM-PROPOSED → HUMAN-REJECTED
JOINTLY-DEVELOPED
SYSTEM-SUPPLIED / HUMAN-UPTAKE-UNRESOLVED
```

Repeated patterns across these events may support useful feedback.

For example:

> "Most final claims began with your own language, while the system contributed primarily through counterexamples."

or:

> "The system proposed several initial distinctions, but you materially revised most of them before they entered the final model."

This is more informative than saying:

> "Your work was 73% human."

---

## Quantification and False Precision

The architecture may eventually support quantitative summaries.

Examples might include:

```text
Questions substantively resolved by human: 12

Human-originated distinctions: 5

System-proposed distinctions:
  recognized: 2
  revised: 3
  rejected: 4

Human revisions after challenge: 6

Uncertainties intentionally retained: 2
```

However, percentages should be treated cautiously.

Semantic contribution is not equivalent to token contribution.

A human may originate an idea that a system later expresses almost entirely in different wording.

Likewise, a human may repeat AI wording without demonstrating understanding.

Future quantitative measures therefore need validation before being interpreted as authorship scores.

---

## Conceptual Versus Linguistic Contribution

The architecture should distinguish at least:

### Conceptual contribution

Who introduced, distinguished, tested, revised, or stabilized the idea?

### Linguistic contribution

Who supplied the wording used to express that idea?

Example:

```text
HUMAN
"I don't care if we do equal amounts. I care whether we're both
noticing each other."

SYSTEM COMPOSITION
"The issue is not strict reciprocity but mutual attentiveness."
```

The final language is system-generated.

The substantive distinction may remain human-originated.

The model should preserve both facts.

---

## A Possible Representation

```yaml
person_reasoning_model:
  observed_patterns:

    - strategy: counterexample
      context:
        domain: argument evaluation
        stage: testing
      observed_effect:
        type: substantive_revision
        count: 4
      confidence: high
      generalizability: unknown

    - strategy: analogy
      context:
        stage: exploration
      observed_effect:
        type: distinction_generation
        count: 3
      confidence: medium
      generalizability: unknown

  representation_preferences:
    - type: relational
      evidence_count: 5
      confidence: high

  challenge_preferences:
    - type: direct
      context: conceptual_testing
      productive: true

    - type: direct
      context: early_brainstorming
      productive: unknown

  domain_expertise:
    - domain: rhetoric
      level: advanced
      confidence: high

  metacognitive_observations:
    - content: "Counterexamples were productive during argument testing."
      source: SYSTEM-INFERRED
      status: USER-CONFIRMED

    - content: "Analogy is generally the user's preferred reasoning mode."
      source: SYSTEM-INFERRED
      status: USER-REJECTED
```

This schema is illustrative rather than final.

---

## Persistence

Not every observed pattern should become persistent personalization.

Possible categories include:

```text
TURN-LEVEL
SESSION-LEVEL
TASK-LEVEL
DOMAIN-LEVEL
CROSS-DOMAIN
PERSISTENT
```

A pattern should earn broader persistence through evidence.

For example:

```text
Observed once
→ task-level hypothesis

Observed repeatedly in same domain
→ domain-level hypothesis

Observed across domains
→ possible broader representation

Human confirms broader pattern
→ stronger candidate for persistence
```

This minimizes overgeneralization and unnecessary personal-data retention.

---

## Failure Modes

The Person / Reasoning Model can fail in several ways.

### Reification

A provisional pattern becomes treated as a permanent trait.

### Overgeneralization

A strategy useful in one task is applied everywhere.

### Preference substitution

The system optimizes for what the user likes rather than what supports useful cognition.

### Identity inference

The system explains reasoning behavior through demographic or psychological categories without need.

### Self-fulfilling personalization

The system repeatedly offers one kind of intervention because it believes the user prefers it, preventing evidence that another strategy might work better.

### Excessive accommodation

The system adapts so thoroughly to established patterns that it stops exposing the human to productive new forms of reasoning.

### Hidden profiling

A broad behavioral profile accumulates without being necessary, visible, or correctable.

These are architectural risks, not merely implementation bugs.

---

## Exploration Versus Exploitation

Personalization creates a classic tension.

If the system always uses the intervention currently believed to be most productive, it may never discover that other interventions could work better.

Therefore the next-move policy may need to balance:

```text
EXPLOIT
Use a currently supported productive reasoning strategy.

EXPLORE
Occasionally test another plausible strategy when interactional risk is low.
```

Exploration should not turn the human into an experimental subject without regard for stakes or context.

But some limited exploration may be necessary to prevent personalization from becoming a self-reinforcing loop.

---

## Relationship to the Next-Move Policy

The Person / Reasoning Model does not choose the intervention by itself.

It contributes evidence.

For example:

```text
COGNITIVE STATE
Claim contains an untested generalization.

PERSON / REASONING MODEL
Concrete counterexamples have been productive in comparable tasks.

LINGUISTIC / SOCIOLINGUISTIC MODEL
Direct contradiction is interpreted as playful rather than hostile
in the current register.

INTERACTION MODEL
Low stakes; strong permission for challenge.

NEXT MOVE
Counterexample realized through direct, concise challenge.
```

A different interaction state may produce a different move even with the same person.

---

## Relationship to Metacognitive Agency

The long-term goal is not merely to make the system better at adapting to the human.

It is also to make the human better able to inspect and control that adaptation.

A mature implementation might allow a user to see:

```text
The system currently believes:
- direct counterexamples are often productive for you in argument testing;
- you usually prefer high abstraction in rhetoric tasks;
- analogies have been useful during exploration but less useful during stabilization.
```

The user could then:

```text
CONFIRM
REVISE
LIMIT TO CONTEXT
MARK AS TEMPORARY
DELETE
```

This turns personalization into a negotiated model rather than invisible profiling.

---

## What This Model Must Not Do

The Person / Reasoning Model should not:

- diagnose personality;
- infer intelligence globally;
- infer identity unnecessarily;
- assign fixed "learning styles";
- turn temporary behavior into permanent traits;
- optimize solely for comfort;
- optimize solely for engagement;
- treat preference as equivalent to productivity;
- hide its important persistent assumptions from the human;
- or become impossible for the human to correct.

---

## Research Questions

Key open questions include:

1. Which reasoning patterns can be inferred reliably from interaction?
2. How many observations justify generalization beyond a task?
3. How should context be represented when storing a productive reasoning pattern?
4. Can users meaningfully inspect and correct these representations?
5. Which observed patterns genuinely improve next-move selection?
6. When should personalization deliberately try a less familiar reasoning move?
7. How can the architecture distinguish preference from cognitive productivity?
8. Can metacognitive feedback improve future independent reasoning?
9. What kinds of metacognitive feedback cause harmful over-identification with a "thinking type"?
10. Which parts of the Person / Reasoning Model should persist across sessions?
11. Can useful personalization be achieved while storing substantially less raw conversation history?
12. How should the system represent conflicting evidence about a person's reasoning patterns?
13. How should conceptual and linguistic contribution be reported without creating false authorship precision?
