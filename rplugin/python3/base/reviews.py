from abc import ABC, abstractmethod
from typing import List


class MergeRequest(ABC):
    pass


class ReviewsProvider(ABC):
    @abstractmethod
    def get(self) -> List[MergeRequest]:
        pass
