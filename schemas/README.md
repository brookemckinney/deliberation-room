# Schemas

> **Status:** These files are provisional state specifications, not yet machine-validating schemas.
>
> They describe the information Deliberation Room may need to represent and the distinctions the architecture intends to preserve. Field names, structures, enumerations, persistence rules, and relationships remain implementation proposals subject to prototyping and empirical revision.
>
> The use of `schemas/` reflects the intended direction of the project: these representations may eventually be formalized as enforceable schemas for implementation. The current YAML files should not be interpreted as JSON Schema, API contracts, database definitions, or validated production interfaces.

## Reading the schemas

Treat the current files as answers to:

> **What state might the architecture need to represent explicitly?**

not yet:

> **What exact data structure must an implementation use?**

An implementation may combine, remove, rename, or restructure fields if evaluation shows that a simpler or different representation better preserves the architectural commitments.

In particular, the four-model architecture is itself testable. The existence of a field in these files does not establish that the field is:

- necessary;
- reliably inferable;
- safe to persist;
- empirically useful;
- or worth its privacy and complexity cost.

The current files are therefore best understood as **research specifications for candidate state representation**.

## Current files

- [`interaction-state.yaml`](interaction-state.yaml) — a provisional representation of the current interaction state across the four models, policy state, composition state, provenance, uncertainty, persistence, and user correction.
- [`deliberation-trace.yaml`](deliberation-trace.yaml) — a provisional representation of meaningful cognitive and interactional events across time, including revision, question-resolution provenance, conceptual and linguistic provenance, metacognitive summaries, and artifact linkage.

## What should become machine-valid later

A future implementation may formalize these representations using one or more of:

- JSON Schema;
- typed Python models;
- Pydantic;
- TypeScript interfaces;
- database schemas;
- protocol definitions;
- or another enforceable representation.

That step should happen **after** early prototyping reveals which state variables are actually necessary.

The project should not harden speculative complexity into an implementation contract merely because it has already been written down.
