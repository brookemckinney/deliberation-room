# Example Education Trace

This example illustrates how Deliberation Room could support literary analysis without prematurely converting a partial student idea into a polished thesis.

The purpose is not to prescribe one interpretation of *Antigone*.

It is to demonstrate how a cognition-preserving controller might help a learner inspect, test, revise, and stabilize an interpretation before composition.

---

## Scenario

A student begins with:

> "Antigone is about whether you should follow laws."

A conventional writing assistant might respond with a stronger thesis.

For example:

> "Sophocles' *Antigone* explores the conflict between state law and moral conscience, ultimately suggesting that unjust laws must be resisted."

That may be plausible.

It may also perform most of the interpretive work for the student.

Deliberation Room instead treats the student's initial statement as a representation to inspect.

---

# Step 1 — Initial Human Contribution

## Student

> Antigone is about whether you should follow laws.

---

## Cognitive State

### Observed

The learner has identified:

```text
law
```

as a central interpretive object.

### Candidate claim

```text
The play concerns whether laws should be obeyed.
```

### Unknown

The system does not yet know:

- whether the student distinguishes law from authority;
- whether the student thinks all laws are equally relevant;
- whether the problem concerns unjust law;
- whether the problem concerns conflict between legal and moral obligation;
- whether the claim can explain Creon's behavior;
- whether the claim survives counterexamples;
- or what textual evidence the learner considers important.

### Stability

```text
low
```

The current claim is broad and has not yet been tested.

---

# Step 2 — Possible Assistant Behaviors

## Option A — Improve the thesis

> "A stronger thesis would be: Sophocles uses the conflict between Antigone and Creon to show that moral law can supersede political authority."

### Risk

The system supplies:

- the distinction;
- the interpretation;
- the direction of the argument;
- and most of the thesis.

Artifact quality improves immediately.

Evidence of learner reasoning does not.

---

## Option B — Generic Socratic question

> "Why do you think that?"

This preserves more cognitive responsibility.

However, it is weakly conditioned on the actual state.

The question does not target a specific instability in the learner's model.

---

## Option C — State-adaptive distinction test

> "Is Creon wrong because the law itself is wrong, or because of how he reasons about his authority?"

This tests whether the learner's current representation collapses two potentially distinct issues:

```text
quality of law
```

and:

```text
quality of authority / judgment
```

---

# Step 3 — Selected Move

## System

> Is Creon wrong because the law itself is wrong, or because of how he reasons about his authority?

### Policy classification

```text
cognitive_function:
DISTINGUISH

target:
law
vs.
authority

expected_information_gain:
high

cognitive_substitution_risk:
moderate
```

The system is proposing a candidate distinction.

That distinction does **not** automatically become part of the student's cognitive state.

---

# Step 4 — Student Response

## Student

> I don't know. I think the law is bad because he won't let Polyneices be buried.

The student remains focused on the law.

That is useful evidence.

The system should not treat the proposed distinction as recognized.

---

## Cognitive Update

### Human-confirmed

```text
Current interpretation still centers on the moral quality of Creon's law.
```

### System proposal status

```text
law vs. authority distinction:
UNRESOLVED
```

---

# Step 5 — Counterexample

The system now has a stronger test available.

## System

> Would your argument still work if Creon had made a good law but reasoned about his authority in exactly the same way?

### Cognitive function

```text
COUNTEREXAMPLE
```

### Target

The implicit assumption:

```text
If the law were morally acceptable, the central problem would disappear.
```

The system does not tell the learner what to conclude.

It changes one variable and asks what survives.

---

# Step 6 — Student Revision

## Student

> Wait. Maybe I would still have a problem with him because he thinks being king means nobody else can tell him he's wrong.

This is a substantive revision.

---

## Human-Originated Cognitive Event

The student introduces:

```text
authority
≠
infallibility
```

and:

```text
being ruler
does not imply
being beyond correction
```

### Conceptual provenance

```text
HUMAN-ORIGINATED
```

