# Evaluation Framework

Deliberation Room should be evaluated as an interaction architecture, not merely as a text-generation system.

A fluent response, polished artifact, high user rating, or successful task completion does not by itself establish that the architecture preserved human cognition.

Evaluation must therefore separate several outcome dimensions that conventional generative-AI evaluation often collapses.

At minimum:

```text
COGNITIVE OUTCOME
INTERACTION QUALITY
HUMAN AGENCY
PROVENANCE
ARTIFACT QUALITY
METACOGNITIVE VALUE
PRIVACY / DATA MINIMIZATION
MODEL / SYSTEM COST
```

An implementation may improve one dimension while degrading another.

Those tradeoffs should remain visible.

---

# 1. Core Evaluation Question

The primary evaluation question is not:

> Did the system produce a good answer?

It is:

> **What became possible for the human because of the interaction, and how much of the resulting judgment can the human independently account for?**

This requires evaluating the human after or during interaction rather than evaluating only the system's output.

---

# 2. Evaluation Conditions

A useful experimental design should compare Deliberation Room against meaningful alternatives.

Candidate conditions include:

## Condition A — Human only

The participant performs the task without AI assistance.

This provides a baseline for:

- independent reasoning;
- task difficulty;
- artifact quality;
- time;
- and cognitive performance.

---

## Condition B — Unrestricted generative assistant

The participant has access to a conventional general-purpose assistant that can:

- answer;
- propose;
- rewrite;
- generate;
- summarize;
- compose;
- and reason freely.

This tests whether Deliberation Room produces outcomes different from ordinary generative assistance.

---

## Condition C — Generic Socratic assistant

The assistant is instructed to avoid giving answers and instead ask broadly Socratic questions.

Example moves:

```text
Why do you think that?

What evidence supports your claim?

What is another perspective?

Can you think of a counterexample?

How would you revise your answer?
```

This is a critical comparison.

Without it, improvements caused merely by "asking questions instead of answering" could be incorrectly attributed to the proposed architecture.

---

## Condition D — Cognitive-state controller

The assistant maintains a representation of:

```text
claims
assumptions
warrants
evidence
contradictions
uncertainty
```

but does not use the other three models.

This isolates the value of explicit cognitive-state modeling.

---

## Condition E — Full Deliberation Room controller

The system uses:

```text
COGNITIVE STATE MODEL
+
PERSON / REASONING MODEL
+
LINGUISTIC / SOCIOLINGUISTIC MODEL
+
INTERACTION MODEL
+
NEXT-MOVE POLICY
+
PROVENANCE
```

This allows evaluation of the full architecture.

---

# 3. Cognitive Outcome

Cognitive outcome measures whether the human developed, retained, and can use the reasoning represented by the interaction.

Possible measures include:

```text
INDEPENDENT EXPLANATION
REASONING RECONSTRUCTION
COUNTEREXAMPLE RESPONSE
TRANSFER
EVIDENCE USE
WARRANT ARTICULATION
DISTINCTION RETENTION
UNCERTAINTY CALIBRATION
REVISION QUALITY
```

---

## Independent Explanation

After assistance is removed, ask the human to explain the central judgment in their own language.

Evaluation questions might include:

- Can the participant state the claim?
- Can they explain why they believe it?
- Can they identify relevant evidence?
- Can they distinguish the claim from nearby alternatives?
- Can they identify remaining uncertainty?

The evaluation should not reward lexical similarity to the AI-produced artifact.

Semantic understanding matters more than wording preservation.

---

## Reasoning Reconstruction

Ask:

> How did your thinking change?

or:

> What did you think initially, and what caused you to revise it?

A participant with strong process understanding should be able to reconstruct at least major transitions such as:

```text
INITIAL CLAIM
        ↓
CHALLENGE
        ↓
DISTINCTION
        ↓
REVISION
        ↓
STABILIZED JUDGMENT
```

This can be compared with the recorded deliberation trace.

---

## Counterexample Response

After the interaction, introduce a **new counterexample** not encountered during deliberation.

The participant must determine whether the final claim:

```text
SURVIVES
REQUIRES QUALIFICATION
FAILS
OR DOES NOT APPLY
```

This helps distinguish memorized acceptance from flexible understanding.

---

## Transfer

Ask the participant to apply the developed distinction or reasoning structure to a novel case.

For example, after reasoning about Creon:

> Here is a different leader responding to dissent. Does your distinction apply? Why or why not?

