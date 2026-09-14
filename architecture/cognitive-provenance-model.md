# Cognitive Provenance

Cognitive provenance represents how substantive judgments, distinctions, claims, revisions, and final artifacts emerge across human-system interaction.

Its central question is not merely:

> **Who produced these words?**

It is:

> **How did the reasoning embodied in this artifact develop, and which parts can the human account for?**

This distinction matters because textual production and intellectual contribution are related but not identical.

A human may originate a substantive idea that a system later expresses in different language.

A system may propose an idea that the human meaningfully evaluates, revises, and incorporates.

A human may repeat model-generated language without demonstrating understanding.

Cognitive provenance attempts to preserve those differences.

---

## Why This Exists

Conventional provenance often focuses on:

- authorship;
- token origin;
- revision history;
- document history;
- or whether AI generated text.

Those are useful questions.

But they do not fully answer an educational or cognitive question:

> **Does the human understand and own the judgment represented here?**

For Deliberation Room, provenance therefore includes the evolution of the underlying model.

A trace may show:

```text
INITIAL OBSERVATION
        ↓
TENTATIVE CLAIM
        ↓
SYSTEM CHALLENGE
        ↓
HUMAN REJECTION
        ↓
NEW DISTINCTION
        ↓
REVISED CLAIM
        ↓
COUNTEREXAMPLE
        ↓
HUMAN REVISION
        ↓
STABILIZED JUDGMENT
        ↓
SYSTEM-ASSISTED COMPOSITION
```

The final prose is only the endpoint.

The reasoning path matters.

---

## Two Primary Provenance Dimensions

At minimum, the architecture should distinguish:

### 1. Conceptual provenance

Who introduced, developed, tested, revised, rejected, or stabilized the substantive idea?

### 2. Linguistic provenance

Who supplied the wording used to express the idea in the final artifact?

These dimensions should remain separate.

For example:

```text
conceptual provenance:
HUMAN-ORIGINATED

linguistic provenance:
SYSTEM-TRANSPOSED
```

is possible.

So is:

```text
conceptual provenance:
SYSTEM-PROPOSED → HUMAN-REVISED

linguistic provenance:
HUMAN-WORDED
```

The architecture should not collapse either case into a binary:

```text
AI
vs.
HUMAN
```

---

## Conceptual Provenance States

Possible conceptual provenance states include:

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

These labels are provisional, but the distinctions are important.

---

## Human-Originated

A concept is human-originated when the human introduces the substantive idea or distinction before the system proposes it.

Example:

```text
HUMAN
"I don't care if we do equal amounts.
I care whether we're both noticing each other."
```

The human has introduced a distinction:

```text
equal contribution
≠
mutual attentiveness
```

If the system later writes:

> "The issue is not strict reciprocity but mutual attentiveness."

the linguistic realization may be system-generated while the conceptual distinction remains human-originated.

---

## System-Proposed → Human-Recognized

The system may propose a distinction or hypothesis that the human meaningfully recognizes.

Recognition should require more than passive continuation when possible.

Evidence might include:

- restatement;
- application;
- qualification;
- defense;
- counterexample;
- extension;
- or coherent use in later reasoning.

Example:

```text
SYSTEM
"Are you distinguishing being noticed from being included?"

HUMAN
"Yes. Exactly. Someone can notice every detail about me and still
make decisions as if I don't belong inside them."
```

The system proposed the distinction.

The human demonstrated understanding and elaborated it.

---

## System-Proposed → Human-Revised

Sometimes the system provides a useful but incomplete representation.

Example:

```text
SYSTEM
"Is this mainly about reciprocity?"

HUMAN
"Not really. Reciprocity sounds transactional.
I mean mutual attentiveness."
```

The system proposal contributed to the reasoning process but did not survive unchanged.

The final concept should reflect that revision.

---

## System-Proposed → Human-Rejected

A rejected proposal remains part of the deliberation trace.

Example:

```text
SYSTEM
"It sounds like you feel abandoned."

HUMAN
"No. That's exactly the word I don't mean."
```

The proposal should not enter the stabilized cognitive state.

But the rejection itself may produce useful information.

It may clarify:

- semantic boundaries;
- interactional meaning;
- conceptual structure;
- or the human's model of the problem.

