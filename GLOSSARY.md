# Glossary

This glossary defines project-specific terminology used throughout Deliberation Room.

These are working definitions.

They are intended to keep the architecture internally consistent while implementation and empirical validation are still in progress.

---

## Cognitive State Model

A provisional representation of what the human currently appears to understand, believe, distinguish, question, assume, support, contradict, or remain uncertain about in relation to the current task.

Possible elements include:

- claims;
- distinctions;
- assumptions;
- warrants;
- evidence;
- contradictions;
- alternatives;
- unresolved questions;
- uncertainty;
- and conceptual stability.

The Cognitive State Model does **not** imply direct access to a human's internal mental state.

It represents evidence available through interaction.

---

## Metacognitive Process Model

A provisional representation of **how productive cognitive movement is currently occurring for this human in this task**.

Possible process dimensions include:

- comparison and contrast;
- analogy;
- counterexample;
- counterfactual testing;
- classification;
- abstraction;
- concrete instantiation;
- causal reasoning;
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

The model may also use relevant evidence about:

- domain expertise;
- prior knowledge;
- previously productive representations;
- abstraction tolerance;
- prior response to challenge modes;
- recurring revision patterns;
- and established reasoning strategies.

However, these should remain contextual rather than becoming fixed cognitive types.

The model's primary question is:

> **How is useful thinking happening right now, and what kind of system move is most likely to support the next productive state change?**

Metacognitive process state is therefore not merely descriptive.

It can function as **live control data** for the next-move policy.

For example:

```text
Observed task pattern:

- counterexamples have produced substantive revision;
- open-ended explanation has produced little change;
- contrastive prompts have produced useful distinctions;
- current abstraction tolerance appears high.
```

The controller may then prefer:

```text
one counterfactual
one changed variable
no supplied conclusion
ask for the invariant
```

This model should remain:

```text
task-bounded
uncertainty-aware
corrigible
contextual
minimally sufficient
```

It should not become a covert personality, intelligence, or learning-style classifier.

---

## Reasoning History

A longer-term record of task-bounded metacognitive observations that may help predict useful future interventions.

Examples may include:

```text
counterexamples repeatedly productive in argument testing
analogy useful during exploration
direct reflection useful during stabilization
high abstraction tolerance in rhetoric tasks
```

Reasoning history is distinct from the Metacognitive Process Model.

The Metacognitive Process Model represents:

```text
WHAT IS HAPPENING NOW
```

Reasoning history provides:

```text
PRIOR EVIDENCE THAT MAY INFORM WHAT TO TRY NEXT
```

Current-task evidence should generally outweigh older generalized patterns.

Reasoning history should preserve:

```text
scope
context
confidence
source
correctability
```

and should not be treated as a fixed cognitive type.

---

## Linguistic / Sociolinguistic Model

A provisional representation of how meaning operates for this human within the current discourse environment.

Possible elements include:

- idiolect;
- register;
- dialect;
- discourse community;
- pragmatics;
- indexicality;
- stance;
- humor;
- irony;
- code-switching;
- role language;
- generational norms;
- shared vocabulary;
- and relational language history.

Its function is not merely to make output "sound like the user."

It helps the architecture reason about what communicative forms mean in context.

---

## Interaction Model

A provisional representation of what a communicative move would do socially and relationally in the present interaction.

Possible elements include:

- role;
- power;
- status;
- familiarity;
- relationship history;
- face;
- belonging;
- audience;
- setting;
- stakes;
- relational distance;
- disclosure pressure;
- response latitude;
- and interactional permissions.

The central question is:

> **What does this move do here, between these people, for this purpose?**

---

## Interaction State

The combined provisional state used by the controller.

Conceptually:

```text
S_t = {
    Cognitive State,
    Metacognitive Process Model,
    Linguistic / Sociolinguistic Model,
    Interaction Model
}
```

This state changes as the human responds.

---

