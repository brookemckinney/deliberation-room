# Architecture Overview

Deliberation Room is a cognition-preserving interaction architecture for AI systems.

Its central optimization target is:

> **What should the human be able to do next?**

rather than simply:

> **What should the model say next?**

The architecture treats AI-mediated deliberation as a dynamic, partially observed interaction-state problem.

The system does not have direct access to a human's cognition, reasoning process, linguistic meaning, or social world. It receives evidence through interaction and maintains provisional representations that are continuously revised as the human responds.

---

## Core Interaction Loop

At the highest level:

```text
HUMAN CONTRIBUTION
        ↓
MODEL CURRENT INTERACTION STATE
        ↓
SELECT NEXT MOVE
        ↓
REALIZE MOVE IN INTERACTION
        ↓
HUMAN RESPONDS
        ↓
UPDATE MODELS
        ↺
```

Generation is not the default objective of this loop.

The immediate output of the architecture is better understood as a **selected interactional move** whose purpose is to create a useful next cognitive possibility for the human.

---

## Interaction State

At time `t`, the architecture maintains a provisional interaction state:

```text
S_t = {
    C_t,
    P_t,
    L_t,
    I_t
}
```

where:

```text
C_t = Cognitive State Model
P_t = Person / Reasoning Model
L_t = Linguistic / Sociolinguistic Model
I_t = Interaction Model
```

These models answer different questions.

### Cognitive State Model

> **What does the human currently appear to understand?**

Possible representations include:

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

### Person / Reasoning Model

> **How does this human productively think?**

Possible representations include:

- expertise
- prior knowledge
- analogical habits
- abstraction tolerance
- preferred challenge modes
- productive reasoning strategies
- response to counterexamples
- representation preferences
- previously established conceptual structures

### Linguistic / Sociolinguistic Model

> **How does meaning operate for this human in this discourse environment?**

Possible representations include:

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
- shared vocabulary
- professional or community-specific language
- relational language history
- repair behavior

### Interaction Model

> **What does a move do here, between these people, for this purpose?**

Possible representations include:

- power
- status
- role
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

---

## The Four Models Are Not a Pipeline

The architecture should not be understood as:

```text
COGNITION
    ↓
PERSONALIZATION
    ↓
LANGUAGE
    ↓
SOCIAL CONSTRAINT CHECK
    ↓
OUTPUT
```

That representation would fundamentally mischaracterize the model.

The four representations are **interdependent sources of evidence about one situated interaction**.

A better approximation is:

```text
                 ┌──────────────────┐
                 │ COGNITIVE STATE  │
                 └────────┬─────────┘
                          ↕
              ┌───────────┼───────────┐
              ↕           ↕           ↕
        ┌──────────┐ ┌──────────┐ ┌───────────┐
        │ PERSON / │↔│LINGUISTIC│↔│INTERACTION│
        │REASONING │ │ / SOCIO- │ │   MODEL   │
        │  MODEL   │ │LINGUISTIC│ │           │
        └──────────┘ └──────────┘ └───────────┘
```

A single human contribution may update several models simultaneously.

For example:

> "No, that's technically what I said, but that's not what that phrase means between us."

may provide evidence about:

- the human's intended conceptual distinction;
- the semantic meaning of a phrase;
- shared relational language history;
- the interactional significance of that phrase;
- and the system's prior inference error.

Correction is therefore not merely a request for regenerated language.

It is **state information**.

---

## Observation and Inference

Because the architecture operates over partially observed human states, every representation should preserve epistemic status.

At minimum, the system should be capable of distinguishing:

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
User rejected three candidate descriptions containing "abandoned."

INFERRED
The term may not preserve the user's intended distinction.

HYPOTHESIZED
The user may distinguish lack of reciprocity from abandonment.

UNKNOWN
Whether the conceptual distinction or only the lexical realization
is causing the rejection.

USER-CONFIRMED
"I don't feel abandoned. I feel like I'm being planned around
instead of planned with."
```

An inference should never silently become an observation.

A system-generated concept should never silently become a human-held concept.

---

## Next-Move Selection

Given the current state, the architecture selects a next move:

```text
A_t = π(S_t, G_t, K)
```

where:

```text
A_t = selected action
S_t = current interaction state
G_t = current human goal
K   = governing principles
π   = next-move policy
```

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
SURFACE_ASSUMPTION
SURFACE_CONTRADICTION
SURFACE_UNCERTAINTY
REQUEST_EVIDENCE
COMPARE
INVITE_PERSPECTIVE
SUMMARIZE_PROVISIONALLY
WITHHOLD
TRANSITION_TO_COMPOSITION
```

The action space is intentionally broader than "ask another question."

Deliberation Room is therefore not equivalent to a generic Socratic prompting strategy.

---

## Joint Move Representation

Selecting a cognitive action and generating its language may not be cleanly separable operations.

The linguistic realization of a move can alter what the move **does** cognitively and socially.

A candidate move may therefore require a joint representation:

