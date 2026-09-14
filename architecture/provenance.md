# Rhetorical Compiler

The Rhetorical Compiler is Engine 2 of Deliberation Room.

Its purpose is to take a sufficiently stable human judgment and produce the **exact utterance or artifact appropriate to the rhetorical situation**.

Its optimization target is:

> **Given what this human means, what exactly should this human say or write to this audience, for this purpose, in this situation?**

This is not a post-processing tone layer.

It is a situated composition architecture combining:

```text
HUMAN JUDGMENT
+
CLASSICAL RHETORICAL SITUATION
+
INTERACTIONAL CONDITIONS
+
LINGUISTIC / SOCIOLINGUISTIC EVIDENCE
+
OBSERVED SPEECH / TEXT BEHAVIOR
+
GENRE / DISCIPLINARY CONVENTIONS
+
RELEVANT EXTERNAL EVIDENCE
        ↓
RHETORICAL REALIZATION
        ↓
SEMANTIC / INTERACTIONAL CHECK
        ↓
EXACT FINAL OUTPUT
```

---

## 1. Input: Stabilized Human Judgment

The compiler should not begin from raw conversation history alone.

Its primary semantic input is a structured representation of the human's current judgment.

Possible inputs include:

```text
claims
distinctions
warrants
evidence
uncertainty
constraints
rejected framings
commitments
desired outcome
```

The compiler may also receive conceptual provenance such as:

```text
HUMAN_ORIGINATED

SYSTEM_PROPOSED_HUMAN_RECOGNIZED

SYSTEM_PROPOSED_HUMAN_REVISED

JOINTLY_DEVELOPED

EXTERNAL_EVIDENCE
```

This allows the compiler to generate substantial language without erasing where the underlying ideas came from.

---

## 2. Composition Contract

Before generation, the compiler should create an explicit composition contract.

A conceptual contract may include:

```yaml
artifact:
  type: message

purpose:
  primary: communicate affection and belonging
  secondary: explain why recipient is represented in the idea

audience:
  relationship: intimate
  familiarity: high
  shared_context: high

semantic_invariants:
  - recipient is included because of how the speaker values their mind
  - affection is more important than explaining the architecture
  - no new promise or commitment should be introduced

material_uncertainty:
  - none relevant to the central message

rhetorical_constraints:
  - concise
  - emotionally direct
  - not explanatory
  - not grandiose

interactional_constraints:
  - preserve intimacy
  - do not overperform sentiment
  - leave response latitude

linguistic_constraints:
  - natural speaker cadence
  - established register
  - shared language permitted

external_support:
  required: false
```

The composition contract acts as a boundary between:

```text
WHAT MUST REMAIN TRUE
```

and:

```text
WHAT THE COMPILER MAY TRANSFORM
```

---

## 3. Classical Rhetorical Situation

Classical rhetoric provides part of the compiler's decision architecture.

The compiler should explicitly reason about:

```text
EXIGENCE
AUDIENCE
PURPOSE
ETHOS
PATHOS
LOGOS
KAIROS
CONSTRAINTS
AVAILABLE MEANS
```

These are not decorative labels.

They affect composition decisions.

---

## 4. Exigence

Exigence asks:

> **Why does this utterance need to exist?**

Examples:

```text
clarify misunderstanding
communicate affection
request action
set boundary
make argument
repair relationship
invite critique
explain judgment
demonstrate learning
```

The compiler should distinguish the immediate trigger from the deeper rhetorical need.

For example:

```text
surface task:
explain why Tina appears in the idea

actual exigence:
communicate love and belonging
```

This difference can radically alter the final utterance.

---

## 5. Audience

Audience modeling includes:

```text
who receives the utterance
what they already know
what they do not know
what discourse conventions they share
what role they occupy
what they can reasonably infer
what they may plausibly misunderstand
```

Audience modeling should not become mind reading.

The system may model:

```text
plausible reception
```

but should not claim:

```text
known internal response
```

without evidence.

---

## 6. Purpose

The compiler should distinguish among rhetorical purposes such as:

```text
INFORM
EXPLAIN
ARGUE
PERSUADE
INVITE
REQUEST
REPAIR
EXPRESS
BOUNDARY
DECLINE
ACKNOWLEDGE
TEACH
ASSESS
OPEN CONVERSATION
CLOSE CONVERSATION
```

A composition should not automatically optimize for persuasion if the human's actual purpose is accurate expression.

---

## 7. Ethos

Ethos concerns the speaker-position established through the utterance.

Relevant questions include:

```text
What competence should be visible?

What humility should be visible?

What relationship should be implied?

How much certainty is warranted?

Should the speaker sound:
confident
tentative
warm
authoritative
collaborative
playful
formal
vulnerable
```

Ethos must remain authentic to the speaker.

The compiler should not manufacture a persona that is rhetorically effective but implausible coming from this human.

---

## 8. Pathos

Pathos concerns the affective conditions created by the utterance.

This does not mean maximizing emotion.

The compiler may need to:

```text
increase warmth
reduce accusation
preserve seriousness
create belonging
lower defensiveness
signal care
preserve urgency
avoid melodrama
```

Emotion words themselves contain semantic commitments.

For example:

```text
hurt
excluded
dismissed
abandoned
frustrated
unsafe
```

are not interchangeable intensity settings.

The compiler should preserve emotional precision.

---

## 9. Logos

Logos concerns what reasoning must be visible for the utterance to work.

Possible structures include:

```text
claim → evidence → warrant

observation → interpretation → request

problem → consequence → recommendation

source → inference → uncertainty

experience → distinction → judgment
```

The compiler should not over-explain when the audience already possesses the relevant premises.

Nor should it compress away reasoning necessary for the audience to understand or evaluate the claim.

---

## 10. Kairos

Kairos asks:

> **Why this move, in this form, at this moment?**

Relevant factors may include:

```text
timing
sequence
prior interaction
current emotional state
deadline
public/private setting
medium
audience readiness
whether explanation has already occurred
```

The same sentence can be rhetorically effective in one moment and wrong in another.

Kairos therefore influences:

```text
length
directness
explicitness
topic choice
degree of detail
whether to speak at all
```

---

## 11. Constraints

Constraints define what the rhetorical situation permits.

Examples include:

```text
word count
medium
role
power
privacy
institutional expectations
time
relationship history
legal or ethical limits
genre
audience knowledge
available evidence
```

The compiler should not treat constraints merely as formatting requirements.

They shape which rhetorical moves are available.

---

## 12. Available Means

Available means include the rhetorical and linguistic resources this particular speaker can appropriately use.

Examples:

```text
direct explanation
story
analogy
technical terminology
humor
shared shorthand
formal evidence
emotional disclosure
citation
contrast
question
understatement
silence
```

A resource may be available in the abstract but inappropriate for this speaker, audience, or moment.

---

## 13. Interactional Conditions

The compiler must also model what the utterance **does socially**.

Relevant state includes:

```text
role
power
status
familiarity
relationship history
face
belonging
relational distance
interactional permissions
disclosure pressure
response latitude
social risk
```

A rhetorically correct sentence can still be interactionally wrong.

---

## 14. Response Latitude

The compiler should consider how much meaningful freedom the final utterance leaves the recipient.

A message may allow the recipient to:

```text
agree
disagree
qualify
explain
redirect
decline
disclose
withhold
repair
```

or it may narrow the response space dramatically.

Response latitude is particularly important in:

```text
relationships
education
management
feedback
conflict
boundary setting
```

---

## 15. Face

The compiler should model potential face concerns such as:

```text
competence
autonomy
status
privacy
dignity
belonging
expertise
relational standing
```

This does not imply always softening language.

It means the system should understand the social cost of different realizations.

---

## 16. Belonging

Belonging should not be reduced to friendliness or warmth.

A rhetorical move can support belonging by signaling:

```text
you are recognized
you have a place here
you can correct me
your response is not predetermined
you are not reduced to one role
your perspective matters
```

Sometimes belonging is created through precision and agency rather than emotional language.

---

## 17. Linguistic / Sociolinguistic Model

The compiler should incorporate evidence about how meaning operates in the relevant discourse environment.

