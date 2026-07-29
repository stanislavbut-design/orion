from abc import ABC
from abc import abstractmethod
from .request import IdentityResolutionRequest


class IdentityMatchingStrategy(ABC):

    @abstractmethod
    def resolve(
        request: IdentityResolutionRequest,
    ):
        """
        Resolve a Module Entity
        to a Core Identity.
        """
        raise NotImplementedError