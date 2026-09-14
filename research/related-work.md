# Related Work

Deliberation Room sits at the intersection of multiple established research traditions.

The project does **not** claim that dialogue-state tracking, user modeling, adaptive tutoring, mixed-initiative interaction, pragmatics, learner modeling, cognitive offloading, provenance, or privacy-preserving personalization are individually novel.

The research question is instead whether these ideas can be integrated around a specific architectural objective:

> **Do not optimize merely for what the model should say next.  
> Optimize for what the human should be able to do next.**

This document maps the nearest conceptual neighbors and identifies where Deliberation Room appears to overlap with, depend on, or depart from them.

The map should evolve as the project encounters additional prior work.

---

# 1. Dialogue-State Tracking

Dialogue-state tracking is one of the clearest technical precedents for Deliberation Room's state-based architecture.

Task-oriented dialogue systems have long maintained evolving representations of user goals, intents, preferences, or slot values across conversational turns.

A simplified traditional architecture resembles:

```text
USER UTTERANCE
      ↓
DIALOGUE STATE TRACKER
      ↓
DIALOGUE POLICY
      ↓
SYSTEM ACTION
      ↓
NATURAL LANGUAGE REALIZATION
```

This is structurally relevant to Deliberation Room because both approaches distinguish:

```text
STATE REPRESENTATION
```

from:

```text
ACTION SELECTION
```

and:

```text
LINGUISTIC REALIZATION
```

Rather than assuming that every user message should directly trigger unrestricted generation.

---

## Relationship to Deliberation Room

Traditional dialogue-state tracking generally asks questions such as:

```text
What does the user want?

What constraints have they specified?

Which task state are we currently in?

Which slots remain unresolved?
```

Deliberation Room expands the modeled state toward:

```text
What does the human currently appear to understand?

Which distinctions have they made?

Which assumptions remain implicit?

Which warrants remain unstable?

Which interpretations have they rejected?

Which uncertainty is meaningful?

How does this person appear to reason productively?

What does language mean in this discourse environment?

What would a candidate move do socially here?
```

The similarity is architectural.

The represented object is different.

---

## Important distinction

Deliberation Room should therefore not claim:

```text
"We invented stateful dialogue."
```

A more precise claim is:

> **The architecture treats human deliberation itself as a partially observed, revisable interaction state that can inform an explicit next-move policy.**

---

# 2. Open-Domain Dialogue-State Tracking

Traditional dialogue-state tracking often assumes relatively bounded tasks such as:

- booking;
- search;
- scheduling;
- transactional assistance;
- or domain-specific support.

More recent work has explored structured state tracking in increasingly open-domain interactions.

This is particularly relevant because Deliberation Room cannot assume a fixed ontology of all possible:

```text
claims
distinctions
assumptions
relationships
meanings
or uncertainties
```

A viable implementation likely requires dynamic or extensible state representations rather than a closed slot inventory.

---

## Relationship to Deliberation Room

The architectural challenge is therefore:

```text
STRUCTURED ENOUGH
to support policy

but

OPEN ENOUGH
to represent novel human reasoning
```

This tension should be treated as an implementation problem rather than solved through an excessively rigid cognitive ontology.

---

# 3. Common Ground

Research on dialogue also distinguishes individual conversational state from **common ground**: propositions participants mutually treat as established for purposes of the interaction.

This is highly relevant to Deliberation Room.

A system needs to distinguish:

```text
SYSTEM BELIEVES X

HUMAN SAID X

SYSTEM PROPOSED X

HUMAN RECOGNIZED X

BOTH PARTICIPANTS ARE CURRENTLY TREATING X AS ESTABLISHED
```

Those are not equivalent states.

---

## Deliberation Room contribution

The architecture's provenance model adds another dimension:

```text
WHOSE COGNITIVE CONTRIBUTION WAS X?
```

A proposition may become common ground while retaining different conceptual provenance.

For example:

```text
SYSTEM-PROPOSED
        ↓
HUMAN-REVISED
        ↓
MUTUALLY ESTABLISHED
```