Candidate features include:

```text
idiolect
register
dialect
stance
pragmatic markers
mitigation
intensification
code-switching
humor
irony
discourse community
role language
generational conventions
shared vocabulary
relational language history
```

This information is not merely applied after rhetorical reasoning.

It can change the rhetorical choice itself.

---

## 18. Observed Speech and Text Behavior

The compiler should privilege empirical evidence about actual language behavior where available.

Examples include:

```text
lexical choices
sentence length
cadence
punctuation
capitalization
discourse markers
directness
hedging
humor forms
metaphor patterns
degree of explicitness
repair patterns
preferred openings
preferred closings
```

The relevant question is not:

> **What style label fits this person?**

It is:

> **What linguistic evidence is available about how this person actually communicates in comparable contexts?**

---

## 19. Idiolect

Idiolect should be modeled as dynamic, contextual evidence rather than as a fixed voice preset.

A useful idiolect representation may include:

```text
frequent lexical choices
characteristic syntax
recurring metaphors
punctuation habits
humor
cadence
register shifts
profession-specific language
shared relational shorthand
```

The compiler should preserve recognizability without caricaturing the speaker.

---

## 20. Understand Versus Perform

A central sociolinguistic distinction is:

```text
SYSTEM UNDERSTANDS A FORM
≠
SYSTEM HAS PERMISSION TO USE THAT FORM
```

For example, understanding:

```text
slang
dialect
community humor
identity-linked language
```

does not automatically authorize imitation.

The compiler should optimize for pragmatic fit rather than mimicry.

---

## 21. Discourse Community

A discourse community affects:

```text
what terminology is normal
what evidence counts
what humor is legible
how directness is interpreted
how expertise is displayed
what rhetorical structures are conventional
```

Examples may include:

```text
computer science
academia
teaching
law
medicine
military
athletics
gaming
online fandom
```

Discourse community information should inform realization without reducing the audience to a stereotype.

---

## 22. Role Language

Language can change meaning depending on the role of the speaker.

For example:

```text
peer → peer

professor → student

manager → employee

mentor → mentee

partner → partner
```

The compiler should therefore reason not merely about:

```text
what language is normal
```

but:

```text
what language is normal and appropriate
from THIS role
to THIS role
in THIS context
```

---

## 23. Humor

Humor may contribute to:

```text
belonging
face-saving
affiliation
compression
stance
relational continuity
```

but can also create:

```text
artificial intimacy
status confusion
stereotype
embarrassment
mimicry
```

The compiler should represent humor permission explicitly.

Possible forms include:

```text
dry understatement
deadpan
absurdity
self-deprecation
shared callback
gentle teasing
ironic formality
```

The appropriate form depends on the interaction.

---

## 24. Genre Model

The compiler should know what kind of artifact it is producing.

Possible genres include:

```text
text message
email
essay
discussion post
memo
speech
feedback
proposal
boundary message
academic response
reflection
recommendation
report
```

Genre affects:

```text
structure
length
evidence
explicitness
opening
closing
citation
register
argument sequence
```

The compiler should not treat every genre as "paragraphs with different tone."

---

## 25. Disciplinary Rhetorical Conventions

Some genres are discipline-specific.

For example, literary analysis may expect:

```text
interpretive claim
textual evidence
analysis
counterreading
```

Scientific writing may expect:

```text
observation
method
result
mechanism
limitation
```

Professional recommendations may expect:

```text
problem
evidence
options
tradeoff
recommendation
```

The rhetorical compiler should therefore integrate domain-specific conventions where relevant.

---

## 26. Relevant External Evidence

The compiler may retrieve information necessary for accurate composition.

Examples include:

```text
facts
sources
statistics
definitions
terminology
genre conventions
public context
legal or institutional rules
disciplinary precedent
```

External evidence should remain provenance-distinct from human judgment.

The system should not silently rewrite:

```text
THE HUMAN THINKS X
```

when the actual structure is:

```text
THE HUMAN THINKS Y

EXTERNAL EVIDENCE SUGGESTS X
```

---