## Next-Move Policy

The mechanism that selects what kind of system intervention should occur next.

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
SURFACE_ASSUMPTION
SURFACE_CONTRADICTION
SURFACE_UNCERTAINTY
REQUEST_EVIDENCE
WITHHOLD
TRANSITION_TO_COMPOSITION
```

The policy should optimize for:

> **What should the human be able to do next?**

rather than only:

> **What should the model say next?**

---

## Joint Move

A representation of a system move that treats cognitive function, linguistic realization, and interactional affordance as interdependent.

Conceptually:

```text
M = {
    cognitive_function,
    linguistic_realization,
    interactional_affordance
}
```

This exists because the same abstract cognitive action can function differently depending on how it is linguistically and socially realized.

---

## Cognitive Function

The reasoning operation a move is intended to support.

Examples include:

- clarify;
- distinguish;
- test;
- challenge;
- compare;
- surface assumption;
- request evidence;
- or preserve uncertainty.

---

## Linguistic Realization

The actual verbal form used to perform a cognitive or interactional move.

For example, the same nominal challenge might be realized as:

> "What evidence supports that?"

or:

> "Wait — does that still work if the opposite is true?"

The realization can alter how the move functions.

---

## Interactional Affordance

The set of meaningful responses or social positions a move makes available to the human.

A move may increase or reduce the human's ability to:

- disagree;
- elaborate;
- redirect;
- disclose;
- withhold;
- correct;
- joke;
- or disengage.

Interactional affordance is one reason response wording cannot always be separated cleanly from move selection.

---

## Response Latitude

The amount of meaningful freedom the human retains in determining what happens next.

High response latitude allows the human to:

```text
agree
disagree
qualify
reject
redirect
expand
narrow
disclose
withhold
or disengage
```

A core heuristic is:

> **Minimum viable system move. Maximum human response latitude.**

---

## Deliberation

The iterative process through which a human:

- notices;
- models;
- distinguishes;
- tests;
- challenges;
- revises;
- represents uncertainty;
- and stabilizes judgment.

Deliberation is distinct from composition.

---

## Composition

The production or transformation of an external artifact after or alongside human reasoning.

Possible artifacts include:

- essays;
- emails;
- messages;
- reports;
- recommendations;
- plans;
- arguments;
- and explanations.

Composition may involve substantial AI assistance without necessarily implying AI-originated judgment.

---

## Composition Boundary

The architectural transition between:

```text
DELIBERATION
```

and:

```text
COMPOSITION SUPPORT
```

The boundary exists because fluent generation can create the appearance of conceptual stability even when the underlying human model remains unstable.

---

## Composition Contract

A structured representation of what must be preserved or constrained when moving from stabilized judgment into artifact generation.

A composition contract may include:

```text
semantic invariants
audience
purpose
rhetorical constraints
permitted transformations
prohibited substantive additions
```

---

## Rhetorical Transposition

The process of expressing substantially the same human judgment under different rhetorical conditions.

Possible changes include:

- register;
- audience;
- medium;
- genre;
- organization;
- concision;
- explicitness;
- and style.

Rhetorical transposition should preserve the substantive model unless the human explicitly revises it.

---

## Semantic Invariant

A substantive element of the human's stabilized judgment that should survive rhetorical transformation.

Example:

```text
The human is uncertain about the other person's motive.
```

A rewritten message should not convert that into:

```text
The other person definitely does not care.
```

without a new human judgment.

---

## Semantic Drift

A change introduced during generation or rewriting that materially alters the human's underlying meaning.

Possible drift includes:

```text
stronger claim
weaker claim
removed uncertainty
new motive attribution
new commitment
collapsed distinction
changed agency
changed stance
```

A rhetorically better sentence can still contain semantic drift.

---

## Conceptual Stability

The degree to which a human representation has survived relevant opportunities for inspection and testing.

Possible tests include:

- clarification;
- counterexample;
- contradiction;
- alternative explanation;
- evidence request;
- warrant testing;
- and explicit uncertainty.

Conceptual stability does **not** mean objective truth or high confidence.

A stable representation can remain uncertain.

---

## Productive Friction

Cognitive effort that materially contributes to the capability the task is intended to develop, exercise, or reveal.

Examples may include:

- forming a claim;
- generating a distinction;
- testing evidence;
- constructing a warrant;
- revising after counterexample;
- or making judgment under uncertainty.

---

## Incidental Friction

Effort that does not materially contribute to the target capability.

Examples may include:

- formatting;
- repetitive transcription;
- mechanical editing;
- low-level organization;
- or language-production burden

when those are not themselves the learning or reasoning objective.

---

## Cognitive Substitution

A system performs a reasoning operation that the human could or should perform for the purpose of the task.

Examples may include the system supplying:

- a central claim;
- key distinction;
- warrant;
- conclusion;
- evidence connection;
- or resolution of contradiction.

Cognitive substitution is not always harmful.

Its value depends on the task objective.

---

## Cognitive Responsibility

The degree to which the human remains responsible for substantive judgment within the interaction.

This includes the opportunity to:

- distinguish;
- reject;
- revise;
- test;
- connect evidence;
- and judge.

---

## Cognitive Provenance

A structured representation of how substantive reasoning developed across human-system interaction.

It may track:

- who introduced a claim;
- who proposed a distinction;
- what triggered revision;
- what the human rejected;
- what remained uncertain;
- and how the final judgment stabilized.

Cognitive provenance is distinct from textual provenance.

---

## Conceptual Provenance

The origin and development history of a substantive idea.

Possible states include:

```text
HUMAN-ORIGINATED
SYSTEM-PROPOSED → HUMAN-RECOGNIZED
SYSTEM-PROPOSED → HUMAN-REVISED
SYSTEM-PROPOSED → HUMAN-REJECTED
JOINTLY-DEVELOPED
SYSTEM-SUPPLIED / HUMAN-UPTAKE-UNRESOLVED
EXTERNAL-SOURCE
UNKNOWN
```

---

## Linguistic Provenance

The origin of the wording used to express a concept or artifact.

Possible states include:

```text
HUMAN-PRESERVED
HUMAN-EDITED
SYSTEM-TRANSPOSED
SYSTEM-GENERATED
JOINTLY-REFINED
UNKNOWN
```

Conceptual and linguistic provenance should not be collapsed.

---

## Human-Originated

A substantive claim, distinction, warrant, question, or other cognitive object first introduced by the human.

A system question can trigger a human-originated event without becoming the conceptual source of that event.

Example:

```text
SYSTEM:
Would the claim survive if X changed?