Common-ground status therefore does not erase contribution history.

---

# 4. Dialogue Policy and Decision-Making Under Uncertainty

Dialogue systems have long separated state estimation from policies governing what the system should do next.

Relevant action choices can include:

```text
ASK
CONFIRM
CLARIFY
ACT
INFORM
WAIT
```

Decision-theoretic approaches have also examined whether a system should:

```text
act autonomously
ask the user
or refrain from acting
```

under uncertainty.

This strongly precedes Deliberation Room's claim that:

```text
WITHHOLD
```

should be a legitimate system action.

---

## Deliberation Room distinction

The difference lies primarily in the policy objective.

Traditional dialogue policy commonly optimizes successful task completion.

Deliberation Room proposes a policy objective incorporating:

```text
expected cognitive value
information gain
human agency
response latitude
correctability

minus

cognitive substitution
intrusion
interactional risk
premature certainty
unnecessary disclosure
```

Whether that objective can be operationalized successfully is an empirical question.

---

# 5. Mixed-Initiative Interaction

Mixed-initiative interaction is another major predecessor.

This tradition asks how responsibility should move dynamically between human and computational system rather than assuming either:

```text
complete automation
```

or:

```text
complete human control
```

A mixed-initiative system may:

- act;
- recommend;
- ask;
- defer;
- request clarification;
- or return control to the user

depending on uncertainty and context.

---

## Relationship to Deliberation Room

Deliberation Room shares the principle that:

> **The system should not always take maximal initiative simply because it can.**

But the proposed architecture sharpens the question around cognition.

Instead of asking only:

```text
Who should perform the task?
```

Deliberation Room asks:

```text
Which cognitive operation should remain with the human?
```

The boundary between automation and assistance therefore operates at the level of:

- distinction;
- judgment;
- interpretation;
- evidence connection;
- revision;
- composition;
- and expression.

---

# 6. Human-AI Interaction Guidelines

Human-AI interaction research has developed guidance around issues such as:

- appropriate timing of AI assistance;
- communicating uncertainty;
- supporting correction;
- maintaining user control;
- setting expectations;
- and enabling recovery from error.

These principles strongly overlap with Deliberation Room's commitments to:

```text
CORRIGIBILITY
UNCERTAINTY VISIBILITY
USER CONTROL
APPROPRIATE INTERVENTION
```

---

## Deliberation Room distinction

The project treats these not only as interface principles but as components of the reasoning architecture.

For example:

```text
USER CORRECTION
```

is not merely a usability affordance.

It updates:

```text
COGNITIVE STATE
PERSON / REASONING MODEL
LINGUISTIC MODEL
INTERACTION MODEL
```

and may alter future policy selection.

---

# 7. Intelligent Tutoring Systems

Intelligent tutoring systems have long maintained models of learner knowledge in order to adapt:

- feedback;
- problem selection;
- hints;
- explanations;
- sequencing;
- and instructional intervention.

This tradition is an important predecessor to the Cognitive State Model and Person / Reasoning Model.

Learner modeling may represent:

```text
knowledge
misconceptions
skill mastery
affect
strategy
or task performance
```

and use those representations to determine pedagogical actions.

---

## Relationship to Deliberation Room

Deliberation Room shares:

```text
MODEL LEARNER STATE
        ↓
ADAPT INTERVENTION
```

but proposes a broader deliberative state including:

```text
claim
assumption
warrant
distinction
counterexample
uncertainty
revision
conceptual provenance
```

The architecture is also intended to generalize beyond formal learning environments.

---

# 8. Student Modeling

Student modeling provides a particularly important precedent.

The fundamental idea that a computational system can maintain a provisional representation of what a learner knows is well established.

Deliberation Room should therefore not describe the Cognitive State Model as if modeling learner knowledge were novel.

---

## Distinction

The proposed Cognitive State Model is less specifically a mastery model and more a representation of an evolving **argumentative or deliberative structure**.

It may contain:

```text
CLAIM A
depends on
WARRANT B

but

COUNTEREXAMPLE C
destabilizes
ASSUMPTION D
```