## 27. Research Should Be Narrowly Useful

Retrieval should not automatically maximize the amount of evidence available.

The compiler should ask:

> **What external information would materially improve accuracy, credibility, or rhetorical fit?**

Possible outcomes include:

```text
NO RESEARCH NEEDED

VERIFY ONE FACT

FIND ONE PRIMARY SOURCE

CHECK GENRE CONVENTION

CHECK AUDIENCE-SPECIFIC TERMINOLOGY

COMPARE PUBLIC CONTEXT
```

This prevents research from overwhelming the human's actual communicative purpose.

---

## 28. Semantic Invariants

Before realization, the compiler should identify what must remain true.

Possible invariants include:

```text
claim
uncertainty
emotional meaning
boundary
commitment
agency
attribution
distinction
request
relationship stance
```

Example:

```text
HUMAN JUDGMENT

"I don't know whether she cares less.
I know that I don't feel included in decisions affecting both of us."
```

The compiler should not produce:

```text
"You clearly don't care about me."
```

That would introduce:

```text
motive
certainty
stronger accusation
different claim
```

---

## 29. Semantic Drift Check

After generation, the compiler should compare the draft against the composition contract.

Candidate drift checks include:

```text
Did the draft:

add a factual claim?

add a motive attribution?

increase certainty?

remove meaningful uncertainty?

introduce a commitment?

change agency?

collapse a distinction?

increase emotional intensity?

change relational stance?

introduce unsupported evidence?
```

A draft that fails the drift check should be revised before presentation.

---

## 30. Interactional Drift Check

Semantic fidelity alone is insufficient.

The compiler should also ask whether realization changed the interactional act.

For example:

```text
human intent:
invite discussion

generated realization:
demands agreement
```

or:

```text
human intent:
express affection

generated realization:
explains theory
```

or:

```text
human intent:
set boundary

generated realization:
punishes recipient
```

These are interactional failures even if individual facts remain accurate.

---

## 31. Compression

The compiler should treat compression as a substantive rhetorical operation.

Sometimes the correct output is shorter than the internal model.

Example:

```text
INTERNAL MODEL

The recipient is represented in the project because the speaker
values the recipient's relational intelligence, care, and way of
thinking about other people.

The speaker wants inclusion in the idea to function as an expression
of love rather than as an explanation of the architecture.

AUDIENCE

intimate
high shared context
high relational familiarity

PURPOSE

belonging + affection

FINAL REALIZATION

"You're in it because I love the way your mind loves people."
```

The final sentence is much smaller than the internal representation.

That does not mean reasoning disappeared.

It means the compiler selected compression as the strongest available rhetorical move.

---

## 32. Expansion

The opposite can also be true.

A short internal judgment may require expansion for:

```text
academic argument
professional justification
technical explanation
legal documentation
assessment
```

The compiler may need to supply:

```text
structure
definitions
evidence
transitions
counterargument
qualification
citation
```

without altering the human's substantive judgment.

---

## 33. Speaker Authenticity

The compiler should ask:

> **Could this person plausibly say this?**

A realization may be technically effective yet fail because it sounds alien to the speaker.

Signals of mismatch may include:

```text
unfamiliar slang
excessive formality
uncharacteristic sentimentality
different humor
different punctuation
different syntax
different vocabulary
different level of directness
```

Authenticity should be grounded in observed language evidence rather than stereotype.

---

## 34. Audience Fit

The compiler should also ask:

> **Could this audience plausibly receive this as intended?**

Relevant factors include:

```text
knowledge
role
expertise
shared context
language
relationship
power
medium
genre expectations
```

The ideal utterance is not merely speaker-authentic.

It is situated between speaker and audience.

---

## 35. Exactness

The goal of the compiler is not to return:

```text
Here are five options.
```

by default.

When sufficient evidence exists, the system should be capable of returning:

> **the strongest exact utterance it can justify**

with optional alternatives when:

```text
multiple rhetorical choices remain genuinely underdetermined
```

or when the human requests options.

The system should not hide uncertainty behind unnecessary option lists.

---

## 36. Confidence and Underdetermination