Rejected system proposals are therefore cognitively relevant even when they contribute nothing to the final claim.

---

## Jointly Developed

Some concepts emerge through interaction in ways that are not usefully reducible to one speaker.

For example:

```text
HUMAN
"I don't think it's really about the law."

SYSTEM
"What changes if the law itself is good?"

HUMAN
"Then I still don't trust Creon."

SYSTEM
"So what remains constant?"

HUMAN
"His belief that being king makes his judgment the same thing
as the state's interest."
```

The final distinction emerged through iterative elicitation and revision.

Calling it exclusively human-originated or system-originated may erase the interactional process.

`JOINTLY-DEVELOPED` can preserve that complexity.

---

## System-Supplied / Human-Uptake-Unresolved

This category matters especially in educational contexts.

Example:

```text
SYSTEM
"The concept you're describing is epistemic authority."

HUMAN
"Okay."
```

The concept may now appear in the conversation.

But the human has not yet demonstrated:

- understanding;
- application;
- distinction;
- or independent use.

The system should not treat this as human-owned understanding.

A useful state is:

```text
SYSTEM-SUPPLIED
HUMAN-UPTAKE-UNRESOLVED
```

until further evidence appears.

---

## Linguistic Provenance States

Possible linguistic provenance states include:

```text
HUMAN-PRESERVED
HUMAN-EDITED
SYSTEM-TRANSPOSED
SYSTEM-GENERATED
JOINTLY-REFINED
UNKNOWN
```

### Human-preserved

Final language substantially preserves human wording.

### Human-edited

System may have suggested wording, but the human materially revised it.

### System-transposed

System substantially changed surface form while preserving a human-developed meaning.

### System-generated

System supplied most or all of the final wording.

### Jointly refined

Wording emerged through iterative revision between human and system.

These labels describe language production.

They do not establish conceptual ownership.

---

## Provenance Event Model

A deliberation trace may represent events rather than only final labels.

For example:

```yaml
event:
  type: distinction

  content:
    left: "equal effort"
    right: "mutual attentiveness"

  introduced_by: human

  triggered_by:
    system_move: clarify

  epistemic_status: user_confirmed

  later_used_in:
    - claim_3
    - artifact_paragraph_2
```

This preserves both:

```text
WHO INTRODUCED THE DISTINCTION
```

and:

```text
WHAT INTERACTION HELPED ELICIT IT
```

Those are not the same question.

---

## Question-Resolution Provenance

The architecture may also track who substantively resolved a question.

Example:

```text
QUESTION
What distinguishes X from Y?

SYSTEM ROLE
Asked the question.

RESOLUTION
Human generated distinction.

PROVENANCE
HUMAN-RESOLVED
```

Compare:

```text
QUESTION
What evidence supports the claim?

SYSTEM ROLE
Asked question, then supplied evidence.

HUMAN ROLE
Accepted evidence without elaboration.

PROVENANCE
SYSTEM-RESOLVED / HUMAN-UPTAKE-UNRESOLVED
```

This distinction is especially useful for metacognitive feedback.

---

## Candidate Resolution States

Possible question-resolution states include:

```text
HUMAN-RESOLVED
SYSTEM-RESOLVED
JOINTLY-RESOLVED
UNRESOLVED
HUMAN-REJECTED-PREMISE
EXTERNAL-EVIDENCE-REQUIRED
```

A question can also disappear because the human rejects the framing.

That should not be counted as failed reasoning.

---

## Deliberation Trace

A cognitive provenance system requires more than raw transcript storage.

The relevant object is a structured trace of meaningful state changes.

A trace might include:

```text
STATE 1
Human claim: X

MOVE
System asks for evidence

STATE 2
Human provides A

MOVE
System presents counterexample B

STATE 3
Human rejects original claim X

STATE 4
Human introduces distinction Y/Z

MOVE
System tests Y/Z against new case

STATE 5
Human preserves Y/Z and revises warrant

STATE 6
Judgment stabilizes
```

The trace focuses on model evolution rather than every conversational token.

---

## Cognitive Event Types

Candidate trace events may include:

```text
HUMAN_CLAIM
HUMAN_QUESTION
HUMAN_DISTINCTION
HUMAN_ASSUMPTION
HUMAN_WARRANT
HUMAN_EVIDENCE
HUMAN_COUNTEREXAMPLE
HUMAN_REVISION
HUMAN_REJECTION
HUMAN_UNCERTAINTY
HUMAN_STABILITY_CONFIRMATION

SYSTEM_PROPOSAL
SYSTEM_CHALLENGE
SYSTEM_COUNTEREXAMPLE
SYSTEM_REFLECTION
SYSTEM_REFRAME
SYSTEM_ASSUMPTION_SURFACED

JOINT_DISTINCTION
JOINT_REVISION

COMPOSITION_TRANSITION
SEMANTIC_DRIFT_DETECTED
RETURN_TO_DELIBERATION
```

The exact event taxonomy remains an implementation question.

---

## Metacognitive Feedback

The trace can support feedback not only about the artifact but about **how the human reasoned during the task**.

Possible feedback includes:

> "Most of your substantive revisions occurred after testing a claim against a counterexample."

> "You generated claims quickly, while warrants required more elicitation."

> "Your strongest distinctions were human-originated."

> "You rejected four of the system's six proposed interpretations before the model stabilized."

> "You retained uncertainty in two places rather than collapsing it."

> "Most system contribution occurred during linguistic transposition rather than claim development."

This feedback can make the reasoning process itself inspectable.

---

## Metacognitive Feedback Is Not Diagnosis

The architecture should avoid turning task-level evidence into fixed cognitive identity.

Prefer:

> "Counterexamples were productive in this deliberation."

over:

> "You are a counterexample thinker."

Prefer:

> "You revised more often after concrete comparison in this task."

over:

> "You are a concrete learner."

A metacognitive observation is a system inference.

It should therefore remain:

```text
PROVISIONAL
CONTEXTUAL
CORRIGIBLE
```

---

## Human Correction of Metacognitive Feedback

Metacognitive feedback should itself enter the deliberative loop.

For example:

```text
SYSTEM
"You seemed to make the most progress through counterexamples."

HUMAN
"Only because we were testing an argument. I hate that when I'm
brainstorming."

UPDATE
counterexample_effectiveness:
  domain: argument_testing
  supported: true
  generalizability: limited
```

This prevents the Person / Reasoning Model from turning interaction patterns into rigid traits.

---

## Human/System Contribution Reports

A future system may generate descriptive contribution reports.

For example:

```text
DELIBERATION SUMMARY

Questions substantively resolved by human: 14

Human-originated:
  claims: 4
  distinctions: 6
  counterexamples: 3
  warrants: 2

System proposals:
  recognized: 2
  materially revised: 4
  rejected: 5
  unresolved uptake: 1

Human revisions after system challenge: 5

Uncertainties intentionally retained: 2

Final substantive claims:
  human-originated: 3
  jointly developed: 2
  system-proposed / human-recognized: 1
```

Such a report can be meaningful without pretending to assign exact intellectual percentages.

---

## Why Simple Percentages Are Dangerous

A tempting output might be:

```text
82% human
18% AI
```

This is probably too crude.

The denominator is unclear.

Possible denominators include:

- tokens;
- sentences;
- propositions;
- claims;
- distinctions;
- reasoning events;
- artifact sections;
- or weighted substantive contribution.

Those measures are not interchangeable.

A system should not present exact percentages as objective authorship facts without validated methodology.

---

## Conceptual Percentage Versus Linguistic Percentage

If quantitative measures are eventually used, conceptual and linguistic contribution should remain separate.

For example:

```text
SUBSTANTIVE JUDGMENTS
primarily human-originated

FINAL WORDING
primarily system-transposed
```

This could later be visualized independently.

Conceptually:

```text
CONCEPTUAL PROVENANCE
████████████████░░░░
mostly human-developed

LINGUISTIC PROVENANCE
██████░░░░░░░░░░░░░
substantial system transposition
```

The visualization should not imply validated numerical precision unless the underlying classification supports it.

---

## Descriptive Synonymy

A major provenance problem involves semantically equivalent or near-equivalent wording.

Example:

```text
HUMAN
"I don't care if we do equal amounts.
I care if we're both noticing each other."

SYSTEM
"The issue is not strict reciprocity but mutual attentiveness."
```