The relevant state is therefore not necessarily:

```text
learner knows concept X
```

but:

```text
this human's current model of this problem has structure Y
```

---

# 9. Open Learner Models

Open learner modeling is especially relevant to Deliberation Room's commitment to **corrigible personalization**.

Open learner models make aspects of the system's representation of the learner visible to the learner.

In some designs, learners may inspect, negotiate, or correct those representations.

This strongly precedes the idea that a person should be able to see and modify what the system believes about their reasoning.

---

## Relationship to Deliberation Room

The Person / Reasoning Model extends this concern beyond formal mastery.

A future interface might expose representations such as:

```text
The system currently believes:

- concrete counterexamples were productive during argument testing;
- high abstraction has been useful in rhetoric tasks;
- analogy was productive during exploration but not stabilization.
```

The user could:

```text
CONFIRM
REVISE
LIMIT SCOPE
MARK TEMPORARY
DELETE
```

This should be understood as building on traditions of inspectable and negotiable learner/user modeling rather than originating the idea of model transparency.

---

# 10. Natural-Language Tutoring Dialogue

Natural-language tutoring systems have extensively studied instructional dialogue.

Relevant behaviors include:

- prompting;
- hints;
- explanation;
- corrective feedback;
- elaboration;
- question asking;
- and tutorial dialogue strategy.

Deliberation Room therefore does not claim novelty merely because an AI asks a learner questions instead of supplying answers.

---

## Important distinction

The central comparison is not:

```text
ANSWERING
vs.
QUESTIONING
```

It is:

```text
GENERIC QUESTIONING
vs.
STATE-ADAPTIVE NEXT-MOVE SELECTION
```

A Deliberation Room controller may choose:

```text
ASK
CHALLENGE
REFLECT
COUNTEREXAMPLE
DISTINGUISH
PROPOSE
WITHHOLD
or
COMPOSE
```

depending on the current state.

Questions are one action class among several.

---

# 11. Socratic Tutoring

Socratic tutoring is a particularly close conceptual neighbor.

Both approaches can use questions to preserve student reasoning.

However, "Socratic" interaction can cover very different system behaviors.

One version resembles:

```text
SYSTEM KNOWS TARGET ANSWER
        ↓
ASK LEADING QUESTION
        ↓
STUDENT APPROACHES TARGET
        ↓
ASK NEXT LEADING QUESTION
```

Deliberation Room explicitly rejects treating that pattern as its default architecture.

---

## No hidden destination

The proposed policy is:

```text
MODEL CURRENT HUMAN REPRESENTATION
        ↓
IDENTIFY INSTABILITY
        ↓
SELECT TEST
        ↓
OBSERVE WHAT SURVIVES
        ↓
UPDATE MODEL
```

The human may reach:

- the system's initial hypothesis;
- a different hypothesis;
- a narrower claim;
- competing interpretations;
- or justified uncertainty.

The objective is quality of inspection rather than convergence on a concealed answer.

---

# 12. Self-Regulated Learning and Metacognition

Educational research has long studied:

- planning;
- monitoring;
- strategy selection;
- self-evaluation;
- reflection;
- and metacognition.

Educational chatbot research increasingly examines whether conversational systems can support self-regulated learning.

Deliberation Room's proposed metacognitive feedback belongs within this broader tradition.

---

## Deliberation Room distinction

The proposed contribution is specifically to derive metacognitive observations from the **structured deliberation trace**.

For example:

```text
3 of 4 substantive revisions followed counterexamples.

Claims emerged independently,
while warrants required more elicitation.

2 system interpretations were rejected,
and those rejections produced useful distinctions.
```

The resulting feedback describes observable interaction patterns rather than assigning a fixed cognitive type.

---

# 13. Cognitive Offloading

Human-tool interaction has long involved cognitive offloading: external systems take over work that humans would otherwise perform internally.

Generative AI greatly expands the range of cognition that can potentially be offloaded.

This is directly relevant to Deliberation Room.

The architecture does not assume cognitive offloading is inherently harmful.

Offloading can be valuable for:

- memory;
- organization;
- calculation;
- linguistic production;
- accessibility;
- retrieval;
- and routine representation.

---

## Productive versus substitutive offloading

The relevant question is:

> **Which cognitive operations are incidental to the task, and which constitute the capability the task is meant to exercise or reveal?**

For example:

```text
grammar correction
```

may be incidental in one learning objective.

```text
constructing the warrant
```

may be central.

Deliberation Room's composition boundary attempts to make this distinction architecturally explicit.

---

# 14. Cognitive Apprenticeship and Scaffolding

Instructional traditions around scaffolding and cognitive apprenticeship are also relevant.

Effective support may temporarily:

- model;
- cue;
- prompt;
- structure;
- or externalize

a process before responsibility shifts increasingly toward the learner.

This overlaps with Deliberation Room's concern for preserving human cognitive responsibility.

---

## Relevant difference

The architecture attempts to make **which cognitive operation is being scaffolded or substituted** explicit in the interaction state and provenance trace.

That creates a possible bridge between traditional instructional scaffolding and generative systems capable of performing the entire task.

---

# 15. Productive Struggle and Desirable Difficulty

Learning science distinguishes productive cognitive effort from unnecessary difficulty.

This is relevant to the architecture's concept of:

```text
PRODUCTIVE FRICTION
vs.
INCIDENTAL FRICTION
```

Deliberation Room should not preserve difficulty for its own sake.

The relevant design question is:

> **Would removing this effort eliminate cognition that matters to the task?**

This is why direct-generation override remains available.

Cognition preservation should not become an ideology of inconvenience.

---

# 16. Argumentation and Deliberation Systems

Computational argumentation research has long represented structures such as:

- claims;
- evidence;
- premises;
- warrants;
- attacks;
- support relations;
- counterarguments;
- and belief revision.

This is a direct conceptual precedent for portions of the Cognitive State Model.

---

## Relationship to Deliberation Room

The architecture borrows the intuition that reasoning can be represented structurally.

But its target is not simply:

```text
construct the best argument graph
```

It is:

```text
represent enough of the human's current argument structure
to choose a useful next interactional move
```

The human model remains primary.

---

# 17. Deliberative Dialogue

Dialogue research has also examined:

- persuasion;
- negotiation;
- argument;
- collaborative problem solving;
- and deliberative dialogue.

These traditions offer important concepts for:

- turn function;
- commitment;
- disagreement;
- counterproposal;
- and interaction strategy.

---

## Important boundary

Deliberation Room is not fundamentally a persuasion architecture.

The system is not supposed to optimize:

```text
human adopts system position
```

Its objective is:

```text
human representation becomes more inspectable,
testable,
and accountable
```

even if the resulting judgment differs from the system's initial hypothesis.

---

# 18. Computational Pragmatics

Pragmatics studies how meaning depends on more than literal semantics.

Relevant phenomena include:

- implicature;
- indirectness;
- presupposition;
- stance;
- politeness;
- reference;
- common ground;
- and discourse context.

Computational pragmatics provides important conceptual grounding for the Linguistic / Sociolinguistic Model.

---

## Relationship to Deliberation Room

The architecture assumes:

```text
lexical meaning
≠
complete interactional meaning
```

and that accurate next-move selection may require reasoning about:

```text
what the human means
```

rather than only:

```text
what the words literally denote
```

This principle is established broadly within pragmatics.

The research question is how much explicit pragmatic representation is necessary for useful next-move policy.

---

# 19. Sociolinguistics

Sociolinguistics provides frameworks for understanding variation in relation to:

- community;
- role;
- identity;
- register;
- context;
- stance;
- social meaning;
- accommodation;
- and interaction.

This is not treated in Deliberation Room as a post-hoc constraint on wording.

It is part of the interaction model itself.

---

## Architectural relevance

Consider:

```text
"bro"
```

Its meaning cannot necessarily be determined by dictionary semantics alone.

Depending on context it may index:

- affiliation;
- mock exasperation;
- aggression;
- intimacy;
- irony;
- peer positioning;
- or little of consequence.

