# Relational Interaction

Relational interaction is the application of Deliberation Room to situations where the system is helping a human decide **how to interact with another person**, not merely how to formulate content.

The central problem is not:

> **What would be a good thing to say?**

It is:

> **What interactional move is appropriate here, between these people, for this purpose?**

This requires modeling not only information and language, but the social action created by the move.

---

# 1. Relational Interaction Is Not Personalization After Reasoning

A conventional architecture might operate as:

```text
decide what to say
        ↓
personalize tone
        ↓
generate response
```

Deliberation Room proposes something stronger:

```text
COGNITIVE STATE
+
PERSON / REASONING MODEL
+
LINGUISTIC / SOCIOLINGUISTIC MODEL
+
INTERACTION MODEL
        ↓
SELECT RELATIONAL MOVE
```

The relational meaning of language can change which move is appropriate in the first place.

This means:

> **Social meaning is part of reasoning about interaction, not merely a style layer applied afterward.**

---

# 2. Recognition Versus Demonstrated Knowledge

A system with access to rich information about another person can easily produce interactions that demonstrate research.

That is not necessarily the same as producing recognition.

Compare:

```text
"I saw you had 12 tackles against X last weekend."
```

with:

```text
"How's the week treating you?"
```

The first may demonstrate knowledge.

The second may create more room for the person to decide what matters.

Whether the first is better depends on:

- relationship;
- familiarity;
- context;
- relevance;
- disclosure expectations;
- and whether revealing the information feels natural or surveillant.

A core principle is:

> **Prefer recognition over demonstrated knowledge when demonstrated knowledge does not improve the interaction.**

---

# 3. Information Available Is Not Information That Should Be Revealed

The system may know:

```text
private_context
```

that is useful for selecting a move but should not be surfaced directly.

This creates an important distinction:

```text
INFORMATION THE SYSTEM MAY USE
```

versus:

```text
INFORMATION THE HUMAN SHOULD REVEAL
```

For example, knowing that someone recently experienced a public loss may help the system avoid an insensitive joke.

That does not imply the human should say:

> "I saw what happened."

The information can improve interaction without becoming part of the utterance.

---

# 4. Private Context

A relational interaction system may therefore distinguish:

```text
PRIVATE CONTEXT
```

from:

```text
RECOMMENDED MOVE
```

Private context includes information useful for calibration but not necessarily appropriate to reveal.

Examples:

- recent public performance;
- known institutional role;
- current workload;
- shared history;
- likely sensitivity;
- previous interaction;
- status difference;
- or public context.

The system should ask:

> **Does revealing this information improve the interaction, or merely demonstrate that it was found?**

---

# 5. Minimum Viable Relational Move

A central heuristic is:

> **Minimum viable relational move. Maximum human response latitude.**

The ideal move often does less than the system technically could.

It may simply create an opening.

Example:

```text
SYSTEM KNOWS:
student's team lost badly
student did not play
public reporting mentions internal conflict

BAD MOVE:
"How are you doing after not getting much playing time during
that rough loss?"

BETTER MOVE:
"How's your week going?"
```

The richer information may be useful precisely because it tells the system what **not** to surface.

---

# 6. Response Latitude

A relational move should be evaluated partly by the range of responses it permits.

High response latitude allows the person to:

- answer briefly;
- elaborate;
- redirect;
- joke;
- disclose;
- withhold;
- correct;
- or disengage.

Low response latitude may force:

- explanation;
- emotional disclosure;
- defense;
- acknowledgment of failure;
- or participation in a topic the person did not choose.

The system should prefer moves that preserve meaningful agency unless the interaction requires greater specificity.

---

# 7. "Actually..." as a Success Condition

One useful observable behavior is:

> **"Actually..."**

This often indicates that the human has enough space to:

- correct the frame;
- introduce what actually matters;
- expand identity;
- change topic;
- or offer context the system could not have predicted.

A good interactional move does not require the system to anticipate the entire conversation.

It creates room for the other person to author what comes next.

---

# 8. Identity-Confirming Versus Identity-Expanding Moves

Relational systems can easily reduce a person to the most salient available category.

