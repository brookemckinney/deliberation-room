# Privacy Threat Model

Deliberation Room is designed around a data-minimization hypothesis:

> **A system that elicits rather than replaces cognition may require less general-purpose generative capability and less raw personal data, making local/on-device inference and data-minimized personalization more feasible.**

This is a hypothesis.

It is not a claim that the architecture is inherently private.

In fact, Deliberation Room introduces a distinct class of privacy risk because its structured state may include highly sensitive representations of:

- beliefs;
- uncertainty;
- reasoning patterns;
- relational history;
- discourse practices;
- power relationships;
- communication preferences;
- conceptual vulnerabilities;
- and interaction-specific meanings.

A compressed representation can still be sensitive.

In some cases, it may be **more revealing than the raw language from which it was derived**.

---

# 1. Threat Model Scope

This document focuses on privacy and misuse risks created by:

```text
COGNITIVE STATE
PERSON / REASONING STATE
LINGUISTIC / SOCIOLINGUISTIC STATE
INTERACTION STATE
DELIBERATION TRACE
COGNITIVE PROVENANCE
METACOGNITIVE FEEDBACK
PERSISTENT PERSONALIZATION
```

The threat model does not assume malicious intent from the system.

Risk can arise from:

- overcollection;
- over-inference;
- retention;
- incorrect inference;
- unauthorized access;
- secondary use;
- invisible personalization;
- institutional misuse;
- or well-intentioned but excessive modeling.

---

# 2. Privacy Objective

The architectural goal is not:

```text
KNOW AS MUCH AS POSSIBLE ABOUT THE HUMAN
```

It is:

```text
REPRESENT ONLY WHAT IS NECESSARY
TO SELECT A USEFUL NEXT MOVE
```

This creates a design principle:

> **Personalization should earn its data.**

Information should be represented only when it materially improves:

- interpretation;
- next-move selection;
- semantic preservation;
- interactional appropriateness;
- provenance;
- or explicit user-requested continuity.

---

# 3. Data Categories

Different state elements carry different levels of sensitivity.

## Cognitive State Data

May include:

- claims;
- beliefs;
- assumptions;
- uncertainty;
- contradictions;
- misconceptions;
- unresolved questions;
- confidence;
- decision structure.

Possible risk:

A structured record of uncertainty or belief can reveal intellectual, professional, relational, or ideological vulnerability.

---

## Person / Reasoning Data

May include:

- productive reasoning strategies;
- challenge preferences;
- abstraction tolerance;
- revision patterns;
- evidence-use patterns;
- metacognitive observations;
- domain expertise.

Possible risk:

These representations may become de facto psychological or ability profiles even when that was not their intended purpose.

---

## Linguistic / Sociolinguistic Data

May include:

- idiolect;
- dialect;
- shared vocabulary;
- relational language history;
- discourse communities;
- pragmatic conventions;
- role language;
- humor patterns;
- code-switching;
- stance.

Possible risk:

These features may indirectly reveal:

- geography;
- profession;
- community affiliation;
- age positioning;
- social identity;
- relationship status;
- or other sensitive characteristics.

The architecture should not assume that avoiding explicit identity labels eliminates identity-related privacy risk.

---

## Interaction Data

May include:

- relationships;
- power asymmetries;
- authority;
- belonging;
- trust;
- disclosure pressure;
- relational distance;
- conflict history;
- ability to disengage;
- institutional role.

Possible risk:

This data may reveal sensitive relational or organizational dynamics.

---

## Provenance Data

May include:

- what the human originated;
- what they rejected;
- what they revised;
- what they did not understand;
- what uncertainty remained;
- where system assistance entered the process.

Possible risk:

A provenance trace can reveal intellectual dependence, uncertainty, or vulnerability in ways that a polished final artifact does not.

---

# 4. Threat: Raw-History Accumulation

## Risk

Personalization systems often improve continuity by storing increasing quantities of conversation history.

Over time, this can create:

```text
large raw personal archive
+
broad cross-context inference
+
difficult deletion
+
unclear secondary use
```

## Architectural Response

Investigate whether raw history can be replaced by:

- task-level structured state;
- domain-level summaries;
- user-approved persistent representations;
- local storage;
- ephemeral state;
- selective provenance;
- and explicit expiration.