That interpretation can affect **which move is appropriate**, not merely how a predetermined move should be styled.

---

# 20. Communication Accommodation

Research on linguistic accommodation examines how speakers alter communication in relation to other participants.

This provides an important neighboring concept for linguistic adaptation.

However, Deliberation Room explicitly distinguishes:

```text
UNDERSTANDING A USER'S LINGUISTIC PRACTICE
```

from:

```text
IMITATING THAT PRACTICE
```

The architecture's objective is:

```text
PRAGMATIC FIT
```

rather than:

```text
MAXIMUM SURFACE SIMILARITY
```

This distinction is partly motivated by risks of:

- mimicry;
- stereotyping;
- artificial intimacy;
- and identity performance.

---

# 21. User Modeling and Personalization

User modeling has a long history in adaptive systems.

Systems may represent:

- goals;
- preferences;
- expertise;
- behavior;
- history;
- context;
- or inferred needs

in order to adapt interaction.

Deliberation Room's Person / Reasoning Model clearly belongs within this family.

---

## Proposed boundary

The system should prefer:

```text
counterexamples have repeatedly produced productive revision
during argument testing
```

over:

```text
user is a counterexample thinker
```

The intended object is a **corrigible interaction-relevant model**, not a totalizing profile of the person.

---

# 22. Personalization Versus Profiling

Adaptive systems create a persistent tension:

```text
more user information
        ↓
potentially better adaptation
```

but also:

```text
more user information
        ↓
greater privacy risk
greater overgeneralization
greater profiling risk
```

Deliberation Room's data-minimization hypothesis therefore belongs within broader research on privacy-aware personalization.

---

# 23. Human-AI Co-Reasoning

Generative AI has renewed interest in systems where humans and models jointly:

- analyze;
- generate;
- critique;
- reason;
- decide;
- or create.

Deliberation Room belongs broadly within human-AI co-reasoning.

But "joint reasoning" alone does not specify where intellectual responsibility lies.

---

## Provenance question

The architecture therefore asks:

```text
Who introduced this claim?

Who supplied the counterexample?

Who generated the distinction?

Who revised it?

Who stabilized the judgment?

Who supplied the final words?
```

The goal is not to prohibit joint cognition.

It is to make the distribution of cognitive contribution more inspectable.

---

# 24. Human-AI Workflow

Research has demonstrated that **workflow order** can influence human-AI decision making.

This is highly relevant to Deliberation Room's composition boundary.

For example:

```text
AI FIRST
then
human evaluates
```

may create different cognitive behavior from:

```text
HUMAN JUDGMENT FIRST
then
AI contribution
```

Deliberation Room extends this concern from workflow order to the granularity of individual cognitive moves.

The architecture asks not merely:

```text
Who goes first?
```

but:

```text
Which reasoning operation happens before AI generation enters?
```

---

# 25. Explainable and Inspectable AI

Explainable AI research seeks to make aspects of model behavior understandable to humans.

Deliberation Room shares the concern for inspectability, but the object differs.

The project is interested not only in:

```text
WHY DID THE AI DO THIS?
```

but also:

```text
WHAT DOES THE AI CURRENTLY BELIEVE ABOUT MY REASONING?

WHY DID IT SELECT THIS INTERVENTION?

WHAT DID IT INFER VERSUS OBSERVE?

WHAT HAS IT STORED ABOUT ME?

HOW CAN I CORRECT IT?
```

This creates overlap with explainability, user modeling, and mixed-initiative interaction.

---

# 26. AI-Assisted Writing

AI-assisted writing research examines systems supporting:

- ideation;
- drafting;
- revision;
- editing;
- feedback;
- and collaborative writing.

Deliberation Room's composition layer belongs directly within this space.

---

## Important distinction

The architecture separates:

```text
DELIBERATION
```

from:

```text
COMPOSITION
```

not because composition assistance is undesirable, but because the two phases can have different cognitive consequences.

The system may eventually perform substantial linguistic work while preserving a human-developed conceptual model.

---

# 27. Authorship and Provenance

Generative AI has intensified questions about:

- authorship;
- attribution;
- provenance;
- disclosure;
- and human contribution.

Many provenance approaches focus on:

```text
which system produced which text
```

or:

```text
whether AI was used
```

Deliberation Room proposes an additional dimension:

```text
COGNITIVE PROVENANCE
```

---

## Cognitive provenance

The relevant questions include:

```text
Who originated the substantive claim?

What challenge caused revision?

Which system proposals were recognized?

Which were rejected?

Which distinctions were human-originated?

Which final wording was system-transposed?
```

This does not replace textual provenance.

It represents a different layer.

---

# 28. Process-Based Assessment

Education has long used process evidence such as:

- drafts;
- revision histories;
- conferences;
- oral defense;
- reflection;
- portfolios;
- and process writing

to understand how student work developed.

Cognitive provenance should therefore not be presented as if process-oriented assessment were new.

---

## Proposed contribution

The novel question is whether AI-mediated reasoning can produce a structured trace such as:

```text
INITIAL CLAIM
        ↓
COUNTEREXAMPLE
        ↓
HUMAN REVISION
        ↓
DISTINCTION
        ↓
WARRANT
        ↓
STABILIZED JUDGMENT
```

and whether that trace provides useful evidence of intellectual accountability in AI-assisted work.

---

# 29. AI Detection

AI-detection systems typically attempt to infer whether text was AI-generated.

Deliberation Room approaches the educational problem differently.

Instead of asking only:

> **Was AI involved?**

it asks:

> **What cognition can the learner account for?**

These questions are not mutually exclusive.

But they serve different educational purposes.

---

# 30. Privacy-Preserving Personalization

Privacy-aware personalization research explores ways to retain useful adaptation while reducing exposure of user data.

Relevant mechanisms may include:

- local processing;
- on-device inference;
- data minimization;
- federated approaches;
- compressed user representations;
- selective memory;
- and user control.

This is directly relevant to Deliberation Room's privacy hypothesis.

---

## Proposed research question

Rather than assuming that useful personalization requires:

```text
ALL PRIOR CONVERSATION
```

the project asks whether interaction quality can be maintained using:

```text
MINIMAL STRUCTURED STATE
```

such as:

```text
current unresolved warrant
counterexamples productive in this task
shared local term
interactional power asymmetry
```

Whether this is sufficient must be tested.

---

# 31. Local and On-Device Language Models

The increasing feasibility of running smaller language models locally motivates one of Deliberation Room's implementation hypotheses.

The relevant claim is **not**:

```text
small models are as capable as frontier models
```

The research hypothesis is narrower:

> **A constrained controller may require less general-purpose generative capability than unrestricted conversation.**

Tasks such as:

```text
state classification
move ranking
contradiction detection
uncertainty estimation
policy selection
```

may have different model requirements from:

```text
arbitrary high-quality generation
```

This is an empirical question.

---

# 32. Partially Observable Decision Processes

The architecture's representation:

```text
observations
        ↓
uncertain latent state
        ↓
action selection
        ↓
new observation
        ↓
state update
```

has clear conceptual similarity to partially observable decision processes.

Deliberation Room does not currently claim to implement a formal POMDP.

However, the analogy is useful because the system:

- does not directly observe cognition;
- maintains uncertain state;
- chooses actions;
- observes responses;
- and updates beliefs.

A future implementation may determine that formal decision-theoretic machinery is useful.

It may also determine that a lighter-weight structured controller is sufficient.

---

# 33. Active Learning and Information Gain

The project's high-information / low-intrusion principle has conceptual overlap with active learning and information-seeking strategies.

In both cases, the system can choose an observation or query that is expected to reduce uncertainty.

However, Deliberation Room introduces an additional cost structure.

A question has not only informational cost but potentially:

```text
COGNITIVE COST
SOCIAL COST
DISCLOSURE COST
FACE COST
INTERACTIONAL COST
```

Therefore the best question is not necessarily the one with maximum information gain.

---

# 34. Value of Information

Decision theory provides a useful conceptual neighbor for deciding whether acquiring additional information is worth the cost.