Sometimes the architecture will not know enough to justify one exact realization.

For example:

```text
audience relationship unknown
power relationship unknown
genre unclear
purpose ambiguous
```

In those cases, the system should ask the smallest question likely to materially change composition.

Example:

> "Is this going to your professor or to a classmate?"

rather than:

> "Tell me everything about your relationship."

The same high-information / low-intrusion principle applies to composition.

---

## 37. Rhetorical Compiler Output

A mature compiler may output both the artifact and a compact trace.

For example:

```text
FINAL MESSAGE

"You're in it because I love the way your mind loves people."

WHY THIS FORM

- primary purpose: affection / belonging
- explanation was rhetorically unnecessary
- intimate audience with high shared context
- compression preserved the human's central judgment
- no unsupported motive or commitment added

CONCEPTUAL PROVENANCE

human-developed

LINGUISTIC PROVENANCE

system-transposed

EXTERNAL EVIDENCE

none used
```

The trace should remain optional for the human-facing interface.

The user should not be forced to read the compiler's internal reasoning every time they want a text message.

---

## 38. Educational Composition

In education, the compiler may produce substantial final prose after cognition has been demonstrated.

For example:

```text
STUDENT JUDGMENT

The unjust burial decree creates the conflict,
but Creon's conception of authority explains why he cannot revise.

COMPILER

Although Creon's burial decree initiates the conflict in Antigone,
Sophocles locates the deeper danger in a model of authority that
treats dissent as disloyalty, preventing correction and making
Creon's judgment increasingly impossible to revise.
```

The wording may be system-generated.

The underlying argument can remain traceable to student reasoning.

That is precisely why conceptual and linguistic provenance must remain separate.

---

## 39. Communication Composition

For interpersonal communication, the compiler may optimize:

```text
semantic precision
face
belonging
response latitude
emotional accuracy
speaker authenticity
relationship fit
```

rather than conventional persuasive effectiveness alone.

The best output may therefore be:

```text
shorter
softer
more direct
less explanatory
less polished
more ordinary
```

than a generic language model would produce.

---

## 40. Professional Composition

In professional contexts, the compiler may integrate:

```text
genre
institutional role
evidence
professional discourse norms
power
actionability
clarity
```

while preserving the human's substantive judgment.

For example, the same underlying concern may become:

```text
text to colleague
email to supervisor
formal memo
meeting talking point
```

with different rhetorical realization in each case.

---

## 41. Evaluation

The Rhetorical Compiler should be evaluated separately from the Metacognitive Controller.

Possible measures include:

```text
semantic preservation
speaker authenticity
audience fit
genre fit
interactional appropriateness
response latitude
evidence accuracy
drift rate
human recognition
final artifact quality
```

A system can have:

```text
excellent deliberation
poor composition
```

or:

```text
weak deliberation
excellent prose
```

Those should remain distinguishable.

---

## 42. Failure Modes

### Generic tone transformation

The system performs:

```text
meaning
→ "make warmer"
```

without modeling the rhetorical situation.

### Style caricature

Observed language patterns become exaggerated imitation.

### Audience stereotyping

Role or demographic information substitutes for actual interaction evidence.

### Semantic drift

The final language changes the underlying judgment.

### Interactional drift

The final language performs a different social act than intended.

### Over-explanation

The compiler includes reasoning the audience does not need.

### Under-explanation

Compression removes reasoning necessary for audience understanding.

### Research overreach

External evidence displaces the human's actual purpose.

### Persuasion optimization

The compiler prioritizes compliance over accurate expression.

### False exactness

The system presents one answer confidently when the rhetorical situation is underdetermined.

---

## 43. Architectural Principle

The Rhetorical Compiler exists to operationalize:

> **Control the utterance.  
> Model the reception.  
> Relinquish the outcome.**

The system can help determine:

```text
what to claim
what to preserve
what to omit
what evidence to include
what language to use
what rhetorical move fits
```

It cannot guarantee:

```text
agreement
affection
forgiveness
compliance
approval
success
```

The final utterance should be the strongest situated realization of the human's actual judgment.

Not the strongest possible manipulation of the audience.
