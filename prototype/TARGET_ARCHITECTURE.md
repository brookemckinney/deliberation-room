# Target Architecture

This document describes the intended technical shape of the next AI-backed Deliberation Room prototype.

It is not a production architecture.

Its purpose is to define the smallest credible implementation path from the current transparent control-core scaffold toward the larger research architecture.

The target system should preserve three properties:

```text
1. HUMAN COGNITIVE AGENCY

2. INSPECTABLE STATE / POLICY / PROVENANCE

3. EXACT RHETORICAL OUTPUT
```

The system should not achieve the third by collapsing the first two into one unrestricted prompt.

---

# 1. Current Prototype

The current prototype already implements:

```text
structured cognitive state

explicit epistemic status

conceptual provenance

rule-based next-move selection

candidate ranking

WITHHOLD

composition transition

move-selection / realization separation

multi-turn state update

manual extraction

confirmation gating

basic composition contract

test coverage
```

Current pipeline:

```text
MANUAL STATE INPUT
        ↓
RULE-BASED CONTROLLER
        ↓
TEMPLATE REALIZER
        ↓
HUMAN RESPONSE
        ↓
MANUAL STATE UPDATE
        ↺
```

This is intentionally narrow.

It exists to expose control logic before introducing richer model inference.

---

# 2. Target AI-Backed Prototype

The next implementation should move toward:

```text
                        HUMAN INPUT
                             │
                             ▼
                    INPUT INTERPRETER
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
      OBSERVED HUMAN TEXT          CANDIDATE INFERENCES
              │                             │
              │                    CONFIRMATION GATE
              │                             │
              └──────────────┬──────────────┘
                             ▼
                  INTERACTION STATE
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       COGNITIVE      METACOGNITIVE   LINGUISTIC /
         STATE           PROCESS       SOCIOLINGUISTIC
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                     INTERACTION MODEL
                             │
                             ▼
                 METACOGNITIVE CONTROLLER
                             │
                             ▼
                  NEXT COGNITIVE OPERATION
                             │
                             ▼
                    SYSTEM MOVE POLICY
                             │
                             ▼
                    MOVE REALIZATION
                             │
                             ▼
                        HUMAN RESPONDS
                             │
                             ▼
                 STATE-CHANGE INFERENCE
                             │
                             └────────────↺
```

When the system transitions to composition:

```text
                  HUMAN JUDGMENT
                        │
                        ▼
                COMPOSITION HANDOFF
                        │
                        ▼
                  EVIDENCE ROUTER
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
         USER        MODEL       OPTIONAL
       EVIDENCE      PRIORS      RETRIEVAL
            │           │           │
            └───────────┼───────────┘
                        ▼
                RHETORICAL SITUATION
                        │
                        ▼
              SOCIOLINGUISTIC MODEL
                        │
                        ▼
                 GENRE / DOMAIN MODEL
                        │
                        ▼
                RHETORICAL COMPILER
                        │
                        ▼
            SEMANTIC / INTERACTIONAL CHECK
                        │
                        ▼
                 EXACT FINAL OUTPUT
```

---

# 3. Component Boundaries

The target prototype should keep major responsibilities separable.

Recommended components:

```text
extractor
metacognitive analyzer
evidence router
controller
move realizer
state updater
confirmation gate
rhetorical planner
linguistic analyzer
genre model
retrieval adapter
rhetorical compiler
drift checker
provenance tracker
```

These may initially share one underlying language model.

Architectural separation does not require one model per component.

The separation exists so the behavior can be tested independently.

---

# 4. Input Interpreter

The Input Interpreter receives raw human language.

Its job is to preserve:

```text
WHAT WAS ACTUALLY SAID
```

separately from:

```text
WHAT THE SYSTEM THINKS IT MEANS
```

Possible outputs:

```yaml
observed:
  raw_text: null

candidate_state:
  claims: []
  assumptions: []
  distinctions: []
  uncertainty: []
  unresolved_questions: []

candidate_metacognitive_events: []

candidate_linguistic_features: []

candidate_interaction_updates: []
```

Observed language should never be rewritten into inferred human belief without preserving the distinction.

---

# 5. Model-Assisted Extraction

A capable language model may be used to infer candidate state.

For example:

```text
HUMAN

"I don't know if it's actually the law that's bothering me."
```

Possible extraction:

```yaml
observed:
  "I don't know if it's actually the law that's bothering me."

candidate_uncertainty:
  content:
    "whether the moral quality of the law is the true explanatory variable"

  epistemic_status:
    system_inferred

  confidence:
    0.71

  requires_confirmation:
    true
```

The system may surface this as:

> "It sounds like you're questioning whether the law itself is the real variable. Is that right?"

rather than silently updating the human model.

---

# 6. Confirmation Policy

Not every inference requires interruption.

A mature system should distinguish:

```text
LOW-IMPACT INFERENCE

HIGH-IMPACT INFERENCE
```

Low-impact inference may be used provisionally.

Examples:

```text
message appears informal

artifact appears to be an email

user is asking for compression
```

High-impact inference should often require confirmation.

Examples:

```text
substantive belief

motive

identity

relationship interpretation

emotional state

major conceptual distinction

persistent personalization
```

The confirmation threshold itself should be testable.

---

# 7. Metacognitive Analyzer

The Metacognitive Analyzer estimates:

```text
WHAT COGNITIVE OPERATION JUST OCCURRED?

WHAT CHANGED?

WHICH INTERVENTION PRECEDED THE CHANGE?

WAS THAT CHANGE PRODUCTIVE FOR THIS TASK?
```

Candidate outputs:

```yaml
operation:
  identify_invariant

trigger:
  system_counterfactual

state_change:
  new_distinction

productivity:
  high

confidence:
  0.76
```

The analyzer should update current-task process evidence.

---

# 8. Dynamic Self-Prompting

The current process state should generate a control instruction for the next move.

Example:

```text
Current evidence:

- two productive revisions followed single-variable counterfactuals
- open-ended explanation produced elaboration but no state change
- direct system proposals have been rejected
- learner is currently reasoning at an abstract level

Controller instruction:

Use one counterfactual.
Preserve abstraction level.
Change one variable.
Do not name the likely distinction.
Ask what remains invariant.
```

This instruction may then be passed to the move generator.

This is a central feature of the target architecture.

---

# 9. Controller

The controller should choose:

```text
WHAT COGNITIVE OPERATION SHOULD REMAIN WITH THE HUMAN?
```

before choosing:

```text
WHAT SHOULD THE SYSTEM SAY?
```

Candidate controller output:

```yaml
target_cognitive_operation:
  identify_invariant

system_move:
  counterfactual

target:
  current_assumption_3

constraints:
  - change one variable
  - do not supply conclusion
  - preserve current abstraction level

expected_state_change:
  - new_distinction
  - claim_revision

substitution_risk:
  low

interactional_risk:
  low
```

---

# 10. Move Realizer

The realizer converts controller policy into language.

It should receive:

```text
selected move

target operation

cognitive state

metacognitive state

linguistic / sociolinguistic state

interaction constraints
```

Example:

```text
same policy:
COUNTERFACTUAL
```

may be realized differently as:

```text
"Would that still hold if X changed?"
```

or:

```text
"Okay, hold everything else constant—if X flips, does the judgment change?"
```

or:

```text
"Would the interpretation remain defensible if X were not the case?"
```

The move stays stable.

The language changes.

---

# 11. Linguistic Analyzer

The linguistic analyzer should infer candidate features from current and prior language evidence.

Possible outputs:

```yaml
lexical:
  technical_density: high
  preferred_terms:
    - "controller"
    - "architecture"

syntax:
  compression: high
  fragmentation: moderate

cadence:
  conceptual_bursting: high

pragmatics:
  directness: high
  humor: affiliative

register:
  current: conversational_technical

confidence:
  0.82
```

These features should remain evidence-scoped.

---

# 12. Speech / Text Evidence Adapter

A future implementation may accept:

```text
current chat

uploaded writing samples

emails

texts

essays

transcripts

speech-to-text

prior interaction traces
```

The adapter should contextualize each sample.

Example:

```yaml
sample:
  medium: text_message
  audience: close_friend
  domain: personal
  date: null
```

Features should not be assumed transferable across all contexts.

---

# 13. Speech Features

If speech input becomes available, candidate features may include:

```text
speech rate

pause duration

repair

hesitation

prosody

emphasis

pitch movement

overlap

laughter

turn length
```

These should be used primarily for linguistic and interactional interpretation.

Psychological inference should remain bounded.

---

# 14. Evidence Router

The Evidence Router determines whether more information is required.

Possible decisions:

```text
NO_EXTERNAL_EVIDENCE

USE_CURRENT_INTERACTION

USE_USER_LANGUAGE_SAMPLE

USE_REASONING_HISTORY

USE_DOMAIN_KNOWLEDGE

USE_MODEL_PRIOR

VERIFY_FACT

RETRIEVE_PRIMARY_SOURCE

CHECK_CURRENT_TERMINOLOGY

CHECK_GENRE_CONVENTION

CHECK_CURRENT_IDIOMATIC_USE

BROAD_RESEARCH
```

The router should prefer the minimum evidence required to change the decision.

---

# 15. Base-Model Knowledge

The model may use pretrained knowledge for:

```text
grammar

rhetoric

idiom

common genre conventions

general discourse norms

disciplinary terminology

common argument structures
```

This should be treated as general prior knowledge.

It should not be treated as person-specific evidence.

---

# 16. Retrieval Adapter

The retrieval adapter may connect to:

```text
web search

academic literature search

institutional documentation

technical documentation

domain corpora

current public context

linguistic references
```

The adapter should return evidence objects with:

```text
source

date

claim

scope

quality

freshness

permissions
```

---

# 17. Retrieval for Language

Current retrieval may be useful for:

```text
rapidly changing slang

meme language

platform conventions

professional terminology

current discourse-community language

idiomatic interpretation

emoji pragmatics
```

A current external pattern should remain weaker evidence about a specific person's language than that person's actual language.

---

# 18. Retrieval for Reasoning

Engine 1 may request external evidence when the human lacks factual input required for judgment.

Example:

```text
human:
"I think this happened after the policy changed."

controller:
causal reasoning is blocked by chronology

retrieval:
verify chronology

system:
provide dates without interpretation

human:
evaluate causal claim
```

The system provides information.

The human performs the judgment.

---

# 19. Composition Handoff

When Engine 1 ends, it should produce a structured handoff.

Example:

```yaml
human_judgment:

  claims:
    - null

  distinctions:
    - null

  warrants:
    - null

  uncertainty:
    - null

  rejected_framings:
    - null

provenance:
  conceptual: []
  metacognitive: []

rhetorical_goal:
  null
```

Engine 2 should not need to infer the entire judgment again from raw chat history.

---

# 20. Rhetorical Planner

The rhetorical planner builds a composition contract.

Inputs:

```text
human judgment

audience

exigence

purpose

ethos

pathos

logos

kairos

constraints

available means

interaction state

genre

evidence
```

Output:

```yaml
composition_contract:

  semantic_invariants: []

  purpose: null

  audience: null

  rhetorical_sequence: []

  evidence_required: []

  interactional_constraints: []

  linguistic_constraints: []

  genre_constraints: []

  prohibited_additions: []
```

---

# 21. Genre Model

The genre model supplies conventions for artifacts such as:

```text
text

email

essay

discussion post

memo

technical critique

proposal

speech

feedback

report

boundary message
```

It should know:

```text
structure

expected evidence

degree of explicitness

opening

closing

citation expectations

argument sequence

register
```

Genre conventions are evidence, not immutable laws.

---

# 22. Domain Model

Domain-specific adapters may define:

```text
walking rules

evidence norms

argument forms

terminology

genre expectations

epistemic operations
```

Example:

```yaml
domain:
  literary_analysis

walking_rules:
  - test_textual_evidence
  - consider_counterreading
  - preserve_ambiguity

genre_expectations:
  - interpretive_claim
  - evidence
  - analysis
```

---

# 23. Rhetorical Compiler

The compiler should integrate:

```text
HUMAN JUDGMENT

RHETORICAL SITUATION

INTERACTION MODEL

LINGUISTIC MODEL

USER LANGUAGE EVIDENCE

GENRE MODEL

DOMAIN MODEL

EXTERNAL EVIDENCE
```

and produce one strong final realization.

Default behavior should not necessarily be:

```text
HERE ARE FIVE OPTIONS
```

If the evidence sufficiently determines one solution, return the strongest justified output.

---

# 24. Final Output Object

A mature system may return:

```yaml
artifact:

  text: null

  purpose: null

  audience: null

  conceptual_provenance: []

  metacognitive_provenance: []

  evidentiary_provenance: []

  linguistic_provenance: []

  semantic_drift_flags: []

  interactional_drift_flags: []

  confidence: null
```

The user-facing interface may display only the final text unless trace information is requested.

---

# 25. Semantic Drift Checker

The checker should compare final output against the composition contract.

Questions include:

```text
Did the system add a factual claim?

Did it add motive?

Did it increase certainty?

Did it remove important uncertainty?

Did it add commitment?

Did it collapse a distinction?

Did it change the human's stance?

Did it introduce a stronger emotion?
```

Flagged output should be regenerated or surfaced for review.

---

# 26. Interactional Drift Checker

The system should also ask:

```text
Did an invitation become a demand?

Did affection become explanation?

Did a boundary become punishment?

Did collegial critique become status challenge?

Did humor create unearned intimacy?

Did helpful specificity create surveillance signal?
```

This requires Model 4, not semantic similarity alone.

---

# 27. Speaker-Authenticity Checker

Candidate output should be compared against relevant language evidence.

Possible checks:

```text
register mismatch

lexical mismatch

uncharacteristic slang

uncharacteristic sentimentality

excessive formality

cadence mismatch

humor mismatch

punctuation mismatch

directness mismatch
```

Mismatch should not automatically block the draft.

It should lower confidence or trigger another realization.

---

# 28. Audience-Fit Checker

Candidate output should also be evaluated against:

```text
audience knowledge

role

power

shared context

discourse norms

genre expectations

interaction history

response latitude
```

Speaker authenticity alone is not sufficient.

---

# 29. Provenance Tracker

The provenance tracker should operate across the full pipeline.

At minimum:

```text
CONCEPTUAL PROVENANCE

METACOGNITIVE PROVENANCE

EVIDENTIARY PROVENANCE

ORGANIZATIONAL PROVENANCE

LINGUISTIC PROVENANCE
```

Example:

```yaml
claim_4:

  conceptual:
    human_originated

  metacognitive:
    system_elicited_human_performed

  evidentiary:
    retrieved_primary_source

  organizational:
    jointly_developed

  linguistic:
    system_transposed
```

---

# 30. Metacognitive Analytics

The trace may support optional descriptive analytics.

Examples:

```text
counterfactual interventions:
4

productive revisions after counterfactuals:
3

open-ended prompts:
3

productive revisions after open-ended prompts:
0

system proposals:
8

accepted unchanged:
1

human revised:
4

human rejected:
2

unused:
1
```

This should describe behavior.

It should not automatically become a fixed user type.

---

# 31. Semantic Contribution Analysis

A future system may compare final propositions to prior trace objects.

Possible methods include:

```text
semantic similarity

entailment

proposition matching

trace alignment

human confirmation
```

This may help distinguish:

```text
same idea / new wording
```

from:

```text
new idea
```

Automated semantic matching should remain uncertainty-aware.

---

# 32. AI / Human Contribution Reporting

The system should avoid simplistic token-based authorship percentages.

Prefer multidimensional reporting.

Example:

```text
CONCEPTUAL

6 final propositions

4 human-originated

1 system-proposed / human-revised

1 external-evidence-derived / human-judged

METACOGNITIVE

3 major revisions followed system counterfactuals

2 distinctions were human-self-initiated

LINGUISTIC

final wording primarily system-transposed

ORGANIZATIONAL

jointly developed
```

If a percentage is ever shown, the denominator and category must be explicit.

---

# 33. Model Options

The architecture should remain model-agnostic.

Possible implementations may use:

```text
one frontier LLM for all semantic tasks

multiple specialized models

small local classifiers

embedding models

rule-based policy

retrieval-augmented generation

hybrid local / remote inference
```

The architecture should be testable independent of model vendor.

---

# 34. Local Inference Candidates

Functions that may be candidates for local processing include:

```text
idiolect feature extraction

recent-state summarization

operation classification

semantic similarity

provenance matching

basic language feature statistics

reasoning-history updates

privacy filtering
```

This should be tested empirically.

---

# 35. Remote / Strong-Model Candidates

Functions that may initially require a stronger model include:

```text
complex state extraction

subtle metacognitive inference

candidate intervention generation

rhetorical planning

high-quality rhetorical realization

semantic drift evaluation

interactional drift evaluation
```

These boundaries may move as smaller models improve.

---

# 36. Retrieval Interfaces

The architecture should permit pluggable retrieval.

Conceptually:

```python
class EvidenceProvider:

    def retrieve(self, query, purpose, context):
        ...
```

Possible providers:

```text
web

academic literature

institutional sources

user corpus

domain corpus

local files

conversation history
```

Each result should retain source metadata.

---

# 37. Privacy Boundary

Sensitive personalization should be minimized.

Possible design:

```text
LOCAL

raw language samples
relationship-specific data
idiolect features
recent reasoning state

REMOTE

abstracted task state
necessary context
retrieval query
generation request
```

