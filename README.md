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

Deliberation Room contains two coupled engines.

```text
                 HUMAN CONTRIBUTION
                         │
                         ▼
┌───────────────────────────────────────────────────────────┐
│ ENGINE 1 — METACOGNITIVE DELIBERATION                    │
│                                                           │
│ What does this human currently think?                     │
│ How are they productively thinking through it?            │
│ What cognitive operation should remain with them next?    │
│                                                           │
│ notice → model → test → revise → distinguish → judge      │
└───────────────────────────┬───────────────────────────────┘
                            │
                            ▼
                  STABILIZED HUMAN JUDGMENT
                            │
                            ▼
┌───────────────────────────────────────────────────────────┐
│ ENGINE 2 — RHETORICAL COMPILATION                        │
│                                                           │
│ Given what this human means, what exactly should this     │
│ human write or say to this audience, in this situation?   │
│                                                           │
│ rhetoric + audience + interaction + sociolinguistics      │
│ + observed speech/text behavior + genre + evidence        │
└───────────────────────────┬───────────────────────────────┘
                            │
                            ▼
                    EXACT FINAL UTTERANCE
```

The two engines solve different problems.

Engine 1 asks:

> **What should the human be able to do next?**

Engine 2 asks:

> **Given the human judgment that emerged, what exactly should this human say or write here?**

The architecture is cognition-preserving **without being anti-generation**.

Its objective is not to keep the AI from eventually producing language.

Its objective is to preserve the distinction between:

```text
DEVELOPING THE JUDGMENT
```

and:

```text
REALIZING THAT JUDGMENT AS LANGUAGE
```

A mature Deliberation Room may therefore produce the entire final message, email, essay, memo, explanation, or speech.

What matters is that the substantive judgment embodied by that artifact remains inspectable and appropriately attributable.

---

## Engine 1 — Metacognitive Deliberation

Deliberation Room does not merely model **what** the human appears to think.

It also models **how useful cognitive movement is currently occurring**.

Conceptually:

```text
HUMAN UTTERANCE
        │
        ▼
┌─────────────────────────────────────────┐
│ 1. COGNITIVE STATE MODEL               │
│                                         │
│ What does the human currently appear   │
│ to understand?                          │
│                                         │
│ claims • distinctions • assumptions    │
│ warrants • contradictions • evidence   │
│ uncertainty • conceptual stability     │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ 2. METACOGNITIVE PROCESS MODEL         │
│                                         │
│ How is productive thinking currently   │
│ happening for this human?               │
│                                         │
│ comparison • analogy • counterexample  │
│ abstraction • concrete instantiation   │
│ causal reasoning • perspective shift   │
│ elimination • synthesis • classification│
│ recursive correction • evidence-first  │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ 3. LINGUISTIC / SOCIOLINGUISTIC MODEL  │
│                                         │
│ How does meaning operate for this human │
│ in this discourse environment?         │
│                                         │
│ idiolect • register • dialect • stance │
│ pragmatics • humor • discourse norms   │
│ role language • shared vocabulary      │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ 4. INTERACTION MODEL                   │
│                                         │
│ What does a move DO here, between      │
│ THESE people, for THIS purpose?         │
│                                         │
│ power • status • familiarity • history │
│ face • belonging • audience • stakes   │
│ permissions • response latitude        │
└────────────────────┬────────────────────┘
                     │
                     ▼
          METACOGNITIVE NEXT-MOVE POLICY
                     │
          ┌──────────┼───────────┐
          ▼          ▼           ▼
       clarify    challenge   counterexample
       compare    reflect     instantiate
       abstract   distinguish perspective-shift
       test       withhold    ask
                     │
                     ▼
               HUMAN RESPONDS
                     │
                     ▼
             ALL MODELS UPDATE ↺
```

The second model is not merely a static preference profile.

It functions as **live control data** for the system.

For example, the system might infer:

```text
Current task evidence:

- contrastive questions have produced useful distinctions;
- open-ended explanation has produced little state change;
- counterfactual testing has produced revision;
- abstraction tolerance is currently high.
```

That state can alter the next system instruction:

```text
Prefer one contrastive or counterfactual move.

Change only one variable.

Do not supply the distinction.

Allow the human to identify what remains invariant.
```

The system is therefore, in effect, **prompting itself about how to help this particular human continue thinking**.

These observations remain provisional, task-bounded, and corrigible.

They are not fixed cognitive "types."

---

## Engine 2 — Rhetorical Compilation

Once the relevant human judgment is sufficiently stable—or the human explicitly requests composition—the optimization problem changes.

The question becomes:

> **What exactly should this human say or write, to this audience, for this purpose, in this situation?**

Conceptually:

```text
STABILIZED HUMAN JUDGMENT
            │
            ▼
┌─────────────────────────────────────────┐
│ RHETORICAL SITUATION                    │
│                                         │
│ exigence • audience • purpose           │
│ ethos • pathos • logos • kairos         │
│ constraints • available means           │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ INTERACTIONAL CONDITIONS               │
│                                         │
│ role • power • status • familiarity    │
│ history • face • belonging • stakes    │
│ response latitude • social risk        │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ LINGUISTIC / SOCIOLINGUISTIC EVIDENCE  │
│                                         │
│ idiolect • register • dialect • stance │
│ pragmatics • humor • code-switching    │
│ discourse community • role language    │
│ generational norms • shared vocabulary │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ OBSERVED SPEECH / TEXT BEHAVIOR        │
│                                         │
│ actual lexical choices • cadence       │
│ sentence length • discourse markers    │
│ punctuation • explicitness • repair    │
│ prior successful realizations          │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ GENRE / DISCIPLINARY CONVENTIONS       │
│                                         │
│ text • email • essay • memo • speech   │
│ discussion • feedback • proposal       │
│ disciplinary rhetorical expectations  │
└────────────────────┬────────────────────┘
                     │
┌────────────────────▼────────────────────┐
│ RELEVANT EXTERNAL EVIDENCE             │
│                                         │
│ facts • sources • terminology          │
│ conventions • precedents • context     │
└────────────────────┬────────────────────┘
                     │
                     ▼
              RHETORICAL COMPILER
                     │
                     ▼
            SEMANTIC / DRIFT CHECK
                     │
                     ▼
              EXACT FINAL OUTPUT
```

Classical rhetoric functions here as more than a vocabulary list.

It provides part of the decision structure for composition:

```text
EXIGENCE
Why must something be said?

AUDIENCE
Who must receive it?

PURPOSE
What should the utterance accomplish?

ETHOS
What speaker-position should the language establish?

PATHOS
What affective conditions matter?

LOGOS
What reasoning must be visible?

KAIROS
Why this move, in this form, at this moment?

CONSTRAINTS
What limits the available rhetorical choices?

AVAILABLE MEANS
Which linguistic and rhetorical resources can this speaker
appropriately use?
```

These variables interact with sociolinguistic and empirical language evidence.

The architecture is therefore not:

```text
reason
→ generate generic prose
→ apply tone
```

It is:

```text
human judgment
× rhetorical situation
× audience
× relationship
× discourse community
× idiolect
× observed language behavior
× genre
× evidence
        ↓
situated rhetorical realization
```

---

## Compression Is a Valid Rhetorical Outcome

A sophisticated model does not imply a long output.

Sometimes extensive deliberation and audience modeling should produce radical compression.

For example:

```text
INTERNAL PROBLEM
How do I explain why this person belongs inside the idea?

DELIBERATIVE DISCOVERY
The important claim is not the architecture itself.
The important claim is affection for the way this person thinks
about and cares for other people.

RHETORICAL CONDITIONS
intimate relationship
high shared context
low need for exposition
belonging is the communicative objective

OUTPUT
"You're in it because I love the way your mind loves people."
```

The sentence is effective not because the system generated prettier language.

It is effective because deliberation identified the relevant human meaning and rhetorical compilation recognized that **compression preserved the strongest relational act**.

---

## Disciplinary Walking Rules

The metacognitive controller can also be conditioned by disciplinary epistemology.

The general loop remains:

```text
notice
→ model
→ test
→ revise
→ perspective
→ stabilize
→ express
```

but the responsible cognitive moves vary by domain.

For literary analysis:

```text
textual evidence
interpretation
counterreading
ambiguity
form
```

For history:

```text
source
perspective
causation
chronology
contingency
competing explanation
```

For science:

```text
observation
hypothesis
mechanism
evidence
confound
falsification
```

For design:

```text
stakeholder
constraint
tradeoff
iteration
consequence
```

For ethics:

```text
stakeholders
values
duties
consequences
competing principles
uncertainty
```

For rhetoric:

```text
audience
exigence
ethos
pathos
logos
kairos
constraints
warrants
language
```

The architecture does not merely switch knowledge bases.

It changes **what counts as responsible cognitive movement in the domain**.

---

## Provenance Across Both Engines

The complete architecture should preserve at least three different forms of contribution:

```text
CONCEPTUAL PROVENANCE
Who developed the judgment?

METACOGNITIVE PROVENANCE
Which interventions and reasoning processes produced meaningful change?

LINGUISTIC PROVENANCE
Who supplied the final verbal realization?
```

This permits outcomes such as:

```text
concept:
predominantly human-developed

deliberative support:
system counterexamples + human revisions

organization:
jointly developed

final wording:
primarily system-generated
```

without collapsing the entire artifact into:

```text
AI
vs.
human
```

The eventual output can therefore be highly system-assisted linguistically while remaining traceable to human judgment.

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

### 2. Metacognitive Process Model

How is this human productively thinking **right now**, and what form of cognitive support is most likely to produce the next useful state change?

This model represents the observed process of reasoning rather than merely the content of the reasoning.

Candidate process dimensions include:

- comparison and contrast;
- analogy;
- counterexample;
- counterfactual testing;
- classification;
- abstraction;
- concrete instantiation;
- causal chaining;
- perspective shifting;
- elimination;
- constraint solving;
- synthesis;
- recursive correction;
- evidence-first reasoning;
- intuition-first hypothesis generation;
- warrant construction;
- invariant detection;
- and movement between concrete and abstract representation.

It may also use relevant evidence about:

- domain expertise;
- prior knowledge;
- previously productive representations;
- abstraction tolerance in the current task;
- prior response to particular challenge modes;
- recurring revision patterns;
- and established reasoning strategies.

But these should not be treated as fixed cognitive types.

The primary object is the **current reasoning process**.

For example, the model might represent:

```text
CURRENT TASK EVIDENCE

contrastive prompts:
productive

counterexamples:
produced substantive revision

open-ended explanation:
low information gain

current abstraction tolerance:
high

current likely next need:
identify invariant across cases
```

That state can directly condition the next system move.

For example:

```text
CONTROLLER INSTRUCTION

Use one counterfactual.

Change only one variable.

Do not name the distinction.

Ask what remains true across both cases.
```

This is a central architectural claim:

> **Metacognitive evidence is not merely feedback generated after deliberation. It is live control data for the next-move policy.**

The system may therefore adapt not simply to what the human knows, but to **how useful cognitive movement is currently occurring**.

Human correction remains essential.

An observation such as:

> "Counterexamples were productive in this argument task."

should not silently become:

> "This person is a counterexample thinker."

The model should preserve:

```text
task
context
evidence
confidence
scope
correctability
```

A longer-term person-specific reasoning history may help predict useful moves, but it should remain subordinate to evidence from the present task.

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
        ├── Metacognitive process
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