Examples:

```text
athlete
student
employee
parent
patient
expert
novice
```

An identity-confirming move reinforces the already salient role.

Example:

> "How was the game?"

An identity-expanding move creates space for the person to appear as more than that role.

Example:

> "What have you been into this week?"

Neither is universally better.

The policy should ask:

> **Does this identity frame improve recognition, or unnecessarily narrow the person?**

---

# 9. Identity Salience

A person's identity may be:

```text
relevant
available
public
```

without being:

```text
interactionally desirable
```

The system should not assume:

```text
known identity
=
best conversation topic
```

A person may be tired of being approached primarily through the identity others find most visible.

The architecture should treat topic selection as relational rather than merely informational.

---

# 10. Belonging

Belonging is not equivalent to friendliness.

A relational move can contribute to belonging by positioning the other person as:

- recognized;
- intelligible;
- competent;
- interesting;
- welcome;
- able to participate;
- able to correct;
- and authoritative about their own experience.

Belonging can be undermined when a move positions the person as:

- an object of research;
- a representative of a category;
- a problem to be managed;
- a performance to be evaluated;
- or someone whose response has already been predicted.

---

# 11. Recognition

Recognition may involve demonstrating that:

```text
I remember you
I heard what you said
I noticed what mattered
I understand the context
```

But recognition should not become surveillance performance.

A system should distinguish:

```text
"You mentioned last week that you were nervous about the presentation.
How'd it go?"
```

from:

```text
"I found the event results online and saw that your group placed fourth."
```

Both may be accurate.

The relational meaning is different.

---

# 12. Face

Relational moves should preserve face when possible.

A person may be protecting:

- competence;
- dignity;
- privacy;
- status;
- autonomy;
- confidence;
- belonging;
- or emotional control.

A move can threaten face by:

- presuming failure;
- calling attention to embarrassment;
- demonstrating excessive research;
- forcing disclosure;
- highlighting a marginalized identity;
- or requiring public correction.

The architecture should consider whether the intended benefit justifies the face cost.

---

# 13. Face-Saving and Revision

Face is also relevant when the human is being challenged.

Compare:

> "You were wrong about that."

with:

> "Did that turn out differently than you expected?"

Both may address the same factual outcome.

The second may preserve more room for explanation and self-correction.

This does not mean all directness is bad.

It means directness has interactional consequences.

---

# 14. Power

Power changes the meaning of relational moves.

Possible sources include:

```text
grading
employment
institutional authority
expertise
age
access
resources
evaluation
social status
dependency
```

A professor and student do not have the same interactional permissions as peers.

A manager's joke is not automatically equivalent to a coworker's joke.

A system should therefore ask:

> **Can the lower-power participant decline, redirect, or disengage without meaningful cost?**

---

# 15. Familiarity

Familiarity affects:

- directness;
- humor;
- shared language;
- disclosure;
- callbacks;
- teasing;
- correction;
- and topic depth.

Possible states might include:

```text
UNKNOWN
MINIMAL FAMILIARITY
REPEATED CONTACT
ESTABLISHED RAPPORT
HIGH FAMILIARITY
INTIMATE / CLOSE RELATIONSHIP
```

These labels are only rough approximations.

The important principle is that interactional permission should be evidence-based rather than assumed.

---

# 16. Humor Permissions

Humor can produce belonging.

It can also create:

- face threat;
- confusion;
- forced intimacy;
- cultural mismatch;
- or power-related discomfort.

Candidate humor forms include:

```text
dry understatement
self-deprecation
shared-situation humor
ironic formality
callback humor
gentle teasing
absurdity
deadpan
```

The system should consider:

- established persona;
- prior humor history;
- role;
- power;
- stakes;
- topic sensitivity;
- and audience.

---

# 17. Understand Humor Without Performing It

A system may need to understand that a phrase is playful.

It does not follow that the system should reproduce that playfulness.

Likewise, a professor may understand student slang without using it.

The objective is:

```text
PRAGMATIC FIT
```

not:

```text
LINGUISTIC MIMICRY
```

Understanding a discourse convention and having permission to perform it are different states.

---

# 18. Generational Norms

Generational discourse norms may inform interpretation.

They should not determine behavior by stereotype.

For example, humor associated with a younger cohort may include:

- ironic detachment;
- absurdity;
- compressed meme references;
- self-aware exaggeration;
- or anti-formal register.

This can help a system understand a student's communicative environment.

It does not justify imitating those features merely to appear relatable.

Observed person-specific interaction should override demographic expectation.

---

# 19. Discourse Community

A discourse community can change:

- terminology;
- humor;
- norms of expertise;
- directness;
- expectations of evidence;
- interaction rhythm;
- and what counts as marked language.

Examples include:

```text
athletics
academia
military
gaming
engineering
teaching
medicine
online fandoms
```

The system may use this information to interpret interaction.

It should not reduce the person to membership in the discourse community.

---

# 20. Role Language

Roles can create local linguistic expectations.

For example:

```text
professor → student
coach → athlete
manager → employee
mentor → mentee
```

A phrase that sounds supportive from a peer may sound evaluative from an authority figure.

The Interaction Model should therefore represent not only:

```text
WHAT LANGUAGE IS NORMAL
```

but:

```text
WHAT LANGUAGE IS NORMAL FROM THIS ROLE
TO THIS OTHER ROLE
```

---

# 21. Topic Sensitivity

Some topics carry elevated interactional risk.

Examples may include:

- loss;
- injury;
- performance;
- grades;
- playing time;
- family;
- relationships;
- finances;
- health;
- identity;
- conflict;
- discipline;
- or failure.

The system should not assume public availability makes a topic low-risk.

A public fact can still be socially sensitive.

---

# 22. Public Information Does Not Eliminate Social Risk

A system may reason:

```text
this information is public
therefore it is acceptable to mention
```

That is insufficient.

The relevant question is:

> **Would mentioning it make the person feel recognized, or researched?**

Public information can still create surveillance cues.

The system should weigh interactional value against that cost.

---

# 23. Research Visibility

A useful variable is:

```text
RESEARCH VISIBILITY
```

Possible levels:

```text
LOW
The human could plausibly know this through normal shared context.

MODERATE
The information suggests deliberate attention.

HIGH
The information strongly signals external research or tracking.
```

High research visibility is not inherently prohibited.

But the system should require stronger interactional justification.

---

# 24. Social Risk

A candidate move can create different forms of risk:

```text
FACE RISK
DISCLOSURE RISK
IDENTITY RISK
STATUS RISK
RELATIONAL RISK
EMBARRASSMENT RISK
EVALUATION RISK
```

The policy should consider:

```text
expected relational value
-
unnecessary social risk
```

not just conversational relevance.

---

# 25. Disclosure Pressure

A move may make personal disclosure difficult to avoid.

Example:

> "How are you handling everything at home?"

requires more boundary management than:

> "How's your week?"

The more powerful the speaker, the more consequential this pressure can become.

The system should prefer lower-pressure openings when specificity is unnecessary.

---

# 26. Invitation Versus Interrogation

A useful relational distinction is:

```text
INVITATION
```

versus:

```text
INTERROGATION
```

Invitation creates optionality.

Interrogation accumulates questions or specificity in ways that require response.

A relational system should generally prefer:

> **invitation over interrogation**

unless the role or task explicitly requires information collection.

---

# 27. Recognition Versus Tracking

Another critical distinction is:

```text
RECOGNITION
```

versus:

```text
TRACKING
```

Recognition communicates:

> "I remember something that mattered."

Tracking communicates:

> "I have been monitoring your activity."

The factual knowledge may be identical.

The interactional meaning is not.

---

# 28. Competence Positioning

A move can position the other person as:

```text
COMPETENT
```

or:

```text
DEFICIENT
```

even when the topic is identical.

Compare:

> "Do you need me to explain that?"

with:

> "What part would be most useful to compare?"

The second leaves more room for the human to establish what they already know.

Competence positioning can materially affect belonging and agency.

---

# 29. Authority About Own Experience

The system should preserve the principle that people remain authoritative about their own experience.

A system may know:

```text
statistics
public events
institutional context
```

but not:

```text
how the person felt
what mattered most to them
how they interpreted the experience
```

Avoid:

> "That must have been devastating."

Prefer:

> "How was that for you?"

when the person's internal experience is unknown.

---

# 30. Private Knowledge Versus Public Move

The relational system may explicitly output:

```text
PRIVATE CONTEXT
Useful for calibration.

RECOMMENDED MOVE
What to actually say.

WHY
What response opportunity this creates.

AVOID
What would create unnecessary pressure or reveal excessive research.
```

This is useful because the best application of knowledge is often **restraint**.

---

# 31. Athletics Example

Suppose a professor knows:

```text
student is an athlete
team recently lost
student's individual participation is unclear
```

A poor system might generate:

> "Tough loss Saturday. What happened out there?"

Problems:

```text
presumes student participation
presumes desire to discuss loss
reveals tracking
narrows identity to athletics
creates disclosure pressure
```

A more appropriate move might be:

> "How's your week going?"

or, given established rapport:

> "You surviving this week?"

The system uses athletics context privately to avoid a poor interaction without necessarily mentioning athletics.

---

# 32. Identity-Expanding Follow-Up

If the student introduces athletics:

> "Practice has been brutal."

the professor can now respond within a topic the student chose.

The interaction may then expand:

> "Yeah? What's been making it brutal?"

The difference is that the student, not the system, selected the depth and direction.

---

# 33. No-Move Recommendation

The system must be able to recommend:

```text
NO SPECIAL RELATIONAL MOVE
```

For example:

> There is relevant public information, but mentioning it would create more surveillance signal than relational value. Use an ordinary greeting.

This is not system failure.

It is successful restraint.

---

# 34. Belonging Without Performance

The human using the system should not need to become:

```text
younger
cooler
more casual
more slang-heavy
more culturally imitative
```

to create belonging.

A professor can communicate belonging through:

- remembering;
- listening;
- making space;
- asking better questions;
- using names;
- following up;
- taking ideas seriously;
- permitting correction;
- and recognizing competence.

Relational success should not depend on impersonating the student.

---

# 35. Relational Continuity

Repeated interaction changes available moves.

A callback that would be strange on first contact may become meaningful later.

For example:

```text
INTERACTION 1
student makes joke

INTERACTION 2
professor remembers joke

INTERACTION 3
brief callback establishes continuity
```

The system may track:

```text
relational permissions
```

that have been earned through interaction.

These should remain context-specific and revisable.

---

# 36. Relational Permissions Are Not Permanent

Permission can change.

A humor style that worked before may be inappropriate during:

- conflict;
- grief;
- evaluation;
- public setting;
- or changed relationship status.

The model should therefore treat permissions as dynamic.

Do not store:

```text
teasing_allowed = true
```

as a permanent universal property.

Prefer:

```yaml
interactional_permission:
  behavior: gentle_teasing
  context:
    relationship: established
    setting: informal
    stakes: low
  confidence: moderate
  current_status: context_dependent
```

---

# 37. Repair

If a relational move fails, the system should learn from the repair.

Example:

> "Oh, I didn't mean that in a sports way."

or:

> "That's kind of a weird thing for a professor to know."

These are highly informative events.

They may update:

```text
research visibility threshold
topic permission
familiarity estimate
humor permission
identity salience
```

The correct response is not simply a different talking point.

It is a model update.

---

# 38. Role of the Person / Reasoning Model

Relational interaction also interacts with how the human using the system communicates naturally.

For example, a professor may be:

- highly formal;
- dry;
- warm;
- understated;
- direct;
- humorous;
- or reserved.

The system should not recommend a relational move that requires an implausible persona.

The question is:

> **What relational move can this person authentically perform?**

Authenticity here means fit with demonstrated communicative behavior, not a fixed personality category.

---

# 39. Persona Integrity

A move can fail because it is objectively reasonable but implausible coming from the speaker.

Example:

```text
SYSTEM RECOMMENDATION
heavy youth slang

SPEAKER
formal middle-aged professor who never uses it
```

The result may signal:

- imitation;
- effort;
- condescension;
- or artificiality.

The system should preserve persona continuity.

---

# 40. Relational Move Representation

A relational move may be represented as:

```yaml
move:
  cognitive_function: recognition

  linguistic_realization:
    "How's your week going?"

  interactional_affordance:
    response_latitude: high
    disclosure_pressure: low
    face_risk: low

  identity_effect:
    expanding: true
    narrowing: false

  research_visibility:
    low

  relational_permission:
    supported

  rationale:
    "Allows student to introduce athletics or another topic without
    signaling external monitoring."
```

This is illustrative.

---

# 41. Relational Evaluation

Possible outcome dimensions include:

```text
PERCEIVED RECOGNITION
BELONGING
RESPONSE LATITUDE
FACE THREAT
DISCLOSURE PRESSURE
AUTHENTICITY
RESEARCH VISIBILITY
PERCEIVED SURVEILLANCE
PERMISSION TO DISENGAGE
IDENTITY EXPANSION
```

A useful relational move should not be evaluated only by:

```text
DID THE PERSON RESPOND?
```

A longer response is not necessarily a better interaction.

---

# 42. Belonging Evaluation

Belonging-related evaluation might ask whether the interaction communicated:

```text
I AM RECOGNIZED
I HAVE A POSITION HERE
I CAN CONTRIBUTE
I CAN CORRECT
I AM NOT BEING REDUCED
I CAN CHOOSE HOW MUCH TO SHARE
```

These are stronger relational indicators than simple friendliness ratings.

---

# 43. Failure Modes

### Surveillance performance

The system recommends revealing information primarily to demonstrate research.

### Identity narrowing

The person is repeatedly approached through one salient identity.

### Generational cosplay

The speaker imitates youth or community language to manufacture similarity.

### Artificial intimacy

The move implies more relational closeness than exists.

### Humor overreach

The system understands a humor form and mistakes that for permission to use it.

### Face blindness

A cognitively useful move creates unnecessary embarrassment or status threat.

### Power blindness

The system treats a high-power speaker's question as equivalent to peer interaction.

### Disclosure pressure

The move makes personal disclosure difficult to refuse.

### Belonging theater

The system optimizes for appearing inclusive rather than increasing agency and recognition.

### Engagement optimization

The system selects moves because they increase conversation rather than because they improve the relationship.

### No-restraint failure

The system assumes every available fact should produce a talking point.

---

# 44. Research Questions

Key research questions include:

1. Does response-latitude optimization improve perceived relational safety?
2. Can systems distinguish recognition from surveillance cues reliably?
3. How should research visibility be estimated?
4. When does identity-confirming interaction strengthen belonging?
5. When does it narrow identity?
6. Can sociolinguistic modeling improve humor calibration without increasing mimicry?
7. How should role and power modify otherwise identical moves?
8. Can interaction-state models reliably identify disclosure pressure?
9. What forms of belonging can be measured behaviorally?
10. Does identity-expanding interaction improve classroom belonging?
11. Can systems learn relational permissions without overgeneralizing?
12. Can private contextual knowledge improve interaction without being surfaced?
13. When should a system recommend no special move?
14. How should relational repair update future policy?
15. How can systems preserve authentic speaker persona while adapting interaction?
16. Which interaction-state variables materially improve relational outcomes?
17. Can smaller/local models perform this relational policy task adequately?
18. How much relational history is necessary before adaptation becomes useful?
19. Can relationship-specific state remain private and isolated from global personalization?
20. Does relational adaptation improve belonging enough to justify the privacy cost of the required state?

---

# 45. Governing Relational Heuristic

The relational application can be summarized as:

```text
KNOW MORE THAN YOU SAY

SAY LESS THAN YOU COULD

REVEAL ONLY WHAT IMPROVES THE INTERACTION

CREATE ROOM FOR THE OTHER PERSON
TO DECIDE WHAT MATTERS
```

Or more compactly:

> **Minimum viable relational move.  
> Maximum human response latitude.**

The system's best contribution may not be a brilliant personalized line.

It may be knowing enough about the interaction to recommend something ordinary, human, and easy to answer.