This is one possible architecture, not a validated requirement.

---

# 38. Raw Data Versus Abstracted State

The system should explicitly test whether:

```text
abstracted state
```

can replace:

```text
large raw history
```

for useful personalization.

If yes, retain less raw data.

If no, quantify the performance/privacy tradeoff.

---

# 39. Failure Isolation

Component separation should make failures diagnosable.

Example:

```text
bad final message
```

may be caused by:

```text
wrong cognitive state

wrong metacognitive inference

bad audience model

bad evidence

bad rhetorical plan

bad linguistic realization

semantic drift

interactional drift
```

A monolithic prompt makes these difficult to distinguish.

---

# 40. Minimal Next Implementation

The next actual AI-backed build should not implement everything in this file.

Recommended first increment:

```text
1. LLM-assisted state extraction

2. candidate metacognitive operation inference

3. confirmation gate

4. adaptive controller instruction

5. LLM move realization

6. trace update

7. simple composition handoff

8. LLM rhetorical realization

9. semantic drift check
```

Leave for later:

```text
speech prosody

large user corpora

cross-domain reasoning history

advanced web retrieval

local-model routing

complex interactional policy

automated contribution scoring
```

---

# 41. First Useful Demo

A strong next demo would support:

```text
USER

"I need to tell someone something, but I can't figure out
what I'm actually trying to say."

SYSTEM

asks a small number of adaptive questions

USER

revises / rejects / distinguishes

SYSTEM

detects stabilized human judgment

SYSTEM

asks only missing high-value audience/context questions

SYSTEM

optionally retrieves one necessary fact or convention

SYSTEM

returns exact final message
```

alongside an optional debug panel showing:

```text
current claim

current uncertainty

metacognitive control signal

selected move

provenance

composition contract
```

This would demonstrate both the visible user experience and the inspectable research architecture.

---

# 42. Educational Demo

A parallel educational demo could use:

```text
short literary interpretation
```

with:

```text
initial claim

adaptive challenge

human revision

disciplinary walking rules

composition handoff

final essay paragraph
```

followed by:

```text
independent explanation

new counterexample

provenance report
```

This would test whether the system can produce strong final prose while preserving learner accountability.

---

# 43. Evaluation Baselines

Any serious prototype should eventually compare against:

```text
GENERAL HELPFUL LLM

GENERIC SOCRATIC PROMPT

STATIC USER-PERSONALIZED LLM

DELIBERATION ROOM
```

Possible ablations:

```text
without metacognitive process model

without linguistic model

without interaction model

without retrieval

without confirmation gate

without provenance
```

---

# 44. Core Engineering Invariants

The implementation should preserve:

```text
OBSERVATION
≠
INFERENCE

SYSTEM ELICITED
≠
SYSTEM ORIGINATED

WORD ORIGIN
≠
IDEA ORIGIN

UNDERSTAND A FORM
≠
PERMISSION TO PERFORM IT

AVAILABLE INFORMATION
≠
INFORMATION THAT SHOULD BE DISCLOSED

GENERATION
≠
DELIBERATION

RHETORICAL QUALITY
≠
MANIPULATION SUCCESS

PERSONALIZATION
≠
MAXIMUM DATA RETENTION
```

These should eventually become explicit tests where possible.

---

# 45. Target Experience

The internal system may be complex.

The external experience should not be.

The intended user-facing interaction is:

```text
USER
brings an unfinished problem

SYSTEM
asks unusually well-chosen questions

USER
recognizes / rejects / revises

SYSTEM
adapts

USER
arrives at a judgment they can account for

SYSTEM
researches only what materially helps

SYSTEM
compiles the judgment for the actual rhetorical situation

USER
receives exactly what they needed to write or say
```

The user should not need to understand:

```text
state machines
metacognitive provenance
rhetorical compilation
sociolinguistic inference
evidence routing
```

to benefit from them.

---

# 46. Final Target

The intended architecture can be compressed to:

```text
UNDERSTAND
how this human is thinking

ELICIT
the next useful cognitive act

PRESERVE
who developed the judgment

RESEARCH
only what materially helps

MODEL
what language means and does here

COMPILE
the judgment for the actual rhetorical situation

CHECK
for semantic and interactional drift

OUTPUT
the exact utterance
```

Or, more compactly:

> **Help the human get somewhere worth saying, then say it exactly right without pretending the system got there alone.**