The wording is different.

The substantive distinction may be preserved.

A provenance system may therefore need to classify semantic relationships such as:

```text
DIRECT PRESERVATION
DESCRIPTIVE SYNONYMY
PARAPHRASE
ENTAILMENT
NARROWING
EXPANSION
REFRAME
SEMANTIC DRIFT
NEW CLAIM
```

These classifications are difficult.

They should not be treated as solved.

---

## Same Topic Is Not Same Meaning

The architecture must distinguish:

```text
same topic
```

from:

```text
same proposition
```

from:

```text
related proposition
```

from:

```text
stronger proposition
```

from:

```text
weaker proposition
```

from:

```text
changed proposition
```

For example:

```text
"I don't know where I fit into her decisions."
```

is not semantically equivalent to:

```text
"She doesn't care about me."
```

Both concern the relationship.

They make different claims.

A provenance system that relies only on topical similarity would fail here.

---

## Provenance Through Composition

The final artifact may map its claims back to the deliberation trace.

Conceptually:

```text
ARTIFACT CLAIM C7
        │
        ├── conceptual origin:
        │      HUMAN-ORIGINATED
        │
        ├── first appeared:
        │      STATE 4
        │
        ├── challenged:
        │      MOVE 7
        │
        ├── revised:
        │      STATE 8
        │
        ├── stabilized:
        │      STATE 11
        │
        ├── final wording:
        │      SYSTEM-TRANSPOSED
        │
        └── semantic drift check:
               PASSED
```

This creates a traceable relationship between artifact and reasoning.

---

## Intellectual Accountability

Cognitive provenance supports a broader notion of authorship:

> **Can the human account for the judgment represented here?**

A human with meaningful intellectual accountability should often be able to explain:

- where the claim came from;
- what evidence supports it;
- what challenged it;
- what changed;
- which system proposals were rejected;
- why a distinction mattered;
- what uncertainty remains;
- and why the final artifact contains the claim.

This does not require the human to have manually produced every token.

---

## The "Why Is This Here?" Test

A useful educational probe is:

> **Why is this sentence here?**

A learner who meaningfully owns the reasoning may answer:

> "Originally I thought X, but the counterexample broke that argument.
> I had to distinguish X from Y, so this paragraph is where I establish
> that distinction."

That is evidence of process understanding.

A learner who cannot account for the sentence may still understand it, but the provenance claim is weaker.

The test is diagnostic, not definitive.

---

## Provenance Is Not Proof

Cognitive provenance should not be treated as cryptographic proof of independent thought.

A trace may still be manipulated.

A human can accept system-generated reasoning without deep understanding.

A system can misclassify recognition.

A learner may understand something without producing a rich trace.

Therefore cognitive provenance should be interpreted as:

```text
STRUCTURED EVIDENCE OF REASONING DEVELOPMENT
```

not:

```text
CERTIFICATION OF AUTHENTIC THOUGHT
```

---

## Provenance Without Surveillance

The architecture should avoid assuming that provenance requires:

- keystroke logging;
- browser history;
- webcam monitoring;
- eye tracking;
- biometric data;
- continuous screen capture;
- or invasive behavioral telemetry.

The relevant evidence is primarily interactional and conceptual.

A minimal trace might preserve:

```text
claim introduced
claim challenged
human revision
distinction introduced
uncertainty retained
composition transition
```

rather than every low-level action.

---

## Data Minimization

Not every trace element should persist indefinitely.

Possible retention levels include:

```text
TURN-LEVEL
SESSION-LEVEL
TASK-LEVEL
ARTIFACT-LINKED
USER-SELECTED PERSISTENCE
EPHEMERAL
```

A user might choose to retain:

```text
final cognitive trace
+
metacognitive summary
```

while discarding:

```text
raw conversational transcript
```

Whether this is sufficient for later verification or composition should be tested empirically.

---

## Privacy Risk

Cognitive provenance itself can contain sensitive information.

A trace may reveal:

- beliefs;
- uncertainty;
- reasoning patterns;
- private relationships;
- values;
- misconceptions;
- emotional concerns;
- or intellectual vulnerabilities.

Therefore:

> **Provenance data should not be considered harmless merely because it is abstracted.**

A structured cognitive trace may be more revealing than raw text in some contexts.

Data minimization, user control, visibility, and selective deletion remain necessary.

---

## Metacognitive Profile

A future implementation could produce a task-level profile such as:

```text
METACOGNITIVE FEEDBACK

You generated:
- 4 substantive claims
- 5 distinctions
- 2 counterexamples

You revised:
- 3 claims after counterexamples
- 2 claims after evidence checks

The system contributed most often by:
- surfacing assumptions
- requesting warrants
- transposing final language

You rejected:
- 4 system interpretations
- 2 proposed framings

Patterns observed in this task:
- concrete comparison frequently preceded useful distinctions
- uncertainty increased appropriately after evidence review
- most final claims remained human-originated
```

This report should remain descriptive.

It should not diagnose a fixed cognitive type.

---

## Metacognitive Feedback as Learning

The provenance layer can serve a second educational purpose.

Instead of only showing:

```text
WHAT YOU CONCLUDED
```

it can show:

```text
HOW YOUR REASONING CHANGED
```

This may help learners develop awareness of:

- how they use evidence;
- when they revise;
- what kinds of questions help;
- where they tend to skip warrants;
- how they respond to counterexamples;
- and when they preserve uncertainty appropriately.

This turns process evidence into potential metacognitive instruction.

---

## Feedback Can Become Future State

If the human recognizes a metacognitive observation, it may update the Person / Reasoning Model.

Conceptually:

```text
DELIBERATION TRACE
        ↓
METACOGNITIVE OBSERVATION
        ↓
HUMAN RESPONSE
   ↙      ↓       ↘
ACCEPT  QUALIFY  REJECT
   \      |       /
        UPDATE
          ↓
PERSON / REASONING MODEL
```

This creates a closed feedback loop.

The system learns about the human's reasoning through interaction.

The human can inspect and correct what the system believes it has learned.

---

## A Possible Trace Representation

```yaml
deliberation_trace:

  events:

    - id: e1
      type: human_claim
      content: "The issue is unequal effort."
      conceptual_source: human
      epistemic_status: user_confirmed

    - id: e2
      type: system_challenge
      target: e1
      move: counterexample

    - id: e3
      type: human_revision
      previous: e1
      content: "Equal effort is not actually the issue."
      trigger: e2

    - id: e4
      type: human_distinction
      content:
        left: "equal contribution"
        right: "mutual attentiveness"
      conceptual_source: human

    - id: e5
      type: system_reflection
      target: e4

    - id: e6
      type: human_recognition
      target: e5
      status: confirmed

  stabilized_judgment:
    claims:
      - source_event: e4

  composition:
    linguistic_provenance: system_transposed
    semantic_drift_check: passed
```

This is illustrative rather than final.

---

## Provenance Granularity

The architecture must determine the appropriate unit of provenance.

Possible units include:

```text
TOKEN
PHRASE
SENTENCE
PROPOSITION
CLAIM
DISTINCTION
WARRANT
EVIDENCE LINK
ARGUMENT MOVE
PARAGRAPH
ARTIFACT SECTION
```

Token-level provenance is useful for wording.

Proposition-level provenance may be more useful for cognition.

Different purposes may require different granularity.

---

## Provenance Confidence

Classification itself may be uncertain.

For example:

```yaml
provenance:
  classification: jointly_developed
  confidence: medium
  ambiguity:
    - "human introduced partial distinction"
    - "system supplied explicit category labels"
```

The architecture should expose uncertainty rather than forcing every idea into a clean category.

---

## Mixed Provenance

A single claim may contain components with different histories.

Example:

```text
CLAIM:
"Creon's political failure comes from treating personal judgment
as identical to state interest, which makes dissent appear illegitimate."
```

Possible provenance:

```text
"personal judgment ≠ state interest"
    HUMAN-ORIGINATED

"dissent appears illegitimate"
    SYSTEM-PROPOSED → HUMAN-RECOGNIZED

combined causal relationship
    JOINTLY-DEVELOPED
```

The system should allow mixed provenance when useful.

---

## External Sources

Conceptual provenance should also distinguish system contribution from external evidence.

For example:

```text
HUMAN-ORIGINATED INTERPRETATION

SUPPORTED BY:
external scholarly source
```

or:

```text
SYSTEM-PROPOSED DISTINCTION

BASED ON:
retrieved source
```

A future implementation may need separate provenance dimensions for:

```text
human
system
external source
retrieval
tool output
```

especially in research and education.

---

## Contribution Is Not Value

The architecture should not assume:

```text
more human contribution = better
```

or:

```text
more system contribution = worse
```

A system may appropriately provide:

- terminology;
- inaccessible background knowledge;
- translation;
- organization;
- accessibility support;
- or substantial linguistic assistance.

The relevant question is whether contribution is:

```text
VISIBLE
APPROPRIATE
TRACEABLE
AND CONSISTENT WITH THE TASK'S PURPOSE
```

---

## Educational Use

In education, a provenance report could help instructors distinguish:

```text
artifact production
```

from:

```text
reasoning development
```

Possible evidence might include:

- student-originated claims;
- student-originated distinctions;
- questions resolved by the student;
- revisions after challenge;
- system proposals accepted or rejected;
- warrants generated;
- uncertainty retained;
- final composition assistance.

The goal is not to create an automated cheating score.

It is to provide richer evidence of learning.

---

## Assessment Use

A provenance-aware assessment might ask the learner to revisit particular trace events:

> "You changed your claim after this counterexample. Explain why."

> "This distinction appears in your final paper. Where did it emerge?"

> "The system proposed this idea and you retained it. Apply it to a new case."

> "You rejected this interpretation. What made it inadequate?"

These tasks assess intellectual accountability more directly than asking whether AI was used.

---

## Failure Modes

### Token reductionism

Authorship is reduced to percentage of generated words.

### Recognition inflation

Minimal agreement is treated as deep human understanding.

### Human-origin inflation

A system-generated concept is labeled human-originated because the human later repeats it.

### System-origin inflation

A human concept is labeled system-originated because the system supplied polished terminology.

### False precision

Unvalidated percentages are presented as objective contribution scores.

### Semantic equivalence error

Different propositions are treated as synonymous because their wording is similar.

### Trace overload

The provenance system stores every interaction event and becomes unusable or invasive.

### Surveillance creep

Provenance expands into unnecessary monitoring.

### Metacognitive reification

Task-level patterns become fixed claims about the person's cognitive type.

### Incentive distortion

Learners optimize for appearing "human-originated" instead of learning.

### Provenance theater

A detailed trace creates confidence without actually measuring meaningful understanding.

---

## What Cognitive Provenance Must Not Claim

The architecture should not claim that provenance:

- proves authentic thought;
- proves independent authorship;
- perfectly identifies idea ownership;
- can assign objective human/AI percentages without validation;
- makes invasive monitoring unnecessary in every context;
- establishes conceptual understanding from simple agreement;
- or resolves all educational concerns about generative AI.

Its purpose is more modest and more useful:

> **Preserve structured evidence about how reasoning and artifacts developed.**

---

## Research Questions

Key open questions include:

1. What is the appropriate unit of conceptual provenance?
2. What interactional evidence is sufficient to classify human recognition?
3. How can human revision be distinguished from superficial paraphrase?
4. When should a concept be labeled jointly developed?
5. Can proposition-level semantic equivalence be classified reliably?
6. How should descriptive synonymy be detected?
7. How should semantic drift alter provenance labels?
8. Can conceptual and linguistic provenance be estimated independently?
9. Which trace events are most predictive of later independent explanation?
10. Which metacognitive patterns can be inferred reliably from a single task?
11. How should metacognitive claims generalize across tasks?
12. Can users accurately correct provenance classifications?
13. How much trace information is necessary for useful accountability?
14. Can structured traces replace raw transcript retention?
15. What privacy risks arise specifically from cognitive-state data?
16. How should external sources and retrieval systems appear in provenance?
17. How should mixed provenance within one claim be represented?
18. Can provenance-aware educational assessment outperform AI-detection approaches?
19. How should instructors interpret system-proposed but human-recognized concepts?
20. Can contribution reports be made useful without encouraging simplistic percentages?
21. What visualizations best communicate conceptual versus linguistic contribution?
22. Does metacognitive feedback derived from traces improve future independent reasoning?
23. How should the architecture distinguish productive joint cognition from excessive cognitive substitution?