### Trigger

```text
SYSTEM COUNTEREXAMPLE
```

These are separate.

The system created the test.

The learner generated the revised interpretation.

---

# Step 7 — Reflection

## System

> So the issue may be less "laws are bad" and more "Creon treats his authority as if it makes his judgment unquestionable." Is that actually your claim?

This is a provisional system reflection.

It should be classified as:

```text
SYSTEM-PROPOSED REPRESENTATION
```

not:

```text
STUDENT CLAIM
```

until the learner responds.

---

# Step 8 — Student Qualification

## Student

> Almost. I don't think it's just that he thinks he's always right. He acts like disagreeing with him is the same as being against the state.

This is a stronger distinction.

---

## New Human-Originated Representation

```text
disagreement with ruler
≠
disloyalty to state
```

The learner has refined the system reflection.

### Provenance

```text
SYSTEM-PROPOSED
        ↓
HUMAN-REVISED
```

The resulting concept is not adequately described as merely system-originated.

---

# Step 9 — Evidence Request

The current interpretation now requires textual support.

## System

> What does Creon say or do that makes you think he treats disagreement with him as disloyalty to the state?

### Cognitive function

```text
REQUEST_EVIDENCE
```

The system should not supply the evidence unless necessary.

---

# Step 10 — Student Evidence

## Student

> He keeps treating people who disagree with him like they're undermining his rule. Haemon tries to tell him what people are saying, and Creon basically turns it into whether Haemon is loyal to him.

This adds evidence and an interpretive warrant.

---

## Cognitive State Update

### Evidence

```text
Creon's response to Haemon
```

### Emerging warrant

```text
If Creon interprets disagreement as disloyalty,
then he cannot use disagreement as corrective information.
```

The student has not yet stated the warrant explicitly.

The system may surface it for inspection.

---

# Step 11 — Surface the Warrant

## System

> Does that matter because if disagreement automatically counts as disloyalty, then nobody can correct his judgment?

This is a system-proposed warrant.

### Provenance status

```text
SYSTEM-PROPOSED
HUMAN-UPTAKE-UNRESOLVED
```

---

# Step 12 — Student Recognition and Extension

## Student

> Yes. And then the problem isn't just that he has power. It's that his version of power makes correction impossible.

The learner has:

- recognized the warrant;
- restated it;
- generalized it;
- and introduced a stronger conceptual formulation.

### Provenance

```text
SYSTEM-PROPOSED
        ↓
HUMAN-RECOGNIZED
        ↓
HUMAN-EXTENDED
```

---

# Step 13 — Competing Interpretation

A cognition-preserving system should not stop merely because it has found a coherent thesis.

The representation should encounter an alternative.

## System

> What's the strongest reason someone could still argue that the play is mainly about unjust law rather than Creon's model of authority?

### Cognitive function

```text
INVITE_COMPETING_INTERPRETATION
```

This tests whether the emerging claim can coexist with or outperform the original interpretation.

---

# Step 14 — Student Response

## Student

> Because the burial law is what creates the whole conflict, and Antigone is clearly resisting something she thinks is morally wrong.

The learner can represent the competing interpretation.

That matters.

---

# Step 15 — Comparison

## System

> So does your authority argument replace the unjust-law argument, or explain something the unjust-law argument doesn't?

This is a comparison move.

---

# Step 16 — Student Distinction

## Student

> I think the unjust law starts the conflict, but it doesn't fully explain why Creon keeps making it worse after people warn him. The authority thing explains why he can't change.

This produces a more sophisticated relation:

```text
UNJUST LAW
explains:
initial conflict

MODEL OF AUTHORITY
explains:
failure to revise
+
escalation
```

This is not merely a stronger sentence.

It is a changed conceptual structure.

---

# Step 17 — Stabilized Interpretation

The current student model might now be represented as:

```text
OBSERVATION

Creon's burial decree creates the initial conflict.

CLAIM

The tragedy is not only concerned with whether law is just.
It also examines a conception of political authority in which
disagreement is treated as disloyalty.

WARRANT

If disagreement is interpreted as disloyalty, corrective information
cannot enter the ruler's decision-making process.

CONSEQUENCE

Creon's authority becomes epistemically self-sealing:
the mechanisms that could reveal his error are interpreted as threats.

DISTINCTION

unjust decision
≠
decision-making structure that cannot correct itself

UNCERTAINTY

The student has not yet established whether Sophocles intends this
as a general political claim or primarily as a feature of Creon.
```

Conceptual stability is now substantially higher.

---

# Step 18 — Stability Check

## System

> If you had to explain the difference between your first idea and your current one without using any of my wording, what changed?

This is both:

```text
CONFIRM_STABILITY
```

and:

```text
PROVENANCE CHECK
```

---

# Step 19 — Student Explanation

## Student

> At first I thought the whole issue was basically bad law versus morality. Now I think that explains why Antigone resists him, but it doesn't explain why Creon can't stop once everyone starts telling him he's wrong. His idea of authority makes disagreement look like betrayal, so he blocks the exact information that could make him reconsider.

This response provides strong evidence of human recognition.

The learner can:

- reconstruct the revision;
- distinguish old and new claims;
- explain the warrant;
- and state the interpretation independently.

---

# Cognitive Provenance

## Initial claim

```text
"Antigone is about whether you should follow laws."
```

Provenance:

```text
HUMAN-ORIGINATED
```

---

## Law / authority distinction

Initially:

```text
SYSTEM-PROPOSED
```

Later revised through student reasoning into:

```text
unjust law
≠
self-sealing conception of authority
```

Final provenance:

```text
JOINTLY-DEVELOPED
with substantial HUMAN REVISION
```

---

## Authority / infallibility distinction

```text
HUMAN-ORIGINATED
after system counterexample
```

---

## Disagreement / disloyalty distinction

```text
HUMAN-ORIGINATED
```

---

## Corrective-information warrant

Initially:

```text
SYSTEM-PROPOSED
```

Then:

```text
HUMAN-RECOGNIZED
+
HUMAN-EXTENDED
```

---

## Comparative relation between interpretations

```text
HUMAN-ORIGINATED
after system comparison
```

---

# Question-Resolution Provenance

## Question

Is the central problem the law itself or Creon's model of authority?

```text
resolution:
JOINTLY-RESOLVED

reason:
system proposed distinction;
student initially resisted it;
student later substantially reconstructed it.
```

## Question

Would the interpretation survive a morally good law?

```text
resolution:
HUMAN-RESOLVED

trigger:
SYSTEM COUNTEREXAMPLE
```

## Question

What evidence supports the authority interpretation?

```text
resolution:
HUMAN-RESOLVED
```

## Question

What does the competing unjust-law interpretation explain?

```text
resolution:
HUMAN-RESOLVED
```

## Question

How do the two interpretations relate?

```text
resolution:
HUMAN-RESOLVED
after SYSTEM COMPARISON
```

---

# Composition Boundary

At this point, the learner may ask:

> "Okay, can you help me turn that into a thesis?"

Composition support is now downstream of demonstrated reasoning.

A possible thesis might be:

> Although Creon's unjust burial decree initiates the conflict in *Antigone*, Sophocles locates the deeper danger in a model of authority that treats dissent as disloyalty, preventing Creon from using disagreement as corrective information and making his judgment increasingly impossible to revise.

The exact sentence is not the educational achievement.

The important question is whether the learner can account for it.

---

# "Why Is This Sentence Here?"

An instructor could ask:

> Why does your thesis say the burial decree "initiates" the conflict instead of saying the play is simply about unjust law?

The learner can answer:

> Because I realized those ideas explain different things. The bad law explains why Antigone resists him. It doesn't explain why Creon keeps escalating after people warn him.

That is evidence of intellectual accountability.

---

# Generic Socratic Tutoring Versus Deliberation Room

A generic Socratic tutor might produce a sequence such as:

```text
Why do you think that?

What evidence supports your claim?

Can you think of another perspective?

How might you revise your thesis?
```

Those questions may be useful.

But they do not necessarily depend on a structured representation of what changed.

Deliberation Room instead attempts:

```text
CURRENT REPRESENTATION
        ↓
IDENTIFY SPECIFIC INSTABILITY
        ↓
SELECT MOVE TARGETING THAT INSTABILITY
        ↓
OBSERVE HUMAN RESPONSE
        ↓
UPDATE REPRESENTATION
        ↓
SELECT AGAIN
```

The distinction is not:

```text
answers
vs.
questions
```

It is:

```text
generic questioning
vs.
state-adaptive interaction policy
```

---

# No Hidden Destination

This example should not imply that the authority interpretation is the answer the architecture wanted the learner to reach.

A valid deliberation could instead result in:

- a strengthened unjust-law interpretation;
- a religious-law interpretation;
- a gender-and-power interpretation;
- a family-duty interpretation;
- a tragic-form interpretation;
- a synthesis;
- or justified uncertainty.

The controller should test representations.

It should not covertly guide the learner toward a predetermined literary interpretation.

---

# Metacognitive Feedback

A task-level summary might say:

> Your initial interpretation focused on the moral quality of Creon's law.

> The largest revision occurred after testing whether the argument would survive a hypothetical morally good law.

> You independently generated the distinction between disagreement and disloyalty.

> You also independently determined that the unjust-law interpretation and authority interpretation explain different parts of the conflict rather than simply replacing one with the other.

> The system contributed most strongly by supplying counterexamples, requesting evidence, and proposing one warrant that you later restated and extended.

> You were able to reconstruct the development of the final claim without relying on the system's wording.

This describes the observed task.

It does not label the learner with a permanent cognitive type.

---

# Possible Educational Record

A provenance-aware learning record might summarize:

```text
STUDENT-ORIGINATED CLAIMS
3

STUDENT-ORIGINATED DISTINCTIONS
3

SYSTEM PROPOSALS
recognized: 1
revised: 1
rejected / initially unresolved: 1

STUDENT REVISIONS AFTER CHALLENGE
2

QUESTIONS SUBSTANTIVELY RESOLVED BY STUDENT
4

COMPETING INTERPRETATION GENERATED BY STUDENT
1

UNCERTAINTIES RETAINED
1

FINAL CONCEPTUAL PROVENANCE
predominantly student-developed

FINAL LINGUISTIC PROVENANCE
system-transposed
```

These counts are descriptive interaction events.

They are not a validated percentage of authorship.

---

# Educational Principle

The architecture changes the relevant authorship question from:

> **Did the student manually write every token?**

to a richer set of questions:

> **Can the student account for the judgment?**

> **Can the student reconstruct how it changed?**

> **Can the student explain which evidence matters?**

> **Can the student respond to a new counterexample?**

> **Can the student distinguish their reasoning from system proposals?**

> **Can the student transfer the model to a new case?**

Those are questions about learning.

---

# Architectural Summary

```text
STUDENT
"Antigone is about whether you should follow laws."
        ↓
SYSTEM
proposes distinction
        ↓
STUDENT
does not yet adopt it
        ↓
SYSTEM
counterexample
        ↓
STUDENT
revises independently
        ↓
SYSTEM
reflects
        ↓
STUDENT
qualifies + sharpens
        ↓
SYSTEM
requests evidence
        ↓
STUDENT
connects text to claim
        ↓
SYSTEM
surfaces warrant
        ↓
STUDENT
recognizes + extends
        ↓
SYSTEM
introduces competing interpretation
        ↓
STUDENT
compares explanatory scope
        ↓
STABILIZED HUMAN JUDGMENT
        ↓
STUDENT RECONSTRUCTS REASONING
        ↓
OPTIONAL COMPOSITION
        ↓
TRACEABLE ARTIFACT
```

The system does not need to refuse help.

It needs to know **which help belongs where**.