Deliberation Room's policy similarly asks whether another intervention is likely to change the state enough to justify:

- another question;
- another disclosure;
- additional cognitive effort;
- or continued interaction.

This is particularly relevant to the architecture's stopping rule.

---

# 35. Stopping and Over-Interaction

Conversational systems often have an implicit incentive to continue.

Deliberation Room treats stopping as a legitimate policy outcome.

Relevant neighboring work includes:

- mixed-initiative control;
- decision theory;
- dialogue management;
- tutoring policies;
- and human-AI interaction.

The distinctive design commitment is:

```text
MORE INTERACTION
≠
BETTER INTERACTION
```

The controller should be able to determine:

> **The human has enough. Stop.**

---

# 36. Where Deliberation Room Appears to Differ

The architecture's likely contribution is not any single component.

Most major components have clear intellectual predecessors.

The proposed contribution is their integration around a cognition-preserving control objective.

A simplified comparison:

| Tradition | Primary modeled object | Typical policy objective | Deliberation Room relationship |
|---|---|---|---|
| Dialogue-state tracking | user intent / task state | successful dialogue action | extends state toward human reasoning |
| Intelligent tutoring | learner knowledge / mastery | learning support | represents deliberative structure and provenance |
| Socratic tutoring | learner reasoning via questioning | elicit answer / understanding | uses multiple move classes and no required hidden destination |
| User modeling | user traits / preferences / goals | adaptation | constrains model toward task-relevant corrigible reasoning patterns |
| Mixed initiative | allocation of human/system initiative | effective collaboration | applies initiative allocation to individual cognitive operations |
| Computational pragmatics | contextual meaning | language interpretation | feeds interpretation into move selection |
| Sociolinguistics | social meaning and language variation | description / interpretation | treats social meaning as interaction-state evidence |
| Argumentation systems | claims / evidence / relations | argument construction / evaluation | uses structures to select human-facing interventions |
| AI-assisted writing | artifact production / revision | improve writing | places composition downstream of deliberation when appropriate |
| Provenance | source / history of artifact | attribution / traceability | adds conceptual contribution and reasoning development |
| Privacy-aware personalization | useful adaptation with less exposure | personalized performance | asks for minimum state needed for next-move selection |

The proposed integration is:

```text
COGNITIVE STATE
        +
PERSON / REASONING STATE
        +
LINGUISTIC / SOCIOLINGUISTIC STATE
        +
INTERACTION STATE
        ↓
COGNITION-PRESERVING NEXT-MOVE POLICY
        ↓
HUMAN RESPONSE
        ↓
STATE UPDATE
        ↓
COGNITIVE PROVENANCE
        +
METACOGNITIVE FEEDBACK
        ↓
OPTIONAL COMPOSITION
```

---

# 37. Strongest Novelty Claim the Project Should Currently Make

At this stage, the repository should **not** claim:

> "No one has ever built anything like this."

The defensible research claim is closer to:

> **Deliberation Room proposes an interaction architecture that integrates explicit cognitive-state tracking, person/reasoning adaptation, sociolinguistic interpretation, interactional modeling, cognition-preserving next-move selection, and conceptual/linguistic provenance around the optimization target of what the human should be able to do next.**

Whether that integration is:

- technically novel;
- empirically superior;
- practically useful;
- or reducible to existing approaches

is itself part of the research program.

---

# 38. What Would Reduce the Novelty Claim?

The novelty claim should become narrower if prior work demonstrates an architecture already combining:

```text
1. explicit evolving representation of human reasoning;

2. adaptive person-specific reasoning strategy;

3. sociolinguistic meaning as pre-action state;

4. explicit modeling of interactional affordance;

5. next-move selection optimized around preserving human cognition;

6. separation of deliberation from composition;

7. conceptual versus linguistic provenance;

8. trace-derived metacognitive feedback;

9. data-minimized corrigible personalization.
```

Finding such work would be valuable.

The purpose of related-work research is not to protect a novelty claim.

It is to locate the project accurately.

---

# 39. Research Traditions to Search Further

The current literature map should continue expanding across:

```text
DIALOGUE STATE TRACKING
DIALOGUE POLICY
POMDP DIALOGUE SYSTEMS
COMMON GROUND
MIXED-INITIATIVE INTERACTION
USER MODELING
OPEN LEARNER MODELS
INTELLIGENT TUTORING SYSTEMS
NATURAL-LANGUAGE TUTORING
SOCRATIC TUTORING
SELF-REGULATED LEARNING
METACOGNITION
COGNITIVE OFFLOADING
COGNITIVE APPRENTICESHIP
SCAFFOLDING
PRODUCTIVE STRUGGLE
ARGUMENTATION SYSTEMS
DELIBERATIVE DIALOGUE
COMPUTATIONAL PRAGMATICS
SOCIOLINGUISTICS
COMMUNICATION ACCOMMODATION
HUMAN-AI CO-REASONING
AI-ASSISTED WRITING
PROCESS-BASED ASSESSMENT
AUTHORSHIP
PROVENANCE
AI DETECTION
PRIVACY-PRESERVING PERSONALIZATION
ON-DEVICE LANGUAGE MODELS
ACTIVE LEARNING
VALUE OF INFORMATION
```

The related-work map should be revised whenever an adjacent system materially changes how Deliberation Room should be described.

---

# 40. Initial References

The following works provide useful starting points for the literature map.

## Dialogue state and dialogue policy

Jacqmin, L., Rojas Barahona, L. M., & Favre, B. (2022). *“Do you follow me?”: A survey of recent approaches in dialogue state tracking.* Proceedings of SIGDIAL 2022. DOI: 10.18653/v1/2022.sigdial-1.33.

Balaraman, V., Sheikhalishahi, S., & Magnini, B. (2021). *Recent neural methods on dialogue state tracking for task-oriented dialogue systems: A survey.* Proceedings of SIGDIAL 2021. DOI: 10.18653/v1/2021.sigdial-1.25.

Das, S. S. S., Shah, C., Wan, M., Neville, J., Yang, L., Andersen, R., Buscher, G., & Safavi, T. (2024). *S3-DST: Structured open-domain dialogue segmentation and state tracking in the era of LLMs.* Findings of ACL 2024. DOI: 10.18653/v1/2024.findings-acl.891.

---

## Mixed-initiative interaction

Horvitz, E. (1999). *Principles of mixed-initiative user interfaces.* Proceedings of CHI 1999.

Hearst, M. A. (1999). *Mixed-initiative interaction.* IEEE Intelligent Systems, 14(5), 14–24.

---

## Human-AI interaction

Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., Suh, J., Iqbal, S., Bennett, P. N., Inkpen, K., Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). *Guidelines for human-AI interaction.* Proceedings of CHI 2019.

---

## Intelligent tutoring and learner modeling

Nkambou, R., Bourdeau, J., & Mizoguchi, R. (Eds.). (2010). *Advances in Intelligent Tutoring Systems.* Springer.

Relevant traditions within this literature include:

- student modeling;
- Bayesian learner modeling;
- open learner models;
- tutorial dialogue;
- tutor decision-making;
- and ill-defined-domain tutoring.

---

## Educational conversational systems and self-regulation

Guan, R., Raković, M., Chen, G., & Gašević, D. (2025). *How educational chatbots support self-regulated learning? A systematic review of the literature.* Education and Information Technologies, 30, 4493–4518. DOI: 10.1007/s10639-024-12881-y.

---

# 41. Research Position

The related-work position of Deliberation Room can currently be summarized as:

```text
NOT:
"We invented adaptive dialogue."

NOT:
"We invented learner modeling."

NOT:
"We invented Socratic AI."

NOT:
"We invented mixed initiative."

NOT:
"We invented sociolinguistic adaptation."

NOT:
"We invented provenance."

BUT:

"What happens if these traditions are reorganized around an explicit
requirement that the system preserve human cognitive responsibility,
and if the primary policy target becomes the human's next cognitive
move rather than the model's next generated response?"
```

That is the question this repository is designed to make concrete enough to test.