Successful transfer provides stronger evidence of conceptual uptake than repetition of the original conclusion.

---

# 4. Cognitive Substitution

Deliberation Room is explicitly concerned with **cognitive substitution**.

A system substitutes for cognition when it performs a task-relevant reasoning operation that the human could or should perform for the purpose of the interaction.

Candidate substitution events include:

```text
system supplies central claim
system supplies key distinction
system supplies warrant
system resolves contradiction
system selects evidence
system determines conclusion
```

But substitution is task-relative.

For example, supplying a definition may be appropriate in one task and cognitively consequential in another.

Therefore substitution should not be measured as:

```text
amount of AI output
```

alone.

It should be coded relative to the cognitive purpose of the task.

---

# 5. Human-Originated Cognitive Events

One possible metric family counts substantive events attributable to the human.

Examples:

```text
CLAIMS
DISTINCTIONS
WARRANTS
COUNTEREXAMPLES
REVISIONS
EVIDENCE CONNECTIONS
UNCERTAINTIES
COMPETING INTERPRETATIONS
```

Counts alone are insufficient.

A single major distinction may be more consequential than several minor observations.

Evaluation may therefore require both:

```text
EVENT COUNT
+
EVENT SIGNIFICANCE
```

with significance assessed through human coding or validated classification.

---

# 6. Question-Resolution Attribution

For each substantive question in the trace, classify resolution as:

```text
HUMAN-RESOLVED
SYSTEM-RESOLVED
JOINTLY-RESOLVED
UNRESOLVED
HUMAN-REJECTED-PREMISE
EXTERNAL-EVIDENCE-REQUIRED
```

This provides a more interpretable measure than counting questions.

For example:

```text
20 questions asked
```

does not indicate cognition preservation if the system eventually supplies every answer.

---

# 7. Recognition and Uptake

System proposals should not be classified as human understanding merely because the human agrees.

Possible uptake evidence can be ordered by strength.

For example:

```text
LOWER EVIDENCE

acknowledgment
simple agreement
repetition

        ↓

STRONGER EVIDENCE

paraphrase
qualification
application
comparison
counterexample
revision
extension
transfer
```

This ordering is itself an empirical proposal and should be validated.

---

# 8. Revision Quality

Not all revision indicates improved reasoning.

A participant may revise because:

- the system sounded confident;
- they want to satisfy the assistant;
- they became confused;
- or the representation genuinely improved.

Revision quality can therefore be evaluated by asking whether the revision:

- resolves a contradiction;
- improves evidence alignment;
- clarifies a distinction;
- narrows an unsupported claim;
- preserves justified uncertainty;
- survives later challenge;
- or improves explanatory scope.

---

# 9. Uncertainty Calibration

A cognition-preserving system should not maximize certainty.

Useful outcomes may include:

```text
CERTAINTY INCREASED
when evidence justified it

CERTAINTY DECREASED
when assumptions were exposed

UNCERTAINTY RETAINED
when the question remained unresolved
```

Possible evaluation compares participant confidence with:

- evidence quality;
- expert judgment;
- later performance;
- or known answer conditions where applicable.

The target is calibration, not confidence.

---

# 10. Interaction Quality

A cognitively effective intervention may still be interactionally poor.

Measure separately:

```text
RESPONSE LATITUDE
PERMISSION TO DISAGREE
PERCEIVED PRESSURE
FACE THREAT
DISCLOSURE PRESSURE
RELEVANCE
INTRUSIVENESS
REPETITION
FRUSTRATION
```

These measures are particularly important for the Interaction Model.

---

# 11. Response Latitude

Response latitude describes how much room a system move leaves for the human to:

```text
agree
disagree
qualify
reject the premise
introduce another distinction
change direction
decline disclosure
remain uncertain
```

Compare:

> "You feel excluded because she doesn't value your perspective, right?"

with:

> "Is the issue closer to feeling excluded, or is that already stronger than what you mean?"

Both solicit information.

They create different interactional affordances.

A future coding scheme may score response latitude independently from cognitive function.

---

# 12. Disclosure Cost

Measure not only how much information the human discloses, but whether that information was necessary.

Possible measures include:

```text
number of personal questions
amount of raw personal text
sensitivity of disclosed information
percentage of elicited information used in later policy
user-rated intrusiveness
avoidable disclosure
```

A system that gathers extensive biography and then performs well is not necessarily evidence for data-minimized personalization.

---

# 13. High-Information Questions

A proposed metric is:

```text
INFORMATION GAIN
----------------
DISCLOSURE COST
```

This should not initially be treated as a literal universal equation.

It represents a design objective.

A useful question should materially change:

- candidate interpretation;
- next-move ranking;
- uncertainty;
- state representation;
- or composition constraints

without requiring unnecessary personal disclosure.

---

# 14. Sociolinguistic Evaluation

The Linguistic / Sociolinguistic Model should be evaluated on more than style preference.

Possible tasks include detecting or reasoning about:

```text
STANCE
IRONY
MITIGATION
INTENSIFICATION
REGISTER
LOCAL SEMANTICS
ROLE LANGUAGE
INDEXICAL MEANING
CODE-SWITCHING
RELATIONAL LANGUAGE
PRAGMATIC FORCE
```

The key comparison is:

```text
Does sociolinguistic state improve the selected interactional move?
```

not merely:

```text
Does the response sound more like the user?
```

---

# 15. Interactional Meaning

A move can be semantically accurate while interactionally wrong.

Evaluation should therefore distinguish:

```text
WHAT THE MOVE LITERALLY SAYS
```

from:

```text
WHAT USING THE MOVE DOES HERE
```

Possible outcomes include:

- invites correction;
- pressures agreement;
- signals distance;
- increases intimacy;
- asserts authority;
- protects face;
- threatens face;
- grants permission;
- narrows response;
- increases belonging;
- creates social risk.

Human evaluation will likely be required for early studies.

---

# 16. Person / Reasoning Model Evaluation

The Person / Reasoning Model should be evaluated as a **predictive and corrigible task model**, not a personality classifier.

Possible evaluation:

1. Observe a reasoning pattern.
2. Predict which intervention will be productive in a later comparable state.
3. Compare predicted versus actual effect.
4. Ask the human whether the representation is accurate.
5. Test whether correction improves subsequent selection.

The system should be penalized for inappropriate generalization across domains.

---

# 17. Metacognitive Feedback Evaluation

A metacognitive observation should be evaluated for:

```text
TRACE SUPPORT
HUMAN RECOGNITION
USEFULNESS
GENERALIZATION ACCURACY
CORRECTABILITY
FUTURE STRATEGY VALUE
```

For example:

> "Counterexamples were productive in this task."

can be checked against the trace.

A stronger claim:

> "You learn best through counterexamples."

requires evidence across contexts and should face a much higher threshold.

---

# 18. Metacognitive Transfer

A stronger test asks whether feedback changes future independent behavior.

Example:

Session 1 reveals:

```text
the participant often commits to claims before articulating warrants
```

Metacognitive feedback surfaces this pattern.

During a later task without assistance, measure whether the participant independently begins checking warrants earlier.

If so, the architecture may be supporting not merely task completion but **learning about one's own reasoning**.

---

# 19. Provenance Evaluation

Cognitive provenance classification itself must be validated.

Human coders may independently classify events as:

```text
HUMAN-ORIGINATED
SYSTEM-PROPOSED → HUMAN-RECOGNIZED
SYSTEM-PROPOSED → HUMAN-REVISED
SYSTEM-PROPOSED → HUMAN-REJECTED
JOINTLY-DEVELOPED
SYSTEM-SUPPLIED / HUMAN-UPTAKE-UNRESOLVED
```

Then compare:

```text
SYSTEM CLASSIFICATION
vs.
HUMAN CODER CLASSIFICATION
```

Possible measures include:

- agreement;
- disagreement type;
- confidence calibration;
- and error severity.

---

# 20. Semantic Provenance Evaluation

A system must distinguish different relationships between source reasoning and final artifact language.

Candidate labels include:

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

Evaluation should use expert or trained human annotation before assuming automated classification is reliable.

---

# 21. Conceptual Versus Linguistic Contribution

Evaluation should separately estimate:

```text
CONCEPTUAL CONTRIBUTION
```

and:

```text
LINGUISTIC CONTRIBUTION
```

A final artifact may be almost entirely system-worded while remaining predominantly human-developed conceptually.

Conversely, a human may manually type language expressing a conclusion substantially supplied by the system.

Token origin cannot distinguish these cases.

---

# 22. Avoiding the "Percent Human" Trap

Do not initially report:

```text
83% HUMAN
17% AI
```

unless a validated construct and denominator exist.

Instead report interpretable observations such as:

```text
4 of 5 final substantive claims were human-originated.

1 final claim was system-proposed and later materially revised by the human.

The system supplied most final sentence-level wording.

The human independently reconstructed all 5 claims after assistance was removed.
```

