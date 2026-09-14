# Metacognitive Controller

The Metacognitive Controller is the adaptive control mechanism inside Engine 1 of Deliberation Room.

Its purpose is not to identify a fixed "type" of thinker.

Its purpose is to estimate:

> **What cognitive operation is this human performing now, what kinds of intervention are producing useful cognitive movement, and what should remain for the human to do next?**

The controller uses interaction history as evidence about the reasoning process and converts that evidence into instructions for subsequent system behavior.

In this sense, Deliberation Room does not merely prompt the human.

It also uses the human's responses to **dynamically prompt itself**.

---

## 1. Core Loop

The controller operates as a repeated evidence-and-intervention loop:

```text
HUMAN CONTRIBUTION
        │
        ▼
REPRESENT CURRENT COGNITIVE STATE
        │
        ▼
INFER CANDIDATE COGNITIVE OPERATIONS
        │
        ▼
COMPARE WITH INTERACTION HISTORY
        │
        ▼
ESTIMATE PRODUCTIVE NEXT OPERATION
        │
        ▼
GENERATE INTERNAL CONTROL INSTRUCTION
        │
        ▼
SELECT MINIMAL SYSTEM MOVE
        │
        ▼
HUMAN RESPONDS
        │
        ▼
MEASURE / INFER COGNITIVE STATE CHANGE
        │
        ▼
UPDATE METACOGNITIVE EVIDENCE
        │
        └──────────────────────────↺
```

The controller therefore distinguishes between:

```text
CONTENT STATE
What does the human currently appear to think?

PROCESS STATE
How is the human currently reasoning?

INTERVENTION HISTORY
What has the system tried?

RESPONSE EFFECT
What changed after each intervention?
```

These are related but should not be collapsed.

---

## 2. Cognitive Operation Vocabulary

A first implementation may represent cognitive operations using an extensible vocabulary.

Candidate general operations include:

```text
NOTICE
RETRIEVE
CLARIFY
COMPARE
CONTRAST
CLASSIFY
ANALOGIZE
INSTANTIATE
ABSTRACT
GENERATE_EXAMPLE
GENERATE_COUNTEREXAMPLE
TEST_COUNTERFACTUAL
IDENTIFY_ASSUMPTION
CONSTRUCT_WARRANT
EVALUATE_EVIDENCE
ISOLATE_VARIABLE
TRACE_CAUSAL_CHAIN
SHIFT_PERSPECTIVE
IDENTIFY_INVARIANT
SYNTHESIZE
REVISE
REJECT
STABILIZE_JUDGMENT
```

These labels describe **cognitive work**, not conversational surface forms.

For example:

```text
cognitive operation:
IDENTIFY_INVARIANT

possible system move:
COUNTERFACTUAL

possible utterance:
"Would that still bother you if everything else stayed the same
except X?"
```

The system move is not the cognitive operation.

The system move creates conditions under which the human may perform the cognitive operation.

---

## 3. Disciplinary Operations

General metacognitive operations can be supplemented by domain-specific epistemic operations.

For literary analysis:

```text
INTERPRET_TEXTUAL_EVIDENCE
TEST_COUNTERREADING
ANALYZE_FORM
LOCALIZE_AMBIGUITY
CONNECT_FORM_AND_MEANING
```

For history:

```text
EVALUATE_SOURCE
ESTABLISH_CHRONOLOGY
TEST_CAUSATION
COMPARE_EXPLANATIONS
REASON_ABOUT_CONTINGENCY
```

For science:

```text
FORM_HYPOTHESIS
PROPOSE_MECHANISM
IDENTIFY_CONFOUND
TEST_FALSIFIABILITY
EVALUATE_MEASUREMENT
```

For design:

```text
MODEL_STAKEHOLDER
IDENTIFY_CONSTRAINT
EVALUATE_TRADEOFF
ITERATE_SOLUTION
TRACE_CONSEQUENCE
```

For ethics:

```text
IDENTIFY_STAKEHOLDER
IDENTIFY_VALUE
COMPARE_DUTIES
TRACE_CONSEQUENCES
TEST_PRINCIPLE
LOCALIZE_UNCERTAINTY
```

For rhetoric:

```text
MODEL_AUDIENCE
IDENTIFY_EXIGENCE
TEST_WARRANT
EVALUATE_ETHOS
EVALUATE_PATHOS
EVALUATE_LOGOS
EVALUATE_KAIROS
IDENTIFY_CONSTRAINT
SELECT_AVAILABLE_MEANS
```

The architecture therefore does not merely adapt the system's factual knowledge by discipline.

It adapts **what counts as responsible cognitive movement**.

---

## 4. Intervention Record

Each system intervention should be represented as an inspectable event.

A conceptual record might include:

```yaml
intervention_id: 17

prior_state:
  current_claim:
    "Creon's problem is that his law is unjust."

target_operation:
  IDENTIFY_INVARIANT

system_move:
  COUNTERFACTUAL

realization:
  "Would your argument still work if Creon's law were just?"

constraints:
  - change one variable
  - do not name authority
  - do not supply the distinction
  - preserve current abstraction level

predicted_value:
  cognitive_progress: moderate
  information_gain: high
  substitution_risk: low

human_response:
  "Wait, yes. I'd still have a problem with how he treats disagreement."

observed_or_inferred_change:
  - original explanation weakened
  - stable feature across cases detected
  - new distinction emerging

human_confirmation:
  pending
```

This allows the system to reason not merely from dialogue history, but from a structured history of:

```text
STATE
→ INTERVENTION
→ RESPONSE
→ CHANGE
```

---

## 5. Productive Cognitive Movement

The controller requires an operational account of what counts as useful change.

Candidate indicators include:

```text
new distinction
new question
assumption exposed
warrant articulated
counterexample generated
claim revised
claim rejected
uncertainty localized
evidence re-evaluated
causal variable isolated
alternative explanation considered
perspective incorporated
abstraction produced
concrete instance produced
contradiction resolved
contradiction intentionally preserved
judgment stabilized
```

The controller should not treat these as equivalent.

Different tasks may assign different values to different changes.

For example:

```text
brainstorming task:
new questions may be highly valuable

argument evaluation:
localized uncertainty may be highly valuable

final decision:
stabilized judgment may be highly valuable

scientific reasoning:
identification of a confound may be highly valuable
```

Productivity is therefore task-relative and epistemically conditioned.

---

## 6. Rejection Is Data

System agreement is not the optimization target.

Suppose the system proposes:

```text
"Maybe the issue is that changing one's mind looks weak."
```

and the human responds:

```text
"No. I don't care whether it looks weak.
I'm talking about whether someone can still be legitimate
if they refuse to revise when they're wrong."
```

The system proposal was rejected.

But the interaction may have produced substantial cognitive value:

```text
rejected framing:
weakness

new distinction:
appearance of strength ≠ legitimacy

new concept:
revision under error

conceptual stability:
increased
```

The controller should therefore distinguish:

```text
SYSTEM WAS ACCEPTED
```

from:

```text
INTERACTION WAS PRODUCTIVE
```

These are not the same variable.

Correction and rejection may be among the highest-information events available to the system.

---

## 7. Dynamic Metacognitive Evidence

The controller can maintain task-local evidence about intervention effectiveness.

For example:

```yaml
current_task_process_evidence:

  counterfactual_testing:
    attempts: 3
    productive_state_changes: 3
    current_support: high

  open_ended_explanation:
    attempts: 2
    productive_state_changes: 0
    current_support: low

  contrastive_comparison:
    attempts: 2
    productive_state_changes: 1
    current_support: moderate

  direct_system_proposal:
    attempts: 2
    accepted_unchanged: 0
    human_revisions: 1
    human_rejections: 1
```

This does not justify:

```text
USER TYPE:
counterfactual thinker
```

It justifies something closer to:

```text
CURRENT EVIDENCE:

Counterfactual testing has recently produced useful state change
in this task.
```

That difference is constitutional.

---

## 8. From Evidence to Self-Prompt

Metacognitive state should be usable as control data.

A controller might convert its current evidence into an internal instruction such as:

```text
CURRENT COGNITIVE NEED

Test whether the user's stated variable actually explains
their judgment.

CURRENT PROCESS EVIDENCE

Single-variable counterfactuals have produced useful revision.

RISK

Naming the likely alternative explanation would substitute
for a distinction the human appears capable of making.

NEXT INTERVENTION

Use one counterfactual.
Change only the disputed variable.
Do not provide the alternative explanation.
Ask what remains true.
```

A realization model can then convert that instruction into appropriate language.

For one user:

```text
"Would that still be true if X changed?"
```

For another interaction:

```text
"Okay, but hold everything else constant for a second—if X flips,
does your judgment change?"
```

For an academic context:

```text
"Would the interpretation remain defensible if X were not the case?"
```

The cognitive operation may be the same.

The linguistic realization differs because the Linguistic / Sociolinguistic and Interaction Models differ.

---

## 9. Exploration Versus Exploitation

A personalized controller should not repeatedly use one intervention simply because it previously worked.

Otherwise:

```text
early success
→ repeated intervention
→ more evidence for that intervention
→ apparent stable user preference
```

can become a self-fulfilling loop.

The controller should therefore balance:

### Exploitation

Prefer operations supported by current evidence when the cost of failure is meaningful.

### Exploration

Occasionally test plausible alternative operations when doing so is low-risk and potentially informative.

### Correction

Rapidly reduce confidence when the human indicates that the model is wrong.

Current-task evidence should generally dominate older reasoning history.

---

## 10. Metacognitive Feedback

The same event structure used for control can support optional feedback to the human.

A useful summary should describe the process rather than assign a cognitive identity.

For example:

```text
During this task:

- 4 of 6 substantive conceptual changes followed contrastive
  or counterfactual prompts.

- Open-ended explanation produced elaboration but no detected
  claim revision.

- You rejected 3 system-proposed framings.

- Two of those rejections produced new distinctions.

- Your final claim emerged after you identified what remained
  constant across two counterfactual cases.
```

This is preferable to:

```text
"You are a contrastive thinker."
```

The first describes evidence.

The second converts contextual evidence into an identity claim.

---

## 11. Contribution and Provenance Metrics

Deliberation Room should avoid a simplistic:

```text
73% HUMAN
27% AI
```

if those numbers are based only on final token overlap.

Authorship and cognitive contribution are multidimensional.

At minimum, the architecture should distinguish:

```text
CONCEPTUAL CONTRIBUTION
Who introduced or developed the substantive idea?

METACOGNITIVE CONTRIBUTION
Who performed the reasoning operation that changed the model?

INTERVENTION CONTRIBUTION
Which system moves helped produce useful change?

ORGANIZATIONAL CONTRIBUTION
Who determined structure or sequence?

EVIDENTIARY CONTRIBUTION
Who supplied evidence, facts, sources, or examples?

LINGUISTIC CONTRIBUTION
Who supplied the final wording?
```

A system may therefore produce nearly every final token while the underlying judgment remains predominantly human-developed.

Conversely, a student may manually type every final token while reproducing a system-supplied argument.

Token production alone does not establish intellectual authorship.

---

## 12. System-Proposal Accounting

System proposals should be explicitly traceable.

For each substantive proposal, the system can record whether the human:

```text
ACCEPTED
REVISED
REJECTED
IGNORED
RETURNED_TO_LATER
```

For example:

```yaml
system_proposals:
  total: 8
  accepted_unchanged: 1
  revised: 4
  rejected: 2
  ignored: 1
```

This may be more informative than a generic AI-use percentage.

A final artifact could therefore report:

```text
Substantive system proposals: 8
Accepted unchanged: 1
Human-revised: 4
Rejected: 2
Unused: 1
```

without implying that every proposal had equal intellectual importance.

---

## 13. Semantic Contribution

The architecture may also compare final artifact propositions against the provenance trace.

A proposition in the final artifact may be classified conceptually as:

```text
HUMAN_ORIGINATED

SYSTEM_PROPOSED_HUMAN_RECOGNIZED

SYSTEM_PROPOSED_HUMAN_REVISED

JOINTLY_DEVELOPED

EXTERNAL_EVIDENCE

SYSTEM_LINGUISTIC_REALIZATION
```

This permits a more meaningful distinction between:

```text
the idea came from the human
```

and:

```text
the system supplied synonymous or rhetorically improved wording
```

For example:

```text
Human:
"I think it's not really the law. It's that he thinks being king
means he can't be wrong."

Final artifact:
"Creon's failure lies less in the content of the law than in his
conflation of political authority with infallibility."
```

Lexically, the sentences differ substantially.

Semantically, the final proposition may still be traceable to the human's prior judgment.

The architecture should therefore avoid treating lexical novelty as conceptual novelty.

---

## 14. Semantic Similarity Is Evidence, Not Proof

A future implementation may use:

```text
semantic similarity
proposition extraction
entailment
human confirmation
trace alignment
```

to estimate relationships between human language, system proposals, and final artifact language.

But automated semantic matching should not silently determine authorship.

For example:

```text
Human:
"He thinks being king means his judgment is the state's judgment."

System:
"Creon conflates personal judgment with state authority."
```

A model may judge these semantically similar.

That can support provenance analysis.

It should not independently establish:

```text
THE HUMAN DEFINITELY ORIGINATED THIS CONCEPT
```

when the trace is ambiguous.

Human confirmation and interaction history remain relevant.

---

## 15. Research and External Evidence

Providing information is not necessarily cognitive substitution.

The system may retrieve or supply:

```text
facts
definitions
sources
historical context
disciplinary conventions
counterexamples
data
terminology
```

when these are inputs the human needs in order to reason.

The distinction is:

```text
SUPPLY INFORMATION
≠
SUPPLY THE JUDGMENT
```

For example, the system may tell a learner:

```text
"Creon becomes king after the deaths of Eteocles and Polynices."
```