```text
M_t = {
    cognitive_function,
    linguistic_realization,
    interactional_affordance
}
```

Consider three possible realizations of a challenge:

```text
"What evidence supports that conclusion?"

"Wait — does that still work if the opposite is true?"

"Okay, try to break your own rule for me."
```

All three may nominally perform `CHALLENGE`.

They may nevertheless differ in:

- cognitive accessibility
- perceived authority
- face threat
- stance
- playfulness
- permission to disagree
- relational alignment
- willingness to expose uncertainty
- likelihood of continued participation

The optimal cognitive intervention therefore cannot always be selected independently of its social and linguistic realization.

This is why linguistic/sociolinguistic and interactional information participate in **move selection itself**, rather than functioning only as post-generation personalization or constraint layers.

---

## Next-Move Objective

Conceptually, candidate moves may eventually be evaluated against factors such as:

```text
EXPECTED COGNITIVE VALUE
+ EXPECTED INFORMATION GAIN
+ HUMAN AGENCY PRESERVED
+ RESPONSE LATITUDE
+ CORRECTABILITY

- COGNITIVE SUBSTITUTION RISK
- INTRUSION COST
- INTERACTIONAL RISK
- PREMATURE CERTAINTY
- UNNECESSARY DISCLOSURE PRESSURE
```

This is a conceptual objective function, not an implemented or empirically validated scoring formula.

The architecture's core question remains:

> **Given the current state, what is the smallest useful intervention that creates the greatest opportunity for productive human cognition?**

---

## High-Information / Low-Intrusion Elicitation

The system should not maximize the amount of information it knows about the human.

It should seek information when that information is likely to change the next move.

Suppose the system has three competing interpretations.

A low-value strategy might be:

```text
Ask the human for extensive background.
```

A higher-value strategy may be:

```text
Find one distinction whose answer separates the competing interpretations.
```

The target is therefore not maximal personal knowledge.

It is **sufficient interactional resolution**.

This principle has implications for both usability and privacy.

---

## Human Response as Model Evidence

After the selected move is realized, the human responds:

```text
O_(t+1)
```

The architecture updates its state:

```text
S_(t+1) = U(S_t, M_t, O_(t+1))
```

where `U` represents the state-update process.

The human response may:

- confirm a representation;
- reject it;
- qualify it;
- introduce a new distinction;
- expose a contradiction;
- resolve an ambiguity;
- create new uncertainty;
- reveal that a question was poorly selected;
- demonstrate that the system overgeneralized;
- or indicate that deliberation should stop.

Human correction is therefore a primary source of architectural information.

---

## Deliberation and Composition

The architecture distinguishes deliberation from composition.

```text
DELIBERATION
     ↓
STABILIZED HUMAN JUDGMENT
     ↓
OPTIONAL COMPOSITION SUPPORT
     ↓
TRACEABLE ARTIFACT
```

During deliberation, the objective is to help the human inspect and develop the underlying representation.

During composition, the objective may shift toward:

- organization
- rhetorical transposition
- audience adaptation
- compression
- elaboration
- clarity
- stylistic realization
- artifact production

The architecture should preserve the boundary because polished representation can create the appearance of conceptual stability even when the underlying human model remains unstable.

---

## Conceptual Stability

Conceptual stability does not mean certainty or correctness.

It describes the degree to which a representation has survived relevant opportunities for:

- clarification;
- distinction;
- evidence checking;
- counterexample;
- contradiction;
- alternative explanation;
- perspective;
- and explicit uncertainty.

A stable state might be:

> "I currently think X because A and B. Y remains plausible, but it would require C, which I do not currently have evidence for."

The architecture should therefore be capable of preserving uncertainty rather than treating uncertainty as an unfinished answer.

---

## Deliberation Trace

The interaction loop naturally produces a sequence of state transitions:

```text
S_0
 ↓
M_0
 ↓
O_1
 ↓
S_1
 ↓
M_1
 ↓
O_2
 ↓
S_2
 ...
```

This sequence can support a **deliberation trace**: a representation of how the human's reasoning changed across interaction.

A trace may capture events such as:

```text
HUMAN INTRODUCED CLAIM
SYSTEM SURFACED ASSUMPTION
HUMAN REJECTED ASSUMPTION
SYSTEM OFFERED COUNTEREXAMPLE
HUMAN REVISED CLAIM
HUMAN INTRODUCED DISTINCTION
SYSTEM TESTED DISTINCTION
HUMAN STABILIZED JUDGMENT
```

This trace is not merely conversation history.

It represents the **development of the model**.

---

## Provenance Has More Than One Dimension

A trace also makes it possible to distinguish different forms of contribution.

At minimum, future implementations should investigate separate representations of:

### Conceptual provenance

Who introduced, distinguished, tested, revised, rejected, and stabilized the substantive idea?

### Linguistic provenance

Who supplied the verbal realization used in the final artifact?

These are not equivalent.

A human may originate a substantive judgment that AI later expresses in different language.

Conversely, AI may propose a concept using language that the human later repeats without demonstrating independent understanding.

Possible conceptual-provenance states include:

```text
HUMAN-ORIGINATED
AI-PROPOSED → HUMAN-RECOGNIZED
AI-PROPOSED → HUMAN-REVISED
AI-PROPOSED → HUMAN-REJECTED
JOINTLY-DEVELOPED
AI-SUPPLIED / HUMAN-UPTAKE-UNRESOLVED
```

The architecture should not collapse these into a binary "human versus AI" authorship label.

---

## Metacognitive Feedback

The deliberation trace may also support feedback to the human about **how they reasoned during the interaction**.

For example:

```text
You made most substantive revisions after encountering counterexamples.

You generated claims readily but required more elicitation around warrants.

Three of your strongest distinctions emerged while comparing concrete cases.

You rejected more system interpretations than you accepted; those
corrections progressively narrowed the model.

Analogy was productive during exploration but contributed little during
final claim stabilization.
```

These observations should be derived from interaction evidence rather than presented as fixed psychological traits.

The system should prefer:

```text
"Counterexamples were productive in this deliberation."
```

over:

```text
"You are a counterexample thinker."
```

unless broader evidence supports that generalization and the human recognizes it.

Metacognitive feedback itself therefore returns to the interaction loop:

```text
DELIBERATION
      ↓
DELIBERATION TRACE
      ↓
METACOGNITIVE OBSERVATION
      ↓
HUMAN RECOGNIZES / REJECTS / QUALIFIES
      ↓
PERSON / REASONING MODEL UPDATES
      ↺
```

The system's model of how the human thinks remains corrigible by the human.

---

## Quantifying Human and AI Contribution

The architecture may eventually support quantitative descriptions of human and system contribution.

However, such measures require care.

Simple token percentages cannot establish conceptual authorship.

For example:

```text
Human:
"I don't think it's about being ignored. It's that she notices the
details that relate to what I'm going to do next."

AI composition:
"My concern isn't a lack of attention generally; it's the selective
attention to details that bear on my future."
```

The final wording may be largely system-generated while the substantive distinction is human-originated.

Useful future measures might therefore separately estimate:

```text
CONCEPTUAL CONTRIBUTION
LINGUISTIC CONTRIBUTION
PROPOSALS ACCEPTED
PROPOSALS REVISED
PROPOSALS REJECTED
HUMAN-ORIGINATED DISTINCTIONS
HUMAN-ORIGINATED COUNTEREXAMPLES
HUMAN REVISIONS AFTER CHALLENGE
UNCERTAINTIES RETAINED
```

A future report might descriptively summarize these patterns.

Exact percentages should not be presented as objective measures of "human authorship" unless the underlying classification methods are empirically validated.

This is an open measurement problem.

---

## Architectural Consequence

The complete loop therefore extends beyond simple question-and-answer interaction:

```text
                    HUMAN
                      ↓
              INTERACTION STATE
                      ↓
               NEXT-MOVE POLICY
                      ↓
                JOINT MOVE
                      ↓
                    HUMAN
                      ↓
                 STATE UPDATE
                      ↺

                 meanwhile:

              DELIBERATION TRACE
                 ↙          ↘
        PROVENANCE        METACOGNITIVE
         ANALYSIS            FEEDBACK
              ↓                 ↓
       TRACEABLE          HUMAN REVIEWS /
        ARTIFACT          CORRECTS MODEL
                              ↓
                     PERSON / REASONING
                       MODEL UPDATES ↺
```

This creates two related forms of accountability:

1. **artifact accountability** — how substantive judgments represented in an artifact developed; and
2. **model accountability** — whether the system's evolving representation of the human can itself be inspected and corrected.

---

## Implementation Neutrality

The four conceptual models do not necessarily require four separate machine-learning models.

They could be implemented through combinations of:

- structured state;
- language models;
- small language models;
- classifiers;
- rankers;
- embeddings;
- retrieval;
- rules;
- local models;
- probabilistic state tracking;
- or hybrid architectures.

The conceptual separation exists so that the architecture can be reasoned about, implemented, evaluated, and challenged without assuming a particular underlying model family.

---

## Open Architectural Questions

Key unresolved questions include:

1. What is the minimum useful representation for each model?
2. Which state variables should persist across sessions?
3. Which should remain ephemeral?
4. How should confidence and uncertainty be represented?
5. How should conflicting evidence update a model?
6. How should candidate moves be generated and ranked?
7. Can cognitive function and linguistic realization be jointly optimized reliably?
8. What constitutes sufficient conceptual stability for composition?
9. How can semantic provenance be classified without creating false precision?
10. Which metacognitive patterns can be inferred reliably from deliberation traces?
11. How should humans inspect and correct persistent person/reasoning representations?
12. How much raw interaction history can be discarded once useful state has been abstracted?
13. Which portions of the controller can perform adequately using local or on-device inference?
14. When does deliberation create productive friction, and when does it merely create friction?
15. Under what conditions should the architecture stop intervening entirely?

These questions are part of the research program rather than hidden implementation assumptions.
