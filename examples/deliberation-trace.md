# Example Deliberation Trace

This example illustrates how Deliberation Room might behave differently from a conventional generative assistant.

It is not presented as evidence that a current implementation already performs these operations reliably.

The purpose is to make the proposed architecture inspectable.

---

## Scenario

A human is trying to explain why an interaction bothered them.

They begin with:

> "I need to explain why this conversation bothered me, but every version sounds dramatic."

A conventional assistant might immediately offer rewritten versions.

Deliberation Room first asks whether the problem is actually one of wording.

---

# Step 1 — Initial Human Contribution

## Human

> I need to explain why this conversation bothered me, but every version sounds dramatic.

---

## Cognitive State

### Observed

The human:

- experienced discomfort;
- wants to communicate about it;
- has already attempted to formulate the message;
- is dissatisfied with those formulations;
- describes the problem using the word `dramatic`.

### Unknown

The system does not yet know whether:

- the wording exaggerates the event;
- the wording exaggerates the emotion;
- the human does not yet understand the source of the emotion;
- the event is functioning as evidence of a broader relational concern;
- or the audience makes certain framings inappropriate.

---

## Person / Reasoning Model

Available interaction evidence suggests:

```text
tentative candidate interpretations
+
contrast between alternatives
```

often allows this human to make distinctions quickly.

Confidence:

```text
moderate
```

This does not imply a permanent reasoning type.

---

## Linguistic / Sociolinguistic Model

The word:

```text
dramatic
```

is currently ambiguous.

Possible meanings include:

```text
emotionally exaggerated
rhetorically inflated
too accusatory
too formal
too absolute
misaligned with the relationship
```

The system should not decide which meaning is intended without evidence.

---

## Interaction Model

Still unknown:

- audience;
- relationship;
- power;
- stakes;
- desired outcome.

Those variables may become important later.

However, the immediate uncertainty can potentially be reduced without requesting all of that information.

---

# Step 2 — Candidate Next Moves

The system considers several possibilities.

---

## Candidate A — Immediate composition

> "Here are three less dramatic ways to say it..."

### Advantages

- immediately useful if wording is actually the problem;
- low user effort.

### Risks

- assumes the human already understands the underlying issue;
- may merely polish an unstable model;
- may create semantic drift;
- high cognitive substitution risk.

---

## Candidate B — Broad elicitation

> "Tell me exactly what happened from the beginning."

### Advantages

- gathers substantial context.

### Risks

- high disclosure cost;
- may gather far more information than necessary;
- delays the distinction actually needed.

---

## Candidate C — Premature interpretation

> "It sounds like you're more hurt by what the conversation represents than by what actually happened."

### Advantages

- may be correct;
- gives the human a concrete candidate to evaluate.

### Risks

- supplies a major distinction;
- may anchor the human;
- converts system inference into the center of the reasoning process.

---

## Candidate D — High-information clarification

> "When you say the versions sound dramatic, is the problem that they exaggerate what happened, or that they make the feeling sound bigger than the reason for it?"

### Expected effects

```text
information gain: high
intrusion cost: low
cognitive substitution risk: moderate-low
response latitude: high
```

---

# Step 3 — Selected Move

## System

> When you say the versions sound dramatic, is the problem that they exaggerate what happened, or that they make the feeling sound bigger than the reason for it?

### Policy classification

```text
cognitive_function:
CLARIFY / DISTINGUISH

linguistic_realization:
contrastive question

interactional_affordance:
- permits either option
- permits rejection of both
- requires little additional disclosure
```

### Provenance

The system has **not** yet asserted a substantive interpretation of the relationship.

It has proposed a distinction for inspection.

---

# Step 4 — Human Response

## Human

> The feeling isn't too big. The wording makes it sound like I'm upset about one event, but I'm actually reacting to what it shows me about the relationship.

This is a substantive state change.

---

## New Human-Originated Distinction

```text
EVENT-LEVEL COMPLAINT
≠
RELATIONSHIP-LEVEL INTERPRETATION
```

### Conceptual provenance

```text
HUMAN-ORIGINATED
```

### Trigger

```text
SYSTEM CLARIFICATION
```

These are intentionally separate fields.

The system created a condition under which the distinction emerged.

The system did not originate the distinction itself.

---

# Step 5 — Updated Cognitive State

The model now represents:

### Human-confirmed

```text
The emotional magnitude is not the primary problem.
```

### Human-originated distinction

```text
reaction to isolated event
≠
reaction to what the event appears to indicate about the relationship
```

### Still unresolved

The system does not yet know:

- what relationship-level meaning the human sees;
- whether that interpretation is stable;
- whether alternative explanations have been considered;
- what the communication goal is.

---

# Step 6 — Candidate Next Moves

The system could now say:

> "So the event made you realize they don't value you."

That would be a substantial inference.

The available evidence does not support it.

Instead, the relevant cognitive question is:

> **What does the event appear to indicate?**

---

## Selected Move

### System

> Okay. Then what does the event seem to show you about the relationship that the event itself doesn't capture?

### Cognitive function

```text
ELICIT INTERPRETATION
```

### Why not propose one?

Because the human has enough structure to generate the interpretation and the architecture currently has no evidence that supplying one would improve the process.

---

# Step 7 — Human Response

## Human

> I think it's that she notices me, but she notices the parts of my life that affect what she's going to do. I don't know if I feel included in the actual decisions.

This produces another substantive distinction.

---

## Human-Originated Distinction

```text
BEING NOTICED
≠
BEING INCLUDED
```

and a more specific relational representation:

```text
attention to information about me
≠
treating me as a participant in decisions involving me
```

### Conceptual provenance

```text
HUMAN-ORIGINATED
```

### System role

```text
ELICITATION
```

---

# Step 8 — System Reflection

The system now has enough information to test whether its representation is accurate.

## System

> So being noticed isn't the thing you're missing. You can feel very noticed and still not feel like you exist inside the decision-making.

This is a **system reflection**.

It compresses the human's distinction into a candidate representation.

---

# Step 9 — Human Correction

## Human

> Yes, but "exist inside the decision-making" sounds way more dramatic than what I mean. It's more like I want to know that my future is something we think about together.

This correction contains information across multiple models.

---

## Cognitive State Update

The prior distinction remains:

```text
noticed
≠
included
```

But the human refines what `included` means.

New representation:

```text
my future is considered collaboratively
```

---

## Linguistic / Sociolinguistic Update

The phrase:

```text
exist inside the decision-making
```

is rejected because its rhetorical force exceeds the intended claim.

This is evidence of **semantic/pragmatic mismatch**, not rejection of the underlying distinction.

---

## Person / Reasoning Update

The human used correction of wording to produce a more precise conceptual representation.

A task-level observation may be:

```text
candidate paraphrases can be productive when the user can
correct them precisely
```

This should not yet generalize into a permanent trait.

---

# Step 10 — Remaining Uncertainty

The system may now represent:

```text
CURRENT HUMAN JUDGMENT

I do not primarily need more attention.

I want evidence that decisions affecting our shared future are
considered collaboratively rather than merely tracked individually.
```

But this may still contain system language.

The system should verify recognition.

---

# Step 11 — Stability Check

## System

> Is "I want my future to be something we think about together" basically the center of it, or is there still something missing?

This move performs:

```text
CONFIRM_STABILITY
```

rather than:

```text
GENERATE_MESSAGE
```

---

# Step 12 — Human Recognition

## Human

> Yeah. That's it. I don't need her to know everything or ask about everything. I want to feel like when something involves both of us, I'm already part of how she thinks about it.

The human has now:

- recognized the central representation;
- elaborated it independently;
- introduced a boundary;
- clarified what the claim does **not** require.

---

# Stabilized Judgment

A structured representation might be:

```text
CLAIM

When a decision concerns a shared future, the human wants to be
represented as a participant in the thinking that precedes the decision.

DISTINCTION

being informed about another person's life
≠
jointly considering shared consequences

NOT CLAIMED

- constant attention
- equal effort in every interaction
- access to every private decision
- certainty about the other person's motives

UNCERTAINTY RETAINED

The system does not know how the other person understands the relationship
or how they will respond.
```

---

# Step 13 — Composition Boundary

At this point the human may request:

> "Okay. Now help me say that."

The architecture transitions from:

```text
DELIBERATION
```

to:

```text
COMPOSITION
```

---

# Composition Contract

Possible semantic invariants:

```text
PRESERVE:
- this is about shared decision-making, not generalized attention
- the user is describing their own need
- the user is not claiming to know the recipient's motives
- the user does not demand constant inclusion
- uncertainty about the recipient remains intact
```

Possible rhetorical constraints:

```text
- not accusatory
- emotionally honest
- concise
- allows response
- does not overstate commitment or certainty
```

---

# Example Composition

The system might produce:

> I think I finally understand what's been bothering me. It isn't that I need you to notice everything I'm doing or check in about every part of my life. I think I want to feel like when something touches both of our futures, I'm already somewhere inside the way we think about it together.

The exact language is not important to this example.

The provenance is.

---

# Final Provenance

## Conceptual provenance

### Human-originated

```text
event-level concern
≠
relationship-level meaning

being noticed
≠
being included

shared future should be considered collaboratively
```

### System contribution

```text
clarifying contrast
elicitation
reflection
stability check
```

### System proposal revised by human

```text
"exist inside the decision-making"
```

was rejected as rhetorically excessive and replaced by the human with:

```text
"my future is something we think about together"
```

---

## Linguistic provenance

The final artifact may be:

```text
SYSTEM-TRANSPOSED
```

even though its central substantive representation is:

```text
HUMAN-ORIGINATED
```

These are not contradictory.

---

# Question-Resolution Provenance

### Question

What does `dramatic` mean in this context?

```text
resolution:
HUMAN-RESOLVED

trigger:
SYSTEM CLARIFICATION
```

### Question

Is the concern about the event itself or what the event represents?

```text
resolution:
HUMAN-RESOLVED
```

### Question

What does the event appear to indicate?

```text
resolution:
HUMAN-RESOLVED
```

### Question

Is the current representation sufficiently accurate?

```text
resolution:
HUMAN-CONFIRMED
```

---

# Metacognitive Feedback

A task-level report might say:

> You made the largest conceptual advances by rejecting or refining candidate framings rather than by answering broad questions.

> Two major distinctions were human-originated after system elicitation.

> One system reflection was useful but rhetorically overstated your meaning; correcting it produced a more precise formulation.

> The system contributed primarily through question selection and final linguistic transposition rather than by originating the central judgment.

These are observations about this deliberation.

They should not automatically become fixed claims about how the human always reasons.

---

# What a Conventional Transcript Misses

A raw transcript would preserve:

```text
human said X
system said Y
human said Z
```

The deliberation trace additionally preserves:

```text
WHY Y WAS SELECTED

WHAT Y WAS TRYING TO TEST

WHETHER Z WAS HUMAN-ORIGINATED

WHICH REPRESENTATION CHANGED

WHAT THE HUMAN REJECTED

WHAT REMAINED UNCERTAIN

WHEN THE MODEL STABILIZED

WHAT AI CONTRIBUTED TO THE FINAL ARTIFACT
```

That is the difference between:

```text
conversation history
```

and:

```text
cognitive provenance
```

---

# Architectural Summary

```text
HUMAN:
"Everything I write sounds dramatic."
        ↓
SYSTEM:
high-information clarification
        ↓
HUMAN:
event ≠ relationship meaning
        ↓
SYSTEM:
elicits relationship meaning
        ↓
HUMAN:
noticed ≠ included
        ↓
SYSTEM:
reflects provisional model
        ↓
HUMAN:
corrects language + sharpens concept
        ↓
SYSTEM:
checks stability
        ↓
HUMAN:
recognizes + elaborates
        ↓
STABILIZED JUDGMENT
        ↓
OPTIONAL COMPOSITION
        ↓
TRACEABLE ARTIFACT
```

The system helped structure the walk.

The human still had to walk it.
