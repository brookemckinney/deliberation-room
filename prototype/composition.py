"""Composition engine for the Deliberation Room prototype.

This module provides the first executable handoff from deliberation
to rhetorical composition.

It is intentionally simple.

The mature Deliberation Room architecture will eventually use:
- rhetorical situation modeling
- interaction state
- linguistic / sociolinguistic evidence
- genre conventions
- external evidence
- semantic and interactional drift checking

This prototype establishes the contract before those richer systems
are implemented.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from state import DeliberationState


class ArtifactType(str, Enum):
    """Supported artifact types."""

    MESSAGE = "message"
    EMAIL = "email"
    ESSAY = "essay"
    DISCUSSION_POST = "discussion_post"
    MEMO = "memo"
    FEEDBACK = "feedback"
    SPEECH = "speech"
    EXPLANATION = "explanation"
    OTHER = "other"


class Register(str, Enum):
    """Broad register targets used by the current scaffold."""

    CASUAL = "casual"
    CONVERSATIONAL = "conversational"
    PROFESSIONAL = "professional"
    ACADEMIC = "academic"
    FORMAL = "formal"


@dataclass
class AudienceModel:
    """Minimal audience representation for composition."""

    description: str

    role: Optional[str] = None

    relationship: Optional[str] = None

    familiarity: Optional[str] = None

    power_relation: Optional[str] = None

    discourse_community: Optional[str] = None

    relevant_prior_context: List[str] = field(
        default_factory=list
    )


@dataclass
class LinguisticProfile:
    """Minimal linguistic realization profile.

    This is only a scaffold.

    The target architecture uses empirical speech/text evidence,
    sociolinguistic interpretation, idiolect, pragmatics,
    discourse-community conventions, role language, humor,
    and interactional permissions.
    """

    register: Register = Register.CONVERSATIONAL

    directness: Optional[str] = None

    warmth: Optional[str] = None

    humor_permission: Optional[str] = None

    stance: Optional[str] = None

    cadence_notes: List[str] = field(
        default_factory=list
    )

    preferred_vocabulary: List[str] = field(
        default_factory=list
    )

    avoid_vocabulary: List[str] = field(
        default_factory=list
    )

    shared_language: List[str] = field(
        default_factory=list
    )

    discourse_conventions: List[str] = field(
        default_factory=list
    )


@dataclass
class CompositionContract:
    """Explicit handoff from deliberation to composition."""

    artifact_type: ArtifactType

    purpose: str

    audience: AudienceModel

    linguistic_profile: LinguisticProfile

    semantic_invariants: List[str] = field(
        default_factory=list
    )

    material_uncertainties: List[str] = field(
        default_factory=list
    )

    relevant_facts: List[str] = field(
        default_factory=list
    )

    external_support: List[str] = field(
        default_factory=list
    )

    permitted_transformations: List[str] = field(
        default_factory=lambda: [
            "organization",
            "syntax",
            "concision",
            "register",
            "rhetorical sequencing",
        ]
    )

    prohibited_additions: List[str] = field(
        default_factory=lambda: [
            "unsupported factual claims",
            "unconfirmed motives",
            "stronger certainty",
            "new commitments",
            "new emotional states",
        ]
    )


@dataclass
class CompositionResult:
    """Composed artifact plus inspectable metadata."""

    text: str

    contract: CompositionContract

    conceptual_source: str

    linguistic_source: str

    external_support_used: List[str] = field(
        default_factory=list
    )

    drift_flags: List[str] = field(
        default_factory=list
    )


class CompositionPlanner:
    """Create a composition contract from deliberation state."""

    def build_contract(
        self,
        state: DeliberationState,
        artifact_type: ArtifactType,
        purpose: str,
        audience: AudienceModel,
        linguistic_profile: LinguisticProfile,
        relevant_facts: Optional[List[str]] = None,
        external_support: Optional[List[str]] = None,
    ) -> CompositionContract:
        """Build the explicit deliberation-to-composition handoff."""

        invariants = [
            claim.content
            for claim in state.cognitive.current_claims
        ]

        uncertainties = [
            item.content
            for item in state.cognitive.uncertainty
        ]

        return CompositionContract(
            artifact_type=artifact_type,
            purpose=purpose,
            audience=audience,
            linguistic_profile=linguistic_profile,
            semantic_invariants=invariants,
            material_uncertainties=uncertainties,
            relevant_facts=relevant_facts or [],
            external_support=external_support or [],
        )


class RhetoricalTransposer:
    """Primitive rhetorical realization scaffold.

    This is not the final Deliberation Room rhetorical compiler.

    It proves that composition receives an explicit contract rather
    than simply handing raw conversation history back to a language
    model.
    """

    def compose(
        self,
        contract: CompositionContract,
    ) -> CompositionResult:
        """Produce a simple artifact from the composition contract."""

        if not contract.semantic_invariants:
            return CompositionResult(
                text=(
                    "I do not yet have enough human-established "
                    "meaning to compose from."
                ),
                contract=contract,
                conceptual_source="insufficient_human_state",
                linguistic_source="template",
                drift_flags=[
                    "No semantic invariants were available."
                ],
            )

        meaning = self._join_invariants(
            contract.semantic_invariants
        )

        text = self._realize(
            meaning=meaning,
            contract=contract,
        )

        return CompositionResult(
            text=text,
            contract=contract,
            conceptual_source="deliberation_state",
            linguistic_source="template_transposition",
            external_support_used=contract.external_support,
        )

    @staticmethod
    def _join_invariants(
        invariants: List[str],
    ) -> str:
        """Combine current claims without inventing a new claim."""

        if len(invariants) == 1:
            return invariants[0]

        return "; ".join(invariants)

    def _realize(
        self,
        meaning: str,
        contract: CompositionContract,
    ) -> str:
        """Realize meaning according to the current artifact scaffold."""

        artifact = contract.artifact_type

        if artifact == ArtifactType.MESSAGE:
            return self._message(
                meaning=meaning,
                contract=contract,
            )

        if artifact == ArtifactType.EMAIL:
            return self._email(
                meaning=meaning,
                contract=contract,
            )

        if artifact in {
            ArtifactType.ESSAY,
            ArtifactType.DISCUSSION_POST,
            ArtifactType.MEMO,
            ArtifactType.EXPLANATION,
        }:
            return self._analytic_artifact(
                meaning=meaning,
                contract=contract,
            )

        return meaning

    @staticmethod
    def _message(
        meaning: str,
        contract: CompositionContract,
    ) -> str:
        """Produce a minimal message realization."""

        profile = contract.linguistic_profile

        if profile.register == Register.CASUAL:
            prefix = "I think what I'm actually trying to say is: "

        elif profile.register == Register.PROFESSIONAL:
            prefix = "I want to clarify the point I'm making: "

        else:
            prefix = "I think the center of what I mean is: "

        text = prefix + meaning

        if contract.material_uncertainties:
            text += (
                " What I don't want to overstate is "
                + "; ".join(contract.material_uncertainties)
                + "."
            )

        return text

    @staticmethod
    def _email(
        meaning: str,
        contract: CompositionContract,
    ) -> str:
        """Produce a minimal email realization."""

        body = (
            f"I'm writing because {contract.purpose}. "
            f"The main point I want to communicate is: {meaning}"
        )

        if contract.material_uncertainties:
            body += (
                " I also want to preserve some uncertainty around "
                + "; ".join(contract.material_uncertainties)
                + "."
            )

        return body

    @staticmethod
    def _analytic_artifact(
        meaning: str,
        contract: CompositionContract,
    ) -> str:
        """Produce a minimal analytic artifact."""

        text = meaning

        if contract.relevant_facts:
            text += (
                "\n\nRelevant support:\n- "
                + "\n- ".join(contract.relevant_facts)
            )

        if contract.external_support:
            text += (
                "\n\nExternal support available:\n- "
                + "\n- ".join(contract.external_support)
            )

        return text
