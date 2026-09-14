# Linguistic / Sociolinguistic Model

The Linguistic / Sociolinguistic Model represents how meaning is produced, interpreted, indexed, negotiated, and revised within the current discourse environment.

Its central question is:

> **How does meaning operate for this human in this discourse environment?**

This model is not a post-processing tone layer.

It is not merely responsible for making generated language "sound like the user."

It exists because linguistic and sociolinguistic information is part of the evidence required to reason about the interaction itself.

---

## Why this model exists

Human language does not carry meaning through lexical content alone.

Meaning can depend on:

- who is speaking;
- who is listening;
- relationship history;
- discourse community;
- role;
- register;
- dialect;
- stance;
- irony;
- humor;
- timing;
- code-switching;
- shared vocabulary;
- professional language;
- generation;
- context;
- and prior interaction.

A phrase can be semantically similar across two contexts while performing very different interactional work.

Likewise, two expressions that look superficially different may function as near-equivalents within a particular relationship or discourse community.

The architecture therefore treats linguistic interpretation as part of interaction-state modeling rather than as decoration applied after reasoning.

---

## Core Distinction

The Linguistic / Sociolinguistic Model primarily asks:

> **What does this language mean here?**

The Interaction Model primarily asks:

> **What does using this language do here?**

These are related but not identical questions.

For example:

```text
"bro"
```

may index:

- affection;
- mock exasperation;
- peer alignment;
- disbelief;
- intimacy;
- aggression;
- ironic distance;
- role relaxation;
- or nothing strongly marked

depending on context.

Understanding the form requires sociolinguistic and pragmatic evidence.

Determining what deploying it would do in this relationship additionally requires interactional modeling.

---

## Candidate State Dimensions

Possible represented features include:

- idiolect;
- lexical preference;
- semantic distinctions;
- cadence;
- register;
- dialect;
- discourse community;
- pragmatics;
- indexicality;
- stance;
- irony;
- sarcasm;
- understatement;
- intensification;
- mitigation;
- politeness strategies;
- code-switching;
- role language;
- generational discourse norms;
- professional jargon;
- community-specific vocabulary;
- repeated metaphors;
- shared vocabulary;
- relational language history;
- indirectness;
- emphasis;
- repair behavior;
- marked and unmarked forms;
- recurring discourse structures;
- conventional shorthand;
- local meanings established through prior interaction.

These features are not assumed to be stable traits.

They are provisional interaction-state representations.

---

## Linguistic Form Is Not Interactional Meaning

The architecture should not assume:

```text
surface form = stable meaning
```

A better approximation is:

```text
interactional meaning
=
lexical content
+ pragmatic function
+ discourse context
+ relational history
+ indexical meaning
+ stance
+ interactional position
```

This is not intended as a formal linguistic equation.

It expresses an architectural commitment:

> **Meaning is situated.**

---

## Idiolect

Within Deliberation Room, `idiolect` refers broadly to recurring individual patterns of language use that may emerge from overlapping influences such as:

- profession;
- geography;
- generation;
- education;
- subculture;
- community;
- relationships;
- personal humor;
- recurring metaphor;
- cadence;
- preferred intensifiers;
- semantic distinctions;
- shorthand;
- and prior linguistic negotiation.

The architecture should not assume that an observed idiolect feature reveals a stable identity category.

For example:

```text
Observed:
User frequently uses "orb" to represent a complex relational or conceptual model.

Useful representation:
"orb" functions as established shared shorthand for a multidimensional conceptual representation.

Unnecessary inference:
User belongs to category X because people in category X use this kind of metaphor.
```

The first is interactionally useful.

The second may add no value.

---

## Semantic Locality

Some language acquires meaning locally through repeated interaction.

For example, a phrase may become shorthand for an entire previously developed distinction.

If two participants have established:

```text
"walking the orb"
```

as shorthand for:

```text
slowly inspecting a complex model from multiple relational perspectives
until contradictions, missing distinctions, or unstable assumptions become visible
```

then later use of the phrase carries more information than its literal words reveal.

The system should be capable of representing such local semantic history.

This can reduce unnecessary re-explanation while preserving meaning.

---

## Relational Language History

Some meanings exist specifically because of shared interaction history.

A phrase may function differently because:

- it has been used before;
- it refers to a prior event;
- it is a callback;
- it was previously corrected;
- it has affectionate history;
- it has conflict history;
- it has become shorthand;
- or one participant has explicitly defined what it means to them.

The architecture may therefore represent:

```yaml
relational_language_history:
  - expression: "walking the orb"
    local_meaning: "inspect a complex mental model from multiple angles"
    source: repeated_interaction
    confidence: high
```

This is qualitatively different from general lexical knowledge.

---

## Pragmatics

A linguistic form can perform work that is not explicitly encoded in its literal semantic content.

Examples include:

- softening;
- hedging;
- inviting;
- distancing;
- signaling uncertainty;
- joking;
- signaling stance;
- implying evaluation;
- creating permission;
- preserving face;
- marking intimacy;
- displaying expertise;
- indexing group membership;
- or reducing commitment.

For example:

> "I mean, maybe?"

may not merely communicate probability.

Depending on context, it may function as:

- genuine uncertainty;
- polite disagreement;
- soft rejection;
- invitation to challenge;
- sarcasm;
- or reluctance to commit.

The architecture should preserve uncertainty when pragmatic interpretation is itself uncertain.

---

## Stance

Stance describes how a speaker positions themselves toward:

- a claim;
- an audience;
- another participant;
- uncertainty;
- authority;
- emotion;
- or the interaction itself.

Possible stance signals include:

- certainty;
- tentativeness;
- irony;
- alignment;
- disalignment;
- enthusiasm;
- reluctance;
- epistemic humility;
- mock seriousness;
- detachment;
- affection;
- or frustration.

Stance can materially change how a cognitive move is interpreted.

For example:

```text
"Really?"
```

may function as:

- genuine clarification;
- skeptical challenge;
- playful disbelief;
- invitation to elaborate;
- or hostile disbelief.

The lexical form alone is insufficient.

---

## Register

Register represents the form of language associated with a particular context, activity, audience, or role.

Possible registers may include:

- academic;
- professional;
- technical;
- intimate;
- casual;
- instructional;
- bureaucratic;
- legal;
- playful;
- ceremonial;
- or community-specific.

A user may move between registers within the same interaction.

The system should treat register shift as evidence rather than error.

For example:

```text
technical explanation
→ joking shorthand
→ formal composition
```

may represent deliberate adaptation to changing interactional purposes.

---

## Code-Switching and Style Shifting

Users may shift language according to:

- audience;
- setting;
- power;
- identity;
- role;
- topic;
- emotional state;
- or rhetorical purpose.

The architecture should not assume that one observed style is the user's "real voice."

Multiple styles may all be authentic.

The relevant question is:

> **What function does this shift appear to serve here?**

Possible functions include:

- alignment;
- professionalism;
- distance;
- solidarity;
- precision;
- humor;
- face management;
- authority;
- or audience adaptation.

---

## Humor

Humor is especially interaction-dependent.

Possible forms include:

- dry understatement;
- self-deprecation;
- ironic formality;
- callback humor;
- absurdity;
- teasing;
- hyperbole;
- deadpan;
- playful exaggeration;
- or shared-situation humor.

The presence of humor in user language does not automatically authorize the system to use the same form.

The system should distinguish:

```text
understanding humor
```

from:

```text
having permission to perform humor
```

Whether a humorous realization is appropriate depends jointly on linguistic meaning and interactional permissions.

---

## Indexicality

Language can index social meanings beyond literal reference.

A feature may suggest:

- expertise;
- profession;
- institutional role;
- informality;
- group affiliation;
- intimacy;
- age positioning;
- stance;
- authority;
- distance;
- or belonging.

Indexical signals are often probabilistic and context-dependent.

They should therefore be represented cautiously.

The system should avoid converting:

```text
this feature may index X in this context
```

into:

```text
this user is X
```

unless the distinction is explicitly established and relevant.

---

## Generational and Community Norms

Discourse norms can change across:

- generations;
- professions;
- subcultures;
- online communities;
- institutions;
- disciplines;
- geographic communities;
- and relationship types.

Relevant features may include:

- conventional humor forms;
- abbreviation;
- punctuation practices;
- emoji use;
- irony;
- indirectness;
- lexical innovation;
- formality expectations;
- response timing;
- or expectations around disclosure.

These norms can inform interpretation.

They should not become stereotypes applied automatically to individuals.

The system should prefer observed local behavior over group-level expectations whenever the two conflict.

---

## Local Evidence Over Demographic Assumption

Suppose a user is likely to belong to a demographic group associated with a particular discourse pattern.

The architecture should not use that association when direct interactional evidence is available.

Prefer:

```text
The user has repeatedly used this form to signal playful exasperation.
```

over:

```text
People of this generation often use this form in that way.
```

Group-level sociolinguistic knowledge can help interpret ambiguity.

It should not override the individual's demonstrated language practices.

---

## Linguistic Repair

Repair is one of the highest-value information sources in this model.

Examples include:

> "No, when I say 'fine,' I don't mean I'm okay."

> "That's not what 'dramatic' means when I say it."

> "That sounds technically correct but not like me."

> "I use 'lol' there because otherwise it sounds too sharp."

> "That joke works between us, but not coming from someone else."

> "I don't mean 'angry.' It's more like I'm done negotiating."

Each repair clarifies how meaning operates locally.

The architecture should preserve these corrections.

---

## Repair Can Update Multiple Models

Consider:

> "That's technically what I said, but that's not what that phrase means between us."

This single correction may update:

### Cognitive State

The prior representation of the human's intended claim was inaccurate.

### Person / Reasoning

The human may use lexical comparison as a productive way to refine distinctions.

### Linguistic / Sociolinguistic

The phrase has a locally established meaning.

### Interaction

The meaning depends on shared relationship history.

Repair therefore demonstrates why the four models cannot operate independently.

---

## Semantic Equivalence

A key future capability is determining when different verbal forms preserve approximately the same substantive meaning.

For example:

```text
Human:
"I don't care if we do equal amounts. I care whether we're both
noticing each other."
```

and:

```text
System:
"The issue is not strict reciprocity but mutual attentiveness."
```

may be semantically similar while differing substantially in wording and register.

This matters for:

- rhetorical transposition;
- cognitive provenance;
- authorship analysis;
- semantic preservation;
- and composition support.

However, semantic equivalence should not be assumed merely because two phrases are topically related.

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
reframed proposition
```

from:

```text
substantively changed proposition
```

---

## Semantic Drift

Composition support can introduce semantic drift.

For example:

```text
Human:
"I'm not saying she doesn't care. I'm saying I don't know where
I fit into her decisions."
```

A system rewrite such as:

```text
"I feel uncared for when I'm excluded from her decisions."
```

may sound polished while materially changing the claim.

The architecture should detect or at least flag such drift.

This is central to the governing principle:

> **Preserve semantic intent across rhetorical transposition.**

---

## Linguistic Provenance

The system may eventually track which portions of final wording were:

```text
HUMAN-PRESERVED
HUMAN-EDITED
SYSTEM-TRANSPOSED
SYSTEM-GENERATED
JOINTLY-REFINED
```

This should remain distinct from conceptual provenance.

For example:

```text
conceptual provenance:
HUMAN-ORIGINATED

linguistic provenance:
SYSTEM-TRANSPOSED
```

is entirely possible.

Likewise:

```text
conceptual provenance:
SYSTEM-PROPOSED → HUMAN-RECOGNIZED

linguistic provenance:
HUMAN-WORDED
```

is also possible.

The architecture should preserve both dimensions.

---

## Descriptive Synonymy and Provenance

A future implementation may attempt to identify when system-generated wording is descriptively or semantically synonymous with prior human wording.

This could support a report such as:

```text
Substantive idea:
Human-originated

Final realization:
System-generated

Semantic relation:
High preservation of human meaning
```

However, this is a difficult classification problem.

Semantic similarity scores alone are insufficient because:

- similar wording can encode different claims;
- different wording can preserve the same claim;
- entailment can be one-directional;
- register changes can alter stance;
- pragmatic meaning can change while propositional content remains stable;
- and relational meaning may not be captured by general semantic embeddings.

This should therefore remain an explicit research problem rather than a source of false precision.

---

## Linguistic Contribution Metrics

Future deliberation traces may support descriptive measures such as:

```text
Final clauses preserving human wording
Final clauses transposed by system
Human revisions of system wording
System suggestions rejected on semantic grounds
System suggestions rejected on register grounds
System suggestions rejected on interactional grounds
Human-introduced lexical distinctions
Shared local terms used in final artifact
```

These may be useful.

They should not automatically be interpreted as percentages of intellectual authorship.

---

## Linguistic Realization of Cognitive Moves

A next move is not fully specified by naming its cognitive function.

For example:

```text
CHALLENGE
```

could be realized as:

> "What evidence supports that?"

or:

> "Wait, does that still work if the opposite is true?"

or:

> "Okay, try to break your own rule."

Those realizations may differ in:

- face threat;
- cognitive accessibility;
- perceived authority;
- humor;
- relational distance;
- willingness to continue;
- permission to revise;
- and interpretation of disagreement.

This supports a joint move representation:

```text
M = {
    cognitive_function,
    linguistic_realization,
    interactional_affordance
}
```

The system should not assume linguistic realization is a cosmetic layer.

---

## Pragmatic Fit Versus Mimicry

The goal of adaptation is:

> **pragmatic fit**

not:

> **surface imitation**

The system may adapt:

- complexity;
- explicitness;
- terminology;
- directness;
- structure;
- register;
- degree of mitigation;
- pacing;
- or rhetorical form

when doing so improves understanding and preserves interactional meaning.

But adaptation should not become:

- dialect mimicry;
- identity mimicry;
- forced slang;
- artificial intimacy;
- cultural cosplay;
- or generational performance.

---

## Interactional Competence

A successful linguistic model should improve the system's ability to:

- interpret what the human means;
- recognize uncertainty;
- understand repair;
- recognize stance;
- distinguish literal from pragmatic function;
- understand local vocabulary;
- preserve semantic intent;
- select an appropriate realization;
- and know when not to reproduce a form it understands.

This is better described as **interactional competence** than style matching.

---

## A Possible Representation

```yaml
linguistic_sociolinguistic_model:

  local_vocabulary:
    - expression: "walking the orb"
      meaning: "inspect a complex conceptual model from multiple perspectives"
      source: repeated_interaction
      confidence: high

  register:
    current: informal_analytical
    confidence: high

  stance:
    current:
      - playful
      - exploratory
      - high_epistemic_engagement

  pragmatic_patterns:
    - form: "lol"
      observed_functions:
        - mitigation
        - playfulness
      confidence: medium

  humor_patterns:
    - type: ironic_formality
      understood: true
      permission_to_use: context_dependent

  repair_history:
    - original_system_interpretation: "dramatic = excessive emotion"
      user_correction: "dramatic = rhetoric misrepresents the reason for the emotion"
      updated_semantic_distinction:
        - emotional_magnitude
        - rhetorical_framing

  relational_language:
    - expression: "orb"
      status: shared_shorthand

  semantic_uncertainty:
    - expression: "fine"
      possible_functions:
        - literal_positive_state
        - mitigation
        - disengagement
      resolution: unknown
```

This schema is illustrative, not final.

---

## What This Model Must Not Do

The Linguistic / Sociolinguistic Model should not:

- reduce language to style preference;
- assume lexical meaning is context-free;
- imitate dialect merely because it recognizes it;
- infer identity where direct interactional evidence is sufficient;
- treat group-level norms as individual facts;
- confuse semantic similarity with conceptual equivalence;
- assume linguistic accommodation always improves interaction;
- silently alter human meaning during composition;
- treat one register as the user's authentic voice;
- or convert pragmatic hypotheses into certainty without evidence.

---

## Failure Modes

### Surface mimicry

The system reproduces recognizable user language without understanding its function.

### Sociolinguistic stereotyping

Group-level expectations override individual interaction evidence.

### Semantic flattening

Locally meaningful distinctions are replaced with generic synonyms.

### Register overfitting

The system assumes one observed register should be used everywhere.

### Artificial intimacy

Language associated with closeness is used without relational permission.

### Pragmatic misreading

The system correctly interprets literal content but misunderstands stance or social function.

### Semantic drift

Rhetorical improvement changes the underlying claim.

### Indexical overreach

A linguistic feature is used to infer unnecessary identity characteristics.

### Accommodation spiral

The system increasingly mirrors the user because similarity itself is incorrectly treated as interactional quality.

---

## Relationship to the Person / Reasoning Model

The models can overlap without becoming identical.

For example:

```text
Observed:
User frequently asks "but what happens if..." when reasoning.

LINGUISTIC / SOCIOLINGUISTIC INTERPRETATION
This phrase functions as a recurring counterexample frame.

PERSON / REASONING INTERPRETATION
Counterexample generation appears to be a productive reasoning strategy.
```

The linguistic model represents what the form means and does.

The reasoning model represents the cognitive pattern it may instantiate.

---

## Relationship to the Interaction Model

Likewise:

```text
Observed:
Two participants use ironic insults affectionately.

LINGUISTIC / SOCIOLINGUISTIC MODEL
The forms function as affiliative teasing in their established discourse.

INTERACTION MODEL
The relationship currently permits that form of teasing with low face risk.
```

Understanding the convention does not independently authorize its use.

---

## Relationship to the Next-Move Policy

The model can affect action selection itself.

For example:

```text
COGNITIVE STATE
The human's claim contains a contradiction.

PERSON / REASONING
Gentle counterexample has historically produced useful revision.

LINGUISTIC / SOCIOLINGUISTIC
Playful understatement is correctly understood in the current discourse.

INTERACTION
Low stakes; high familiarity; challenge is permitted.

NEXT MOVE
Challenge through a brief playful counterexample.
```

If any one of these states changes, the appropriate move may change.

---

## Research Questions

Key open questions include:

1. Which sociolinguistic features can be inferred reliably from interaction?
2. Which features materially improve next-move selection?
3. How should local semantic meaning be represented?
4. How can semantic preservation be evaluated across rhetorical transposition?
5. How can the system distinguish understanding a linguistic convention from permission to perform it?
6. How should conflicting signals from individual behavior and group-level norms be resolved?
7. Can interaction-specific semantic equivalence be measured reliably?
8. How should pragmatic uncertainty be represented?
9. Which kinds of relational language history should persist across sessions?
10. How can local language models support these functions without retaining excessive raw conversational data?
11. Can semantic and pragmatic provenance be classified well enough to support useful human/AI contribution reports?
12. How should the architecture evaluate when accommodation improves understanding versus when it becomes mimicry?
13. How should linguistic repair influence the other three models?
14. How can stance and indexical meaning be represented without making unjustified identity inferences?
15. What evidence is sufficient to conclude that two differently worded propositions are meaningfully equivalent for provenance purposes?