A design target is:

```text
RAW INTERACTION
        ↓
MINIMAL USEFUL STATE
        ↓
DISCARD WHAT IS NO LONGER NEEDED
```

---

# 5. Threat: Structured-State Sensitivity

## Risk

Data minimization can create a false sense of safety.

Consider:

```yaml
reasoning_pattern:
  strategy: direct_counterexample
  effect: productive

interaction_model:
  relationship:
    power_asymmetry: high
  disclosure_pressure: high

cognitive_state:
  unresolved_uncertainty:
    - "whether colleague can be trusted"
```

This is concise.

It is also highly revealing.

## Architectural Response

Structured state should be treated as sensitive personal information.

Data minimization should reduce:

```text
volume
```

without pretending it eliminates:

```text
sensitivity
```

---

# 6. Threat: Unnecessary Identity Inference

## Risk

Sociolinguistic, behavioral, and interactional evidence may correlate with demographic or identity categories.

A system could infer characteristics that are irrelevant to the task.

For example:

```text
Observed:
User uses a particular discourse convention.

Bad inference:
Therefore the user belongs to demographic category X.

Useful representation:
The form appears to function as mitigation in this interaction.
```

## Architectural Response

Prefer:

```text
INTERACTIONALLY RELEVANT REPRESENTATION
```

over:

```text
IDENTITY EXPLANATION
```

when the former is sufficient.

The architecture should ask:

> **Does knowing this category actually change the next move in a justified way?**

If not, do not infer or retain it.

---

# 7. Threat: Sensitive Attribute Proxying

## Risk

Even if the system never explicitly stores:

```text
identity = X
```

other variables may operate as proxies.

For example:

- linguistic forms;
- geography;
- institutional role;
- community vocabulary;
- family references;
- religious discourse;
- political terminology;
- or professional affiliation.

## Architectural Response

Sensitive inference risk should be evaluated at the **representation level**, not merely by checking whether protected labels appear explicitly.

A privacy audit should ask:

> What could reasonably be reconstructed from the state?

not only:

> What fields did we intentionally store?

---

# 8. Threat: False Psychological Certainty

## Risk

Repeated interaction may tempt the system to transform provisional observations into stable psychological claims.

For example:

```text
Observed:
Direct challenge was useful three times.

Risky persistent inference:
This person needs confrontation to think clearly.
```

or:

```text
Observed:
User revises language repeatedly.

Risky inference:
User lacks confidence.
```

These claims may be inaccurate and invasive.

## Architectural Response

Preserve:

```text
context
confidence
source
generalization limits
```

Represent:

```text
counterexample productive in argument testing
```

rather than:

```text
user is a counterexample thinker
```

unless broader evidence and human recognition justify the stronger claim.

---

# 9. Threat: Hidden Profiling

## Risk

A system may accumulate a detailed model of the human without the human knowing what has been inferred.

This can include:

- reasoning habits;
- communication patterns;
- conflict style;
- vulnerability;
- relational dynamics;
- confidence;
- expertise;
- or social positioning.

## Architectural Response

Important persistent state should eventually be inspectable.

A mature implementation should investigate user interfaces such as:

```text
THE SYSTEM CURRENTLY BELIEVES:

- direct counterexamples are often productive for you in argument testing
- this phrase has a locally established meaning
- this relationship appears to involve evaluation authority
```

with controls such as:

```text
CONFIRM
REVISE
LIMIT TO THIS CONTEXT
MARK TEMPORARY
DELETE
```

Personalization should be negotiable rather than invisible.

---

# 10. Threat: Persistence Creep

## Risk

A useful task-level inference may silently become:

```text
session-level
→ domain-level
→ cross-domain
→ permanent
```

without sufficient evidence or user awareness.

## Architectural Response

Represent persistence scope explicitly.

Possible levels:

```text
TURN
SESSION
TASK
DOMAIN
CROSS-DOMAIN
PERSISTENT
```

The default should favor the narrowest useful scope.

Broader persistence should require stronger justification.

---

# 11. Threat: Context Collapse

## Risk

A representation that is valid in one relationship or task may become harmful if reused elsewhere.

Example:

```text
"ironic teasing is permitted"
```

may be valid:

```text
with close friend
```

and deeply inappropriate:

```text
with supervisor
```

