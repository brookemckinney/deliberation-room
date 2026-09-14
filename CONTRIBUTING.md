# Contributing

Deliberation Room is currently an exploratory interaction architecture and research program.

Contributions are welcome, especially when they:

- identify relevant prior work;
- challenge architectural assumptions;
- propose alternative state representations;
- identify failure modes;
- suggest evaluation designs;
- test next-move policies;
- examine privacy risks;
- propose domain-specific deliberation rules;
- improve schemas;
- or clarify the distinction between existing methods and genuinely new claims.

---

## Classify the contribution

When proposing a change, identify which kind of contribution it is.

### Architectural commitment

A principle the architecture is designed to preserve.

Example:

> Conceptual and linguistic provenance should remain distinct.

### Working hypothesis

A claim intended to be tested empirically.

Example:

> State-adaptive next-move selection may preserve more human cognitive responsibility than unrestricted generation.

### Implementation proposal

One possible mechanism for realizing the architecture.

Example:

> Use a small local model to rank candidate next moves.

### Empirical finding

A result supported by actual evaluation data.

Example:

> In Study X, participants using the controller demonstrated higher transfer scores than participants using the comparison condition.

### Application-specific adaptation

A modification required by a particular domain or use case.

Example:

> Literary analysis should treat counterreading and textual evidence as domain-specific deliberative objects.

These categories should not be treated as interchangeable.

---

## Preserve epistemic precision

Do not convert:

```text
plausible
```

into:

```text
demonstrated
```

Do not convert:

```text
architecturally possible
```

into:

```text
empirically validated
```

Do not convert:

```text
one observed interaction pattern
```

into:

```text
a stable property of a person
```

Claims should preserve their actual evidence status.

---

## Preserve the optimization target

Changes should remain compatible with the central question:

> **What should the human be able to do next?**

A proposed feature should explain how it affects:

- human cognitive agency;
- next-move selection;
- interactional meaning;
- provenance;
- composition;
- privacy;
- or evaluation.

Features that merely increase response fluency, personalization, engagement, or generation quality are not automatically aligned with the architecture.

---

## Avoid hidden cognitive substitution

When proposing new system behavior, ask:

> Is this helping the human perform the relevant reasoning, or quietly performing it for them?

Cognitive substitution is not always wrong.

But it should be intentional, visible, and appropriate to the task.

---

## Treat user models as provisional

Representations of the human should remain:

```text
task-relevant
uncertainty-aware
corrigible
contextual
minimally sufficient
```

Avoid unnecessary:

- personality typing;
- identity inference;
- demographic explanation;
- psychological diagnosis;
- or permanent generalization.

---

## Preserve sociolinguistic meaning

The Linguistic / Sociolinguistic Model is not a style layer.

Contributions should preserve the distinction between:

> **What does this language mean here?**

and:

> **What does using it do here?**

Do not reduce sociolinguistic modeling to tone matching or mimicry.

---

## Preserve provenance

When adding examples, schemas, or implementations, distinguish:

```text
conceptual provenance
```

from:

```text
linguistic provenance
```

A system may provide wording without originating the underlying judgment.

A human may repeat system wording without demonstrating conceptual uptake.

Those cases should remain distinguishable.

---

## Prefer corrigible representations

If a representation about the human could persist, contributors should consider how the human might:

```text
CONFIRM
REVISE
LIMIT SCOPE
MARK TEMPORARY
DELETE
```

Invisible personalization should not become the default simply because it is convenient.

---

## Minimize unnecessary data

Do not assume more personal information produces a better system.

Ask:

> **What is the minimum state required to make the next interaction meaningfully better?**

Then ask:

> **What can now be forgotten?**

---

## Add failure cases

A useful contribution does not only demonstrate when the architecture works.

Include cases where it may fail.

Examples include:

- over-scaffolding;
- hidden steering;
- semantic drift;
- sociolinguistic stereotyping;
- interactional overreach;
- provenance misclassification;
- rumination;
- personalization lock-in;
- unnecessary disclosure;
- or excessive complexity.

---

## Related work

If a contribution appears similar to existing research, include the relevant prior work.

The goal is not to defend novelty at all costs.

The goal is to locate Deliberation Room accurately.

---

## Examples

Examples should distinguish:

```text
WHAT THE HUMAN SAID

WHAT THE SYSTEM INFERRED

WHAT THE SYSTEM PROPOSED

WHAT THE HUMAN RECOGNIZED

WHAT THE HUMAN REJECTED

WHAT CHANGED
```

Avoid examples where the system appears to know the human's internal state without evidence.

---

## Research contributions

Empirical work should report more than artifact quality.

Relevant outcomes may include:

- independent explanation;
- transfer;
- revision;
- response to counterexamples;
- uncertainty calibration;
- provenance;
- response latitude;
- perceived autonomy;
- disclosure burden;
- model cost;
- and privacy exposure.

---

## Pull-request framing

A useful pull request should answer:

1. What problem does this change address?
2. Which part of the architecture does it modify?
3. Is it a principle, hypothesis, implementation proposal, finding, or application adaptation?
4. What new failure mode might it introduce?
5. What evidence would show that the change is wrong?
6. Does it require additional personal data?
7. Does it alter cognitive or linguistic provenance?
8. Does it preserve human ability to correct the model?

---

## Project stance

Deliberation Room should remain willing to become simpler.

If evidence shows that:

- one of the four models adds no value;
- a simpler controller performs equally well;
- provenance cannot be measured reliably;
- personalization creates more risk than benefit;
- or a proposed mechanism does not improve human cognition;

the architecture should change.

Complexity is not a contribution by itself.
