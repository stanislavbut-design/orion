from dataclasses import dataclass


@dataclass(frozen=True)
class IdentityResolutionRequest:
    """
    Request submitted to the Identity Resolution Service.
    """

    module_entity: object

    identity_type: type