without telling the learner:

```text
"Therefore Sophocles is arguing that political authority creates
epistemic arrogance."
```

The first supplies potentially relevant information.

The second performs interpretive judgment.

Whether a particular intervention substitutes for cognition depends on:

```text
task
learning objective
discipline
current cognitive state
requested support
```

rather than on a universal prohibition against AI-provided content.

---

## 16. Privacy and Data Minimization

Metacognitive adaptation creates a potential privacy risk.

A system capable of accumulating a detailed model of how a person thinks could become substantially more intrusive than necessary.

Therefore the controller should prefer:

```text
task-local state
abstracted process features
minimal retention
explicit scope
correctability
confidence
```

over unrestricted storage of raw interaction history.

For example, a future system may retain:

```text
counterfactual testing was productive in recent argument tasks
```

rather than retaining every sensitive conversation from which that observation was derived.

This supports the broader research hypothesis that useful personalization may be possible using abstracted interaction state rather than large stores of raw personal data.

That remains an empirical hypothesis.

---

## 17. Failure Modes

### Fixed cognitive typing

The system turns contextual evidence into a stable identity.

Example:

```text
"You are an analogical thinker."
```

Mitigation:

```text
scope observations by task
retain uncertainty
prefer current evidence
permit correction
```

### Intervention lock-in

The controller repeats whichever operation worked first.

Mitigation:

```text
controlled exploration
decay stale evidence
detect diminishing returns
```

### Agreement optimization

The system treats acceptance of its proposals as success.

Mitigation:

```text
score representational change
treat rejection as information
separate agreement from productivity
```

### Hidden cognitive substitution

The system asks a question whose wording already contains the conclusion.

Example:

```text
"Could Creon's real problem be his inability to separate authority
from infallibility?"
```

when making that distinction is precisely the cognitive work the human should perform.

Mitigation:

```text
represent target cognitive operation explicitly
estimate substitution risk
prefer minimally leading realization
```

### Metacognitive overreach

The system infers internal cognitive traits from insufficient evidence.

Mitigation:

```text
distinguish observation from inference
track confidence
require confirmation where appropriate
avoid diagnostic language
```

### Surveillance by provenance

A system intended to preserve authorship becomes a high-resolution behavioral monitoring system.

Mitigation:

```text
collect reasoning events rather than irrelevant behavior
avoid keystroke surveillance
minimize raw data
permit local processing
retain only what the task requires
```

---

## 18. Evaluation Questions

The Metacognitive Controller creates several testable research questions.

### H1 — Adaptive elicitation

Does a metacognitively adaptive next-move policy produce more substantive human reasoning change than generic Socratic questioning?

### H2 — Cognitive responsibility

Does explicitly selecting the cognitive operation that remains with the human preserve more human conceptual responsibility than unrestricted generative assistance?

### H3 — Intervention efficiency

Can the controller produce equivalent or better reasoning outcomes using fewer system interventions?

### H4 — Correction

Does treating rejection and revision as controller evidence improve subsequent intervention selection?

### H5 — Generalization

Which metacognitive process signals transfer across tasks, and which remain domain-specific?

### H6 — Personalization

Does task-local adaptation outperform static user profiles?

### H7 — Provenance validity

Can structured interaction traces meaningfully predict whether a human can explain and defend the judgment embodied in a final artifact?

### H8 — Data minimization

Can abstracted metacognitive state provide useful personalization without retaining large quantities of raw personal interaction data?

---

## 19. Educational Interpretation

In an educational implementation, the controller should not optimize for:

```text
correct answer as quickly as possible
```

It should optimize for the learner performing the relevant disciplinary cognition.

For example:

```text
student:
"Antigone is about whether people should follow laws."

system:
"Would your argument change if Creon's law were morally good?"

student:
"Maybe not."

system:
"What would still bother you?"

student:
"He acts like disagreeing with him means disagreeing with the state."

system:
"So what distinction are you making now?"

student:
"Authority isn't the same as being right."
```

The important artifact is not merely the final sentence.

It is the path:

```text
initial interpretation
→ counterfactual
→ destabilization
→ invariant detection
→ distinction
→ revised judgment
```

Composition may happen afterward.

The learner should be able to answer:

> **Why is this claim here?**

because the learner participated in the reasoning that produced it.

---

## 20. Architectural Principle

The Metacognitive Controller exists to operationalize two governing principles:

> **The system may challenge. The human must judge.**

and:

> **Optimize for what the human should be able to do next, not merely for what the model should say next.**

The controller is successful not when the system appears maximally intelligent.

It is successful when the interaction makes useful human cognition more likely **without quietly performing the relevant judgment on the human's behalf**.
