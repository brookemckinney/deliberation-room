# Deliberation Room

**A cognition-preserving interaction architecture for AI systems.**

> **Status:** Research specification / conceptual architecture.  
> No validated implementation or empirical results yet.  
> Schemas, state representations, and policy mechanisms are provisional and intended to be tested.

Most conversational AI systems implicitly optimize a problem resembling:

> **What should the model say next?**

Deliberation Room proposes a different optimization target:

> **What should the human be able to do next?**

The architecture explores whether AI can support human reasoning without prematurely replacing that reasoning with generated conclusions, interpretations, or language.

Rather than treating generation as the default action, Deliberation Room models the current interaction, selects a next move, observes the human response, and updates its models.

```text
MODEL THE CURRENT STATE
        ↓
SELECT A NEXT MOVE
        ↓
HUMAN RESPONDS
        ↓
UPDATE THE MODELS
        ↺
```

Free-form answer or artifact generation is not the default objective of this loop. The system may still generate the linguistic realization of a selected move—for example, a clarification, challenge, reflection, or counterexample—but generation is subordinate to the next-move policy rather than serving as the policy itself.
---

## Conceptual Architecture

Deliberation Room combines four interacting models.

```text
┌─────────────────────────────────────────┐
│ 1. COGNITIVE STATE MODEL               │
│                                         │
│ What does the human currently appear   │
│ to understand?                          │
│                                         │
│ distinctions • assumptions • warrants  │
│ contradictions • uncertainty • gaps    │
│ evidence • conceptual stability        │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ 2. PERSON / REASONING MODEL            │
│                                         │
│ How does this human productively think? │
│                                         │
│ expertise • analogical habits          │
│ abstraction tolerance • preferred      │
│ challenge modes • prior knowledge      │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ 3. LINGUISTIC / SOCIOLINGUISTIC MODEL  │
│                                         │
│ How does meaning operate for this human │
│ in this discourse environment?         │
│                                         │
│ idiolect • register • dialect           │
│ discourse community • pragmatics       │
│ indexicality • stance • humor           │
│ role language • generational norms     │
│ code-switching • shared vocabulary     │
│ relational language history            │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ 4. INTERACTION MODEL                   │
│                                         │
│ What does a move DO here, between      │
│ THESE people, for THIS purpose?         │
│                                         │
│ power • status • familiarity • history │
│ face • belonging • audience • setting  │
│ stakes • relational distance           │
│ permissions • social risk              │
│ interactional expectations             │
└────────────────────┬────────────────────┘
                     │
              NEXT-MOVE POLICY
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
    clarify       challenge     counterexample
    distinguish   reflect       withhold
    reframe       test          ask
                     │
                     ↓
               HUMAN RESPONDS
                     │
                     ↓
              MODELS UPDATE ↺
```

The four models are analytically distinguishable but interactionally dependent.

A cognitive move cannot always be evaluated independently of the language through which it is realized, the social meaning of that language, the relationship between participants, or the human's established reasoning practices.

---
## Start Here

Deliberation Room is specified across several layers. Readers can enter the project according to what they want to inspect.

| If you want to understand... | Start with |
|---|---|
| The project's governing commitments | [Governing Principles](GOVERNING_PRINCIPLES.md) |
| The four interacting models | [Architecture](architecture/) |
| How the system chooses what to do next | [Next-Move Policy](architecture/next-move-policy.md) |
| How human and system contributions are distinguished | [Provenance](architecture/provenance.md) |
| The provisional state representations | [Schemas](schemas/) |
| Concrete interaction traces | [Examples](examples/) |
| The research claims to be tested | [Research Hypotheses](research/hypotheses.md) |
| How the architecture could be evaluated | [Evaluation](research/evaluation.md) |
| Privacy and misuse risks | [Threat Model](research/threat-model.md) |
| Relevant intellectual and technical precedents | [Related Work](research/related-work.md) |
| Educational applications | [Education](applications/education.md) |
| Deliberation before communication | [Communication](applications/communication.md) |
| Social and relational move selection | [Relational Interaction](applications/relational-interaction.md) |
| Project-specific terminology | [Glossary](GLOSSARY.md) |

### How the application files differ

The application documents are related but intentionally distinct:

- **Education** asks how AI can support learning without silently replacing the cognition an assessment is intended to develop or evidence.
- **Communication** asks how a human can stabilize what they mean before rhetorically transposing that judgment for an audience.
- **Relational Interaction** asks what a communicative move *does* within a particular relationship, role, power structure, discourse environment, and moment.

The architecture is not presented as empirically validated. The files above distinguish architectural commitments, implementation proposals, research hypotheses, and evaluation questions wherever possible.

---
## The Four Models

### 1. Cognitive State Model

**What does the human currently appear to understand?**

This model represents the current deliberative state, including:

- observations
- claims
- distinctions
- assumptions
- warrants
- evidence
- contradictions
- competing explanations
- uncertainty
- conceptual gaps
- unresolved questions
- conceptual stability

It does not claim direct access to cognition. It represents what the interaction currently provides evidence for.

### 2. Person / Reasoning Model

**How does this human productively think?**

This model represents interaction-relevant patterns such as:

- domain expertise
- prior knowledge
- analogical habits
- abstraction tolerance
- preferred challenge modes
- response to counterexamples
- preferred representations
- previously established distinctions

Its purpose is not demographic or personality classification.

Its purpose is to help select forms of elicitation that allow this particular human to reason productively.

### 3. Linguistic / Sociolinguistic Model

**How does meaning operate for this human in this discourse environment?**

This model represents features such as:

- idiolect
- register
- dialect
- discourse community
- pragmatics
- indexicality
- stance
- humor
- irony
- role language
- generational discourse norms
- code-switching
- professional or community-specific language
- shared vocabulary
- relational language history
- repair behavior

This is not a style-transfer layer applied after reasoning.

> **Sociolinguistic information is not a personalization layer applied after reasoning. It is part of the evidence required to reason about interaction in the first place.**

A phrase does not necessarily have a stable interactional meaning independent of speaker, recipient, discourse community, relationship history, register, and moment.

The architecture therefore distinguishes:

> **What does this language mean here?**

from:

> **What does using it do here?**

Understanding a linguistic convention also does not imply performing it. The objective is interactional competence, not surface mimicry.

### 4. Interaction Model

**What does a move do here, between these people, for this purpose?**

This model represents:

- role
- power
- status
- familiarity
- relationship history
- face
- belonging
- audience
- setting
- stakes
- relational distance
- interactional permissions
- social risk
- disclosure pressure
- response latitude
- interactional expectations

The same semantic content can perform very different social actions depending on who says it, to whom, where, and within what relationship.

Power, belonging, familiarity, and social risk are therefore not merely constraints checked after a response has been generated.

They are evidence relevant to deciding **which move should occur at all**.

---

## Next-Move Policy

The four models jointly inform a next-move policy.

Conceptually:

```text
CURRENT INTERACTION STATE
        │
        ├── Cognitive State
        ├── Person / Reasoning
        ├── Linguistic / Sociolinguistic
        └── Interaction
        │
        ↓
   NEXT-MOVE POLICY
        │
        ↓
  SELECT INTERVENTION
```

Candidate moves may include:

```text
ASK
CLARIFY
DISTINGUISH
REFLECT
CHALLENGE
COUNTEREXAMPLE
TEST
REFRAME
SURFACE_ASSUMPTION
SURFACE_CONTRADICTION
SURFACE_UNCERTAINTY
INVITE_PERSPECTIVE
SUMMARIZE_PROVISIONALLY
WITHHOLD
TRANSITION_TO_COMPOSITION
```

The relevant optimization problem is not simply which response would be most fluent, comprehensive, or persuasive.

It is:

> **Given the current interaction state, what is the smallest useful system move that creates the greatest opportunity for productive human cognition?**

### Joint move representation

A next move may not be adequately represented as a cognitive operation followed by an independent language-generation stage.

The linguistic realization of a cognitive move can change its effective cognitive and relational properties.

A candidate move may therefore require a joint representation:

```text
M = {
    cognitive_function,
    linguistic_realization,
    interactional_affordance
}
```

Several utterances may all instantiate a nominal `CHALLENGE` while differing substantially in:

- cognitive accessibility
- face threat
- perceived authority
- permission to disagree
- humor
- relational alignment
- willingness to continue
- interpretation of speaker stance

The controller may therefore need to evaluate cognitive function, linguistic realization, and interactional affordance together.

---

## Governing Principles

The four models describe the interaction.

A separate set of governing principles constrains what the system should do with those representations.

### Preserve human cognitive agency

The system should support cognition without unnecessarily performing the cognition on the human's behalf.

### Optimize for the human's next move

The primary optimization target is not the apparent intelligence of the system's next utterance.

It is the quality of the cognitive or interactional possibility made available to the human next.

### The system may propose. The human must recognize.

The system may offer a candidate interpretation, distinction, hypothesis, or representation.

A system-generated proposition should not automatically become part of the represented human cognitive state.

Recognition may take the form of acceptance, rejection, revision, qualification, application, or counterexample.

### The system may challenge. The human must judge.

The system may expose contradictions, test warrants, introduce counterexamples, or surface alternatives.

It should not treat its own preferred resolution as the destination.

### Do not manufacture certainty

Observation, inference, hypothesis, contradiction, uncertainty, and missing evidence should remain distinguishable.

### Treat correction and rejection as information

When the human says:

> "No, that's not what I mean."

the interaction has produced valuable evidence.

Correction should update the models rather than merely trigger another attempt at generating a more agreeable response.

### Prefer high-information / low-intrusion elicitation

Ask for the smallest amount of additional information likely to reduce meaningful uncertainty.

Personalization should not require exhaustive biography, identity inference, or unnecessary disclosure.

### Preserve semantic intent across rhetorical transposition

When the system eventually assists with expression, changes in register, organization, audience fit, or style should not silently change the judgment produced during deliberation.

### Withholding is a legitimate action

More system output is not inherently more helpful.

The best next move may be to avoid supplying a distinction, conclusion, inference, or sentence that the human should still produce.

---

## Deliberation Before Composition

Generation does not belong inside the deliberative loop by default.

```text
DELIBERATION
     ↓
STABILIZED HUMAN JUDGMENT
     ↓
OPTIONAL COMPOSITION SUPPORT
     ↓
TRACEABLE ARTIFACT
```

The system should distinguish:

```text
reasoning support
        ↓
representation support
        ↓
composition support
```

These operations can interact, but they should not silently collapse into one.

Possible indicators of conceptual stability include:

- important terms have usable meanings
- material contradictions have been surfaced
- relevant assumptions are visible
- warrants can be articulated
- evidence and inference are distinguishable
- relevant alternatives have been considered
- uncertainty can be represented
- the human recognizes the resulting judgment as their own

Conceptual stability does **not** mean certainty.

A stable representation may explicitly preserve unresolved uncertainty.

The architecture's purpose is not to prohibit generation.

It is to prevent generation from silently substituting for unfinished human cognition.

---

## Cognitive Provenance

This architecture creates a possible alternative to thinking about authorship solely in terms of token production.

Instead of asking only:

> **Did the human manually produce every word?**

we can also ask:

> **Can the human account for the judgment embodied in the artifact?**

A deliberation trace might preserve:

```text
initial observation
        ↓
tentative interpretation
        ↓
counterexample
        ↓
rejected explanation
        ↓
new distinction
        ↓
revised claim
        ↓
remaining uncertainty
        ↓
stabilized judgment
        ↓
optional composition
```

The artifact therefore has not only textual provenance but potentially **cognitive provenance**: evidence of how its substantive judgments developed.

The useful evidence is not necessarily keystrokes, browser activity, or token-level attribution.

It is the evolution of the human's model.

This does not prove independent authorship. It creates a potentially more educationally meaningful form of intellectual accountability.

---

## Educational Application

Education is a particularly important test environment because generative AI exposes a distinction between:

```text
producing an artifact
```

and:

```text
performing the cognition the artifact is intended to evidence
```

Consider a learner beginning with:

> "Antigone is about whether you should follow laws."

A conventional writing assistant might improve the thesis.

A deliberative system could instead test the representation:

> "Would your argument still work if Creon had made a good law?"

The learner may eventually distinguish the legitimacy of a law from the epistemic limits of authority.

The important educational event is then not merely the final thesis.

It is the transformation:

```text
observation
→ hypothesis
→ counterexample
→ revision
→ distinction
→ judgment
→ claim
```

The learner experienced the discovery.

### Domain-specific deliberation

The general architecture may remain stable while the epistemic objects being examined change by discipline.

| Domain | Deliberative objects |
|---|---|
| Literary analysis | textual evidence, ambiguity, interpretation, counterreading, form |
| History | source, perspective, causation, chronology, contingency, competing explanation |
| Science | observation, hypothesis, mechanism, evidence, confound, falsification |
| Design | stakeholder, constraint, tradeoff, iteration, consequence |
| Ethics | stakeholder, value, duty, consequence, competing principle, uncertainty |
| Rhetoric | audience, exigence, ethos, pathos, logos, kairos, warrant, language, constraint |

The architecture therefore proposes a general cognition-preserving controller with potentially **domain-specific deliberation policies**.

---

## Not a Hidden-Destination Socratic Tutor

Deliberation Room is not intended to be a system that already knows the correct destination and asks increasingly clever questions until the human reaches it.

Its job is better described as:

> **Make the human's reasoning inspectable enough that unstable representations become difficult to maintain unnoticed.**

A successful interaction may end with:

- a stronger conclusion
- a changed conclusion
- a narrower conclusion
- a new distinction
- explicit competing interpretations
- justified uncertainty
- or a decision not to conclude yet

The human may arrive at a judgment the system would not have generated.

That is a feature.

---

## Privacy Research Direction

The architecture creates a second research question.

Many personalization systems benefit from retaining large amounts of raw conversational or personal data.

Deliberation Room asks whether useful personalization can instead operate partly over abstracted interaction state.

For example:

```text
prefers concrete counterexamples
high abstraction tolerance
often reasons through analogy
current claim confidence: moderate
unresolved issue: causal warrant
```

may sometimes be more useful to the controller than retaining every original conversation from which those patterns emerged.

This motivates the hypothesis:

> **A system designed to elicit rather than replace cognition may require less general-purpose generative capability, making local/on-device inference and data-minimized personalization more feasible.**

This is a research hypothesis, not a demonstrated result.

The relevant empirical question is:

> **How little information and general-purpose generative capability are actually necessary for useful next-move selection?**

---

## Headline Research Hypotheses

The six hypotheses below summarize the project's highest-level empirical claims. The full research program currently specifies 18 testable hypotheses, including operationalizations and potential falsification criteria; see [research/hypotheses.md](research/hypotheses.md).

Deliberation Room should currently be understood as an interaction architecture and research program.

### H1 — Cognition-preserving interaction

Constrained next-move selection can preserve more human cognitive responsibility than unrestricted generative assistance.

### H2 — Adaptive elicitation

Elicitation conditioned on cognitive state, reasoning patterns, linguistic meaning, and interactional context can outperform generic Socratic questioning for relevant deliberative tasks.

### H3 — Constrained inference

Because next-move selection is narrower than unrestricted general-purpose generation, useful performance may be achievable at model sizes compatible with local or on-device inference.

### H4 — Data-minimized personalization

Abstracted interaction-state representations may support useful personalization while reducing the need to store raw conversational or biographical data.

### H5 — Cognitive provenance

Structured deliberation traces may provide more educationally meaningful evidence of human intellectual accountability than token-level provenance alone.

### H6 — Sociolinguistically informed move selection

Modeling social meaning before action selection may improve interactional appropriateness compared with systems that apply tone or style adaptation only after semantic response generation.

These hypotheses are intended to be falsifiable.

They should not be treated as established merely because the architecture makes them plausible.

---

## What This Project Does Not Yet Claim

Deliberation Room does not currently establish that:

- cognition can be directly inferred from conversation
- the four-model representation is optimal
- conceptual stability can already be measured reliably
- adaptive elicitation outperforms existing tutoring approaches
- cognitive provenance proves independent authorship
- abstracted state eliminates privacy risk
- small or local models are sufficient for the controller
- sociolinguistic modeling can be performed without error or bias
- every task benefits from deliberation
- generation is inherently harmful
- or the architecture has been empirically validated

These are precisely the kinds of questions the project is intended to make testable.

---

## Status

**Current status: conceptual interaction architecture / early research specification.**

Current areas of development include:

- interaction-state representation
- next-move policy design
- cognitive stability criteria
- joint cognitive/linguistic/interactional move representation
- uncertainty representation
- cognitive provenance
- domain-specific deliberation policies
- privacy-preserving personalization
- local inference feasibility
- evaluation design
- related-work mapping

The project intentionally distinguishes:

1. architectural commitments
2. working hypotheses
3. implementation proposals
4. empirical findings

Those categories should not be treated as interchangeable.

---

## Core Heuristic

> **Do not optimize merely for what the model should say next.**
>
> **Optimize for what the human should be able to do next.**