Likewise:

```text
direct contradiction is productive
```

may apply:

```text
during argument testing
```

but not:

```text
during vulnerable personal disclosure
```

## Architectural Response

Personalization should preserve context.

Do not store:

```text
likes teasing
```

when the evidence actually supports:

```text
affiliative teasing has been interactionally successful
with participant X in informal low-stakes contexts
```

---

# 12. Threat: Relational Surveillance

## Risk

The Interaction Model may encourage collection of detailed information about third parties.

For example:

- relationship history;
- conflict patterns;
- authority;
- trust;
- private disclosures;
- another person's likely motives.

This can turn deliberation support into indirect surveillance of people who never interacted with the system.

## Architectural Response

Represent only what is necessary to model the user's interaction.

Prefer:

```text
user experiences high uncertainty about recipient response
```

over speculative third-party profiles such as:

```text
recipient has avoidant attachment tendencies
```

unless the task explicitly and appropriately requires such information.

---

# 13. Threat: Model-of-Others Overreach

## Risk

The system may treat the user's account of another person as sufficient to construct an overly confident model of that person.

This violates the architecture's own epistemic principles.

## Architectural Response

Distinguish:

```text
USER'S REPRESENTATION OF OTHER PERSON
```

from:

```text
FACT ABOUT OTHER PERSON
```

The system may model plausible receptions or perspectives.

It should not pretend to know unavailable minds.

---

# 14. Threat: Linguistic Mimicry

## Risk

A system that understands idiolect, dialect, register, humor, or community language may use that knowledge to manufacture artificial similarity or intimacy.

This could increase:

- trust;
- persuasion;
- disclosure;
- or compliance

without genuine relational basis.

## Architectural Response

Separate:

```text
UNDERSTANDING A COMMUNICATIVE CONVENTION
```

from:

```text
PERMISSION TO PERFORM IT
```

The system should optimize for pragmatic fit, not identity imitation.

---

# 15. Threat: Relational Manipulation

## Risk

The Interaction Model explicitly represents:

- face;
- belonging;
- trust;
- power;
- social risk;
- response latitude;
- and relational distance.

Those same variables could be used to optimize persuasion.

For example:

```text
Which wording makes the human most likely to agree?
```

is technically compatible with the data.

It is not compatible with the intended architecture.

## Architectural Response

The optimization target must remain:

```text
HUMAN COGNITIVE AGENCY
```

not:

```text
COMPLIANCE
ENGAGEMENT
CONVERSION
DISCLOSURE
DEPENDENCE
```

Relevant evaluation should explicitly test for this failure mode.

---

# 16. Threat: Engagement Optimization

## Risk

A system may learn that certain moves produce:

- more conversation;
- stronger emotional response;
- more disclosure;
- more frequent return;
- or greater dependence.

These can be mistaken for successful personalization.

## Architectural Response

Conversation continuation should not be a primary objective.

A successful interaction may end quickly because the human can now continue independently.

Potential success signal:

```text
SYSTEM INTERVENTION
        ↓
HUMAN GAINS CLARITY
        ↓
SYSTEM BECOMES LESS NECESSARY
```

---

# 17. Threat: Provenance Surveillance

## Risk

Cognitive provenance could become a new form of learner or employee monitoring.

A system designed to preserve evidence of reasoning might be repurposed to measure:

- compliance;
- productivity;
- speed;
- uncertainty;
- disagreement;
- or "acceptable" thought processes.

## Architectural Response

Cognitive provenance should not imply continuous behavioral surveillance.

Prefer meaningful cognitive events such as:

```text
claim introduced
claim revised
counterexample considered
uncertainty retained
```

over:

```text
keystrokes
browser activity
camera data
screen monitoring
```

The architecture should also separate:

```text
supporting intellectual accountability
```

from:

```text
policing thought process
```

---

# 18. Threat: Institutional Misuse

## Risk

Schools, employers, insurers, platforms, or institutions could interpret trace data in ways that exceed the original purpose.

Examples:

```text
employee frequently revises decisions
→ labeled indecisive

student frequently accepts AI proposals
→ automatically penalized

user uncertainty
→ interpreted as lack of competence
```

## Architectural Response

Purpose limitation should be explicit.

Provenance data should not automatically become:

- performance data;
- disciplinary data;
- hiring data;
- grading data;
- or psychological assessment data.

Any such use would require separate justification and governance.

---

# 19. Threat: False Precision in Contribution Scores

## Risk

A system may produce attractive but unsupported outputs such as:

```text
87% HUMAN
13% AI
```

These numbers can appear authoritative even when the underlying classification is ambiguous.

## Architectural Response

Prefer descriptive provenance:

```text
4 of 5 final substantive claims were human-originated.

1 claim was system-proposed and materially revised by the human.

Final sentence-level wording was primarily system-transposed.
```

Do not convert ambiguous conceptual contribution into precise percentages without validated methodology.

---

# 20. Threat: Sensitive Metacognitive Feedback

## Risk

Metacognitive feedback can feel diagnostic.

For example:

> "You struggle to generate warrants."

may be interpreted as a stable personal deficit.

## Architectural Response

Prefer bounded observations:

> "In this task, claims emerged more readily than warrants."

Metacognitive feedback should remain:

```text
CONTEXTUAL
PROVISIONAL
CORRIGIBLE
```

and should not imply clinical, cognitive, or personality diagnosis.

---

# 21. Threat: Reconstruction

## Risk

Even if raw transcripts are deleted, structured state may allow substantial reconstruction of sensitive interactions.

For example:

```text
relationship = romantic
power = low
uncertainty = commitment
shared term = "San Diego"
central concern = shared future
```

may reveal substantial context.

## Architectural Response

Privacy evaluation should include:

> **What can an attacker or institution reconstruct from structured state alone?**

Possible mitigation includes:

- reducing specificity;
- shortening persistence;
- local storage;
- removing relational identifiers;
- separating state stores;
- or storing higher-level abstractions.

---

# 22. Threat: Linkability Across Contexts

## Risk

Even harmless-looking state fragments can become sensitive when linked across:

- sessions;
- tasks;
- applications;
- devices;
- relationships;
- or domains.

## Architectural Response

Avoid universal persistent identifiers when not required.

Investigate separation such as:

```text
TASK STATE

DOMAIN STATE

RELATIONSHIP-SPECIFIC STATE

GLOBAL STATE
```

with deliberate boundaries between them.

---

# 23. Threat: Over-Persistence of Local Meaning

## Risk

A shared phrase may be useful within one relationship but inappropriate or revealing elsewhere.

Example:

```text
local phrase:
"walking the orb"
```

If exposed to unrelated contexts, it may:

- reveal prior conversations;
- create inappropriate intimacy;
- or distort interpretation.

## Architectural Response

Relational language history should be scoped to the relationship or discourse environment in which it was established.

---

# 24. Threat: Data Leakage to Composition Models

## Risk

Even if the controller operates locally, the composition stage may send the full conversation to a remote large model.

That would undermine much of the privacy benefit.

## Architectural Response

Investigate a minimized handoff:

```text
RAW DELIBERATION
        ↓
LOCAL STATE ABSTRACTION
        ↓
COMPOSITION CONTRACT
        ↓
REMOTE COMPOSITION
```

The remote model might receive only:

- semantic invariants;
- audience;
- rhetorical constraints;
- relevant facts;
- and required style parameters.

Whether this preserves quality is an empirical question.

---

# 25. Threat: External Tool Leakage

## Risk

Future implementations may use:

- retrieval;
- search;
- external databases;
- composition APIs;
- educational platforms;
- or other tools.

Sensitive state could be unnecessarily transmitted to those systems.

## Architectural Response

Tool calls should receive the **minimum required state**, not the full internal representation.

The system should distinguish:

```text
what the controller knows
```

from:

```text
what this external tool needs
```

---

# 26. Threat: Incorrect State Persistence

## Risk

Incorrect system inferences can become more harmful when stored.

For example:

```text
user prefers direct confrontation
```

may have been inferred from one unusual interaction.

If retained, the system may repeatedly act on the error.

## Architectural Response

Persistence should depend on:

- confidence;
- repetition;
- context;
- user correction;
- and actual predictive value.

Low-confidence inferences should generally expire quickly.

---

# 27. Threat: Self-Fulfilling Personalization

## Risk

A system may repeatedly choose interventions based on its current model, generating the very evidence that appears to confirm the model.

Example:

```text
system believes user responds to analogy
        ↓
system repeatedly uses analogy
        ↓
user responds within analogy
        ↓
system concludes analogy preference is confirmed
```

Alternative strategies were never tested.

## Architectural Response

The next-move policy may require limited low-risk exploration.

Persistent personalization should preserve:

```text
evidence diversity
```

not just repeated confirmation.

---

# 28. Threat: User Lock-In Through Shared Language

## Risk

A system that develops rich shared vocabulary can become unusually cognitively convenient.

This may increase dependence.

The user may feel:

> "No one else understands what I mean this quickly."

That convenience is valuable.

It can also create lock-in.

## Architectural Response

Where feasible, important conceptual shorthand should be:

- inspectable;
- exportable;
- explainable;
- and translatable into ordinary language.

A useful system should not make the user's own conceptual model inaccessible without the system.

---

# 29. Threat: Local Model ≠ Private Model

## Risk

Local inference reduces some exposure.

It does not solve:

- insecure storage;
- device compromise;
- overcollection;
- harmful inference;
- inappropriate persistence;
- or institutional access.

## Architectural Response

The project should distinguish:

```text
LOCAL
```

from:

```text
PRIVATE
```

Local execution is one potential privacy mechanism.

It is not a complete privacy architecture.

---

# 30. Threat: Encryption Is Not Data Minimization

## Risk

Securely storing excessive data is still excessive data collection.

## Architectural Response

Privacy strategy should distinguish:

```text
DATA SECURITY
```

from:

```text
DATA MINIMIZATION
```

The strongest protected database can still contain information that never needed to exist.

---

# 31. Threat: De-Identification Failure

## Risk

Removing names may not make interaction-state data anonymous.

Unique combinations of:

- profession;
- relationship structure;
- local vocabulary;
- reasoning patterns;
- institution;
- and event history

may be identifying.

## Architectural Response

Do not assume structured state is anonymous simply because direct identifiers are absent.

Re-identification risk should be evaluated separately.

---

# 32. Data-Minimization Principles

A privacy-preserving implementation should investigate principles such as:

### Purpose limitation

Represent information for a specific interaction function.

### Minimal scope

Store the narrowest context in which the representation is useful.

### Minimal duration

Retain information only as long as required.

### Explicit epistemic status

Store whether information is observed, inferred, or hypothesized.

### Corrigibility

Allow important state to be corrected.

### Inspectability

Allow users to see meaningful persistent representations.

### Deletion

Allow persistent state to be removed.

### Separation

Avoid combining unrelated domains unless necessary.

### Local-first processing

Perform sensitive inference locally when feasible.

### Selective disclosure

Provide downstream models or tools only the state they require.

---

# 33. Candidate Persistence Policy

A future implementation might use:

```text
TURN-LEVEL STATE
default: ephemeral

SESSION-LEVEL STATE
default: delete after session

TASK-LEVEL STATE
retain only if task requires continuation

DOMAIN-LEVEL STATE
requires repeated evidence

RELATIONSHIP-SPECIFIC STATE
explicit scope and higher sensitivity

CROSS-DOMAIN STATE
high threshold

PERSISTENT STATE
user-visible and corrigible
```

This is a design proposal, not a finished policy.

---

# 34. Candidate Storage Tiers

Possible architecture:

```text
TIER 0
No persistence

TIER 1
Ephemeral interaction state

TIER 2
Task state

TIER 3
User-approved reasoning preferences

TIER 4
Relationship-specific local semantic history
```

Different applications may permit different maximum tiers.

For example, an educational deployment may prohibit relationship-specific persistent state entirely.

---

# 35. Model Separation

The four-model architecture may support privacy through separation.

Instead of one universal profile:

```text
GLOBAL USER MODEL
```

maintain scoped representations such as:

```text
CURRENT TASK COGNITIVE STATE

RHETORIC DOMAIN REASONING STATE

CURRENT RELATIONSHIP INTERACTION STATE

SESSION-LOCAL LINGUISTIC STATE
```

This may reduce unnecessary cross-context leakage.

Whether such separation materially improves privacy should be tested.

---

# 36. User Review

A mature system may allow users to inspect persistent state.

Example:

```text
Saved reasoning observations

✓ Counterexamples often productive in argument testing.
  Scope: rhetoric
  Confidence: moderate

✓ "walking the orb" is shared shorthand for examining a model
  from multiple perspectives.
  Scope: this workspace

? User prefers direct challenge.
  Scope: general
  Confidence: low
```

The user could:

```text
CONFIRM
REVISE
LIMIT SCOPE
MARK TEMPORARY
DELETE
```

This makes personalization more legible.

---

# 37. Selective Forgetting

The architecture should support deletion at the level of meaningful representations.

For example:

```text
delete raw transcript
retain final task state
```

or:

```text
delete relationship history
retain general reasoning preference
```

or:

```text
delete all persistent personalization
```

The technical feasibility of selective deletion will depend on implementation.

It should nonetheless be considered an architectural requirement rather than an afterthought.

---

# 38. Privacy and Provenance Tension

Cognitive provenance benefits from retaining reasoning history.

Privacy benefits from deleting unnecessary history.

These objectives can conflict.

A central research question is:

> **What is the minimum trace sufficient for intellectual accountability?**

Possible compressed provenance:

```text
claim introduced by human
counterexample presented
claim revised by human
distinction introduced by human
final claim stabilized
```

rather than full transcript retention.

This tradeoff should be studied explicitly.

---

# 39. Privacy and Metacognition Tension

Metacognitive feedback improves with longitudinal evidence.

Longitudinal evidence increases profiling risk.

Possible compromise:

```text
TASK-LEVEL METACOGNITIVE SUMMARY
        ↓
HUMAN CHOOSES WHETHER TO PROMOTE
        ↓
PERSISTENT REASONING REPRESENTATION
```

The system should not automatically convert every task pattern into long-term personalization.

---

# 40. Privacy and Sociolinguistics Tension

Sociolinguistic interpretation may improve interaction substantially.

It also creates heightened risk of:

- identity inference;
- stereotyping;
- community inference;
- intimacy simulation;
- and context collapse.

Therefore evaluation must ask not merely:

> Did sociolinguistic modeling improve interaction?

but:

> **Did the benefit justify the sensitivity of the representation required?**

---

# 41. Threat Severity

Threats should eventually be evaluated across dimensions such as:

```text
LIKELIHOOD
SENSITIVITY
REVERSIBILITY
SCOPE
USER VISIBILITY
SECONDARY-USE RISK
RECONSTRUCTION RISK
```

Not every privacy failure has the same consequence.

---

# 42. Privacy Evaluation Conditions

Possible comparison conditions include:

```text
FULL RAW HISTORY

RAW HISTORY + SECURITY CONTROLS

SUMMARIZED HISTORY

STRUCTURED STATE

LOCAL STRUCTURED STATE

EPHEMERAL STRUCTURED STATE

NO PERSONALIZATION
```

Measure:

- next-move quality;
- user correction;
- task success;
- privacy exposure;
- reconstruction risk;
- storage volume;
- and user preference.

---

# 43. Privacy Success Criteria

A privacy-oriented implementation should aim for:

```text
LESS RAW DATA
LESS UNNECESSARY INFERENCE
LESS CROSS-CONTEXT LINKAGE
MORE LOCAL PROCESSING
MORE USER VISIBILITY
MORE CORRIGIBILITY
MORE SELECTIVE DELETION
```

while preserving enough interaction quality to justify personalization.

The goal is not maximum privacy at the expense of functionality.

It is **minimum necessary data for the desired cognitive support**.

---

# 44. Failure Criteria

The privacy hypothesis should be considered weakened if:

- structured state becomes nearly as extensive as raw history;
- reconstruction of sensitive interactions remains trivial;
- small/local controllers require full raw context anyway;
- personalization quality collapses without broad history;
- users cannot understand or correct persistent state;
- provenance requires invasive behavioral monitoring;
- sociolinguistic inference creates substantial identity profiling;
- or composition models still require full personal transcripts.

These outcomes should alter the architecture.

---

# 45. Architectural Principle

The privacy problem can be summarized as:

```text
DO NOT ASK:
How much can the system learn about this person?

ASK:
What is the minimum state required to make the next interaction
meaningfully better?
```

And after that:

```text
What can now be forgotten?
```

Privacy is therefore not a separate compliance layer added after personalization.

It is a constraint on **what the architecture chooses to know in the first place**.