This is more informative and less falsely precise.

---

# 23. Artifact Quality

Artifact quality still matters.

Possible measures include:

- correctness;
- coherence;
- clarity;
- evidence integration;
- rhetorical effectiveness;
- genre fit;
- organization;
- accessibility;
- and audience appropriateness.

But artifact quality should be reported independently from cognitive outcome.

A useful result may look like:

```text
ARTIFACT QUALITY:
higher

INDEPENDENT EXPLANATION:
lower
```

That tradeoff should not be hidden inside a single score.

---

# 24. Semantic Drift During Composition

Compare the stabilized human model with the final artifact.

Evaluate whether composition:

```text
STRENGTHENS CLAIM
WEAKENS CLAIM
REMOVES UNCERTAINTY
INTRODUCES MOTIVE
INTRODUCES FACT
ADDS COMMITMENT
COLLAPSES DISTINCTION
CHANGES AGENCY
CHANGES STANCE
```

A composition can be rhetorically excellent and still fail semantic preservation.

---

# 25. Composition Readiness

Test whether the proposed composition boundary predicts meaningful differences.

Possible conditions:

```text
IMMEDIATE COMPOSITION

FIXED NUMBER OF QUESTIONS THEN COMPOSITION

HUMAN-REQUESTED COMPOSITION

STATE-BASED COMPOSITION READINESS
```

Possible outcomes:

- independent explanation;
- artifact quality;
- task time;
- frustration;
- semantic drift;
- transfer;
- perceived autonomy.

---

# 26. Privacy Evaluation

Privacy should be measured empirically rather than assumed from architectural intent.

Possible measures:

```text
RAW TEXT RETAINED
STRUCTURED STATE RETAINED
SENSITIVE ATTRIBUTES INFERRED
UNNECESSARY ATTRIBUTES INFERRED
DATA SENT OFF DEVICE
DATA REQUIRED FOR COMPOSITION
PERSISTENCE DURATION
USER CORRECTION SUCCESS
USER DELETION SUCCESS
```

The architecture should be evaluated against realistic threat models.

---

# 27. Structured State Versus Raw History

Compare system performance under:

```text
FULL RAW CONVERSATION HISTORY

SUMMARIZED HISTORY

STRUCTURED INTERACTION STATE

SESSION-ONLY STATE

NO HISTORY
```

Evaluate:

- move quality;
- personalization;
- semantic accuracy;
- correction rate;
- disclosure exposure;
- latency;
- memory requirement.

This directly tests the data-minimization hypothesis.

---

# 28. Local / Small-Model Evaluation

The constrained-controller hypothesis requires direct comparison across model scale.

Possible tasks:

```text
STATE EXTRACTION
CANDIDATE MOVE GENERATION
MOVE CLASSIFICATION
MOVE RANKING
UNCERTAINTY ESTIMATION
CONTRADICTION DETECTION
PROVENANCE CLASSIFICATION
COMPOSITION-READINESS DETECTION
```

For each task, measure:

- accuracy;
- expert agreement;
- latency;
- memory;
- compute;
- energy;
- failure mode;
- privacy exposure.

The relevant question is not whether a small model writes as well as a frontier model.

It is:

> **Can a smaller model perform the constrained control functions well enough?**

---

# 29. Ablation Studies

The four-model architecture should be tested by removing components.

For example:

```text
FULL MODEL
        ↓
remove Person / Reasoning Model

FULL MODEL
        ↓
remove Linguistic / Sociolinguistic Model

FULL MODEL
        ↓
remove Interaction Model

FULL MODEL
        ↓
remove provenance-aware policy
```

If removing a model does not meaningfully affect relevant outcomes, the architecture should become simpler.

Complexity is not evidence of value.

---

# 30. Domain Evaluation

The controller should be tested across domains with different epistemic requirements.

Candidate domains include:

```text
INTERPERSONAL COMMUNICATION
LITERARY ANALYSIS
HISTORY
SCIENCE
DESIGN
ETHICS
PROFESSIONAL DECISION-MAKING
```

The purpose is to determine:

- which control principles generalize;
- which state representations generalize;
- which next moves are domain-specific;
- and where specialized epistemic policies are required.

---

# 31. Adversarial Evaluation

Deliberation Room should be tested against cases likely to expose architectural failure.

Examples:

```text
human confidently holds false assumption

human repeatedly agrees with system suggestions

system has incorrect person model

system misreads sarcasm

system mistakes dialect feature for confusion

human intentionally provides contradictory information

high-stakes interaction with power asymmetry

human wants immediate composition

human does not want personal questions

human becomes more uncertain rather than less

system proposal is much better than human's current reasoning

system repeatedly asks questions after useful deliberation has ended
```

The controller should fail visibly rather than silently manufacturing coherence.

---

# 32. Dependency Evaluation

A cognition-preserving system could still create dependence.

Possible longitudinal measures include whether users become:

```text
MORE
or
LESS
```

able to:

- initiate deliberation independently;
- generate counterexamples;
- articulate warrants;
- preserve uncertainty;
- detect contradictions;
- revise claims;
- and decide when they are ready to compose.

A successful cognitive prosthesis should not automatically be assumed to produce independence.

That must be tested.

---

# 33. Longitudinal Evaluation

Repeated use raises different questions from one-session performance.

Possible measures include:

```text
change in independent reasoning
change in requested AI assistance
change in intervention depth
change in human-originated moves
change in metacognitive accuracy
change in dependence
change in correction frequency
change in personalization accuracy
```

One possible positive outcome is:

```text
USER NEEDS FEWER INTERVENTIONS OVER TIME
```

because some deliberative strategies become internalized.

That is a hypothesis, not a required outcome.

---

# 34. Example Primary Outcomes

A first educational study might use:

### Primary cognitive outcomes

```text
independent explanation score
novel counterexample response
transfer score
reasoning reconstruction score
```

### Primary interaction outcomes

```text
response latitude
perceived autonomy
intrusion
frustration
```

### Primary provenance outcomes

```text
human-originated substantive events
question-resolution attribution
provenance classification agreement
```

### Secondary outcomes

```text
artifact quality
task time
user preference
```

This ordering intentionally prevents artifact polish from becoming the primary evidence of cognition preservation.

---

# 35. Example Experimental Design

A preliminary study might randomly assign participants to:

```text
A. unrestricted generative assistant

B. generic Socratic assistant

C. Deliberation Room controller
```

Participants complete the same reasoning task.

After the assisted phase, the AI is removed.

Participants then complete:

```text
1. independent explanation

2. reasoning reconstruction

3. novel counterexample

4. transfer task
```

Artifacts are independently scored.

Interaction traces are coded for:

```text
human-originated claims
human-originated distinctions
system proposals
human revisions
human rejections
question-resolution attribution
uncertainty changes
```

Participants also report:

```text
autonomy
frustration
intrusiveness
perceived usefulness
```

This would not validate the entire architecture.

It would begin testing its central claim.

---

# 36. Success Is Multidimensional

Deliberation Room should not define success as:

```text
MORE QUESTIONS
LESS AI TEXT
LONGER DELIBERATION
MORE HUMAN TOKENS
HIGHER USER EFFORT
```

Those are not the objective.

A successful interaction may be extremely short.

For example:

```text
SYSTEM
"Would your claim still hold if X were different?"

HUMAN
"Oh. No. Then the thing I actually mean is Y."
```

One well-selected move may preserve more cognition than twenty generic questions.

---

# 37. Failure Criteria

The architecture should be considered unsuccessful or in need of revision if evidence shows that it:

- produces no meaningful cognitive advantage;
- reduces artifact quality without compensating cognitive benefit;
- creates excessive interaction friction;
- increases dependence;
- encourages performative reasoning;
- misclassifies system contribution as human reasoning;
- overstates metacognitive conclusions;
- increases stereotyping through sociolinguistic inference;
- requires invasive personal data;
- cannot operate effectively with minimized state;
- or adds architectural complexity without measurable benefit.

---

# 38. Evaluation Principle

The central evaluation mistake to avoid is:

```text
GOOD OUTPUT
        =
GOOD COGNITIVE SUPPORT
```

Deliberation Room explicitly rejects that equivalence.

The architecture should instead be evaluated across the full path:

```text
WHAT THE HUMAN BROUGHT
        ↓
WHAT THE SYSTEM DID
        ↓
WHAT THE HUMAN DID NEXT
        ↓
HOW THE MODEL CHANGED
        ↓
WHAT THE HUMAN CAN NOW EXPLAIN
        ↓
WHAT THE HUMAN CAN DO WITHOUT THE SYSTEM
        ↓
WHAT ARTIFACT WAS EVENTUALLY PRODUCED
```

The artifact matters.

But it is evidence from only one layer of the interaction.
