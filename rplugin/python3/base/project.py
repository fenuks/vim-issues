from abc import ABC, abstractmethod
from typing import Optional

from .issues import IssuesProvider
from .reviews import ReviewsProvider


class Project(ABC):
    issues: IssuesProvider
    reviews: ReviewsProvider

    @abstractmethod
    def __init__(self, repo_url: str, token: Optional[str]):
        pass
