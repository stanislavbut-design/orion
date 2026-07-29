from .registry import StrategyRegistry
from .request import IdentityResolutionRequest

class IdentityResolutionService:

    @classmethod
    def resolve(
        cls,
        request: IdentityResolutionRequest,
    ):

        strategy = StrategyRegistry.get(
            request.identity_type
        )

        return strategy.resolve(request)