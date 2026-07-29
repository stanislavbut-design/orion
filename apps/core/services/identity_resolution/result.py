from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class IdentityResolutionResult:

    identity = None

    created: bool = False

    requires_confirmation: bool = False