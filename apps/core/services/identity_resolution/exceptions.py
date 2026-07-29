class IdentityResolutionError(Exception):
    pass


class MatchingStrategyNotFoundError(
    IdentityResolutionError
):
    pass

class InvalidMatchingStrategyError(
    IdentityResolutionError
):
    pass


class DuplicateMatchingStrategyError(
    IdentityResolutionError
):
    pass