HUMAN:
Then the real issue is actually Y.
```

The system supplied the test.

The human supplied the distinction.

---

## System-Proposed

A concept or representation introduced by the system for the human to inspect.

A system proposal should not automatically enter the human cognitive state as established understanding.

---

## Recognition (Cognitive Uptake)

Evidence that the human has meaningfully encountered a system proposal rather than merely receiving it.

Recognition may include:

- restatement;
- qualification;
- application;
- extension;
- counterexample;
- revision;
- defense;
- or coherent reuse.

Simple agreement is weaker evidence.

---

## Human Uptake

The degree to which a system-supplied concept has become part of the human's demonstrated reasoning.

Possible states include:

```text
UNRESOLVED
RECOGNIZED
REVISED
REJECTED
APPLIED
EXTENDED
```

---

## Jointly Developed

A concept whose development is not usefully attributable to only the human or only the system because it emerged through iterative interaction.

This label should not be used merely because both participants spoke before the final idea appeared.

It should reflect genuine co-development.

---

## Question-Resolution Provenance

A record of who substantively resolved a reasoning question.

Possible states include:

```text
HUMAN-RESOLVED
SYSTEM-RESOLVED
JOINTLY-RESOLVED
UNRESOLVED
HUMAN-REJECTED-PREMISE
EXTERNAL-EVIDENCE-REQUIRED
```

This is distinct from who asked the question.

---

## Deliberation Trace

A structured record of meaningful state transitions across a deliberation.

A trace may include:

```text
claim introduced
assumption surfaced
counterexample presented
human rejection
distinction generated
claim revised
uncertainty retained
judgment stabilized
composition transition
```

It is not simply a raw transcript.

---

## Metacognitive Feedback

Feedback derived from the deliberation trace about how reasoning developed during a task.

Examples:

> "Most substantive revisions followed counterexamples."

> "Claims emerged independently, while warrants required more elicitation."

> "You rejected more system interpretations than you accepted."

Such observations should initially remain task-level and corrigible.

---

## Metacognitive Summary

A structured description of reasoning patterns observed within a task or across explicitly scoped tasks.

Examples may include:

> "Most substantive revisions in this task followed counterexamples."

> "Claims emerged independently, while warrants required more elicitation."

> "Five system-proposed framings were revised before the final distinction stabilized."

A Metacognitive Summary is primarily **descriptive feedback**.

It is different from the Metacognitive Process Model, which operates during the interaction as live controller state.

It is also different from Reasoning History, which may preserve selected observations for future prediction.

A Metacognitive Summary should remain:

```text
contextual
provisional
corrigible
non-diagnostic
```

It should not assign a fixed cognitive identity.

---
## Corrigibility

The ability of the human to correct, reject, narrow, or delete important system representations.

Corrigibility applies to:

- cognitive state;
- person/reasoning state;
- linguistic interpretation;
- interactional assumptions;
- provenance;
- and persistent personalization.

A model of the human that cannot be corrected becomes a constraint rather than useful personalization.

---

## Epistemic Status

The status of a represented object with respect to evidence.

Possible states include:

```text
OBSERVED
INFERRED
HYPOTHESIZED
USER-CONFIRMED
CONTRADICTED
UNKNOWN
```

Epistemic status should remain distinct from source provenance.

---

## Observation

Information directly available from the interaction or a trusted source.

Example:

```text
The user said: "I don't think it's about attention."
```

---

## Inference

A conclusion drawn from available evidence but not directly stated or confirmed.

Example:

```text
The user may distinguish attention from inclusion.
```

---

## Hypothesis

A provisional candidate representation being considered or tested.

A hypothesis may later be:

- confirmed;
- revised;
- rejected;
- or remain unresolved.

---

## User-Confirmed

A representation the human has explicitly or behaviorally demonstrated as part of their current model.

Confirmation should not necessarily require exact wording repetition.

---

## Uncertainty

A represented absence of sufficient grounds for a stable judgment.

Uncertainty is not necessarily a defect.

It may be an appropriate end state.

---

## High-Information / Low-Intrusion Elicitation

The principle that the system should seek information that materially reduces important uncertainty while requiring as little unnecessary disclosure as possible.

The practical question is:

> **What is the smallest question whose answer would materially change the next move?**

---

## Withhold

A legitimate next-move action in which the system intentionally avoids adding substantive content.

Withholding may be appropriate when:

- more system content would replace useful human reasoning;
- the human can continue independently;
- system uncertainty is too high;
- further questioning would become intrusive;
- or no intervention has sufficient expected value.

---

## Minimum Viable System Move

The smallest intervention expected to create useful cognitive progress while preserving human agency.

This principle discourages unnecessary explanatory overproduction.

---

## Minimum Viable Relational Move

The smallest interactional move that creates a useful social opening without unnecessary disclosure, surveillance cues, identity narrowing, or response pressure.

---

## Relational Recognition

In relational contexts, recognition means communicating that a person is noticed, remembered, understood, or granted a meaningful position in the interaction.

Recognition is distinct from demonstrating how much information the system or speaker has collected.

---

## Demonstrated Knowledge

The overt display of information about another person.

Demonstrated knowledge may support recognition, but it may also signal:

- surveillance;
- tracking;
- overresearch;
- or inappropriate familiarity.

The architecture should not assume more demonstrated knowledge produces better relational interaction.

---

## Research Visibility

The degree to which an interactional move reveals that information was externally searched, monitored, or deliberately collected.

Possible levels may include:

```text
LOW
MODERATE
HIGH
```

Research visibility should be considered separately from whether the underlying information is public.

---

## Identity-Confirming Move

A move that interacts with the person primarily through an already salient identity or role.

Example:

```text
student-athlete → athletics topic
```

Identity-confirming interaction may be useful, but repeated use can narrow the person's available social identity.

---

## Identity-Expanding Move

A move that creates space for the person to participate outside the most salient known identity or role.

The objective is not to avoid identity.

It is to preserve the person's ability to define what matters in the interaction.

---

## Belonging

A relational condition in which the person can experience themselves as:

- recognized;
- intelligible;
- able to participate;
- able to correct;
- not reduced to a category;
- and able to exercise agency without unnecessary social penalty.

Belonging is not synonymous with friendliness.

---

## Face

The social value a participant may be attempting to preserve in an interaction.

Relevant concerns may include:

- competence;
- autonomy;
- dignity;
- privacy;
- status;
- expertise;
- belonging;
- and relational standing.

---

## Disclosure Pressure

The degree to which a move makes personal disclosure socially difficult to refuse.

Disclosure pressure can be amplified by power asymmetry.

---

## Interactional Permission

Evidence that a particular form of interaction is appropriate within the current relationship and context.

Examples include permission for:

- humor;
- teasing;
- direct challenge;
- intimacy;
- informal language;
- or personal disclosure.

Interactional permissions should remain contextual and revisable.

---

## Pragmatic Fit

The degree to which language functions appropriately within the actual discourse and relationship.

Pragmatic fit differs from surface similarity.

The system may understand and adapt to a language practice without reproducing it.

---

## Linguistic Mimicry

Surface imitation of:

- dialect;
- slang;
- cultural language;
- generational language;
- identity-linked forms;
- or individual style

without sufficient interactional justification.

Deliberation Room distinguishes interactional competence from mimicry.

---

## Interactional Competence

The capacity to interpret and realize language in a way that respects:

- meaning;
- stance;
- register;
- role;
- relationship;
- and social action.

Interactional competence includes knowing when **not** to reproduce a form the system understands.

---

## Idiolect

The recurring linguistic practices of an individual.

Within Deliberation Room, idiolect may include patterns shaped by:

- profession;
- geography;
- community;
- generation;
- relationship history;
- humor;
- vocabulary;
- cadence;
- and recurring conceptual shorthand.

An idiolect model should remain descriptive and provisional.

---

## Local Semantics

Meaning established through repeated interaction rather than recoverable from general lexical knowledge alone.

Example:

```text
"walking the orb"
```

may function as shared shorthand for a larger previously developed reasoning process.

---

## Repair

A correction made by the human when the system's interpretation, wording, framing, or interactional move is inaccurate.

Repair is a high-value source of model information.

Examples:

> "That's not what I mean."

> "The idea is right, but the wording is too strong."

> "That joke would sound wrong coming from me."

---

## Reception Modeling

The process of considering plausible ways an utterance may be interpreted by another person.

Reception modeling should preserve uncertainty.

It is distinct from claiming to know another person's internal response.

---

## Rhetorical Reception

The likely interpretive and social possibilities created by an utterance for a particular audience.

This may include:

- perceived stance;
- implied accusation;
- emotional force;
- response latitude;
- disclosure pressure;
- and relational positioning.

---

## Outcome

The eventual response or consequence of an interaction.

The architecture distinguishes outcome from utterance quality because the speaker cannot fully control:

- agreement;
- affection;
- compliance;
- forgiveness;
- or response.

Hence:

> **Control the utterance. Model the reception. Relinquish the outcome.**

---

## Cognitive Agency

The human's capacity to participate meaningfully in:

- interpretation;
- judgment;
- revision;
- decision;
- and expression.

A cognition-preserving system seeks to increase capability without unnecessarily transferring these operations to the system.

---

## Intellectual Accountability

The capacity of a human to explain and defend the substantive judgments represented in an artifact.

A useful question is:

> **Why is this here?**

A person with intellectual accountability should often be able to explain:

- where a claim came from;
- what challenged it;
- why it changed;
- what evidence matters;
- and what uncertainty remains.

---

## Traceable Artifact

An artifact whose substantive elements can be connected back to relevant deliberative history.

A traceable artifact may preserve relationships among:

```text
final claim
source judgment
revisions
counterexamples
evidence
conceptual provenance
linguistic provenance
```

---

## Data-Minimized Personalization

Personalization based on the minimum state necessary to improve interaction rather than maximal retention of raw conversation.

Possible mechanisms include:

- abstracted state;
- local processing;
- ephemeral state;
- scoped persistence;
- and user-correctable representations.

Data-minimized does not mean non-sensitive.

---

## Persistence Scope

The context and duration over which a representation remains available.

Possible scopes include:

```text
TURN
SESSION
TASK
DOMAIN
RELATIONSHIP
CROSS-DOMAIN
PERSISTENT
```

Broader persistence should require stronger justification.

---

## Context Collapse

The inappropriate reuse of a representation outside the context in which it was valid.

Example:

```text
gentle teasing works in one close relationship
```

does not imply:

```text
gentle teasing is generally appropriate for this user
```

---

## Personalization Lock-In

A failure mode in which the system repeatedly uses historically successful strategies and therefore stops gathering evidence that another strategy might work better.

This can create self-fulfilling personalization.

---

## Exploration Versus Exploitation

The policy tension between:

```text
EXPLOIT:
use a strategy already supported as productive

EXPLORE:
try another plausible strategy to improve the model
```

Exploration should remain proportionate to risk and stakes.

---

## Domain-Specific Deliberation Policy

A set of discipline- or task-specific rules defining what responsible deliberation requires.

Examples:

### Literature

```text
textual evidence
interpretation
ambiguity
counterreading
```

### Science

```text
observation
hypothesis
mechanism
confound
falsification
```

The general controller may remain stable while domain-specific epistemic objects change.

---

## Walking Rules

Informal project shorthand for the domain-specific ways a person should move through a problem.

Examples include:

```text
What counts as evidence here?

What must be tested?

What alternatives matter?

What uncertainty is legitimate?

What makes a judgment stable?
```

Different domains have different walking rules.

---

## Walking the Model

Informal shorthand for deliberately inspecting a problem representation from multiple conceptual or relational positions until important distinctions, contradictions, or uncertainties become visible.

---

## "Walking the Orb"

Project shorthand for a phenomenological version of walking the model: slowly inspecting a multidimensional conceptual or relational representation from different angles until the structure becomes clearer.

This is descriptive project language, not a formal technical term.

---

## Cognition-Preserving Architecture

An interaction architecture designed to support human reasoning while avoiding unnecessary substitution of model-generated reasoning for human judgment.

Its defining optimization target is:

> **What should the human be able to do next?**

---

# Constitutional Shorthand

The architecture can be compressed into several recurring principles:

> **The system may propose.  
> The human must recognize.**

> **The system may challenge.  
> The human must judge.**

> **Minimum viable system move.  
> Maximum human response latitude.**

> **Control the utterance.  
> Model the reception.  
> Relinquish the outcome.**

And above all:

> **Do not optimize merely for what the model should say next.  
> Optimize for what the human should be able to do next.**
