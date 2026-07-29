from .exceptions import MatchingStrategyNotFoundError
from .strategy import IdentityMatchingStrategy

class StrategyRegistry:

    _strategies = {}    

    @classmethod
    def register(
        cls,
        identity_type,
        strategy,
    ):

        if identity_type in cls._strategies:
            raise ValueError(
                f"Strategy already registered for "
                f"{identity_type.__name__}."
            )

        if not isinstance(
            strategy,
            IdentityMatchingStrategy,
        ):
            raise TypeError(
                "Strategy must inherit from "
                "IdentityMatchingStrategy."
            )

        cls._strategies[identity_type] = strategy


    @classmethod
    def get(cls, identity_type):

        strategy = cls._strategies.get(identity_type)

        if strategy is None:
            raise MatchingStrategyNotFoundError(
                f"No matching strategy registered for "
                f"{identity_type.__name__}."
            )

        return strategy