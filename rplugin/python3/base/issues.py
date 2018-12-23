from typing import List
from abc import ABC, abstractmethod, abstractstaticmethod
from .config import Config

class Issue:
    identifier: str
    title: str
    author: str


class IssueFilters(ABC):
    pass


class IssuesProvider(ABC):
    def __init__(self, config: Config):
        self.config = config

    @abstractmethod
    def create_issue(self) -> Issue:
        pass

    @staticmethod
    def format_issues(issues: List[Issue]) -> List[str]:
        return [
            "* #{identifier} - {title}".format(
                identifier=issue.identifier, title=issue.title
            ) for issue in issues
        ]

    @abstractmethod
    def get_issues(self, page: int, filters: IssueFilters) -> List[Issue]:
        pass

    @abstractmethod
    def get_releases(self):
        pass

    @abstractstaticmethod
    def get_project_name(
            vcs_url: str, issues_url: str, review_url: str
    ) -> str:
        pass
