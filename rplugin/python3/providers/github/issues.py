from typing import List

import github
from github import Github

from base import Config, Issue, IssueFilters, IssuesProvider, MergeRequest


class GithubIssues(IssuesProvider):
    def __init__(self, config: Config):
        super().__init__(config)
        self.api = Github()

    def create_issue(self) -> Issue:
        pass

    def get_issues(self, page: int, filters: IssueFilters) -> List[Issue]:
        r = self.api.get_repo('neovim/python-client')
        return [self._get_issue_data(i) for i in r.get_issues()]

    def get_merge_requests(self) -> List[MergeRequest]:
        pass

    def get_releases(self):
        pass

    @staticmethod
    def get_project_name(
            vcs_url: str, issues_url: str, review_url: str
    ) -> str:
        pass

    @staticmethod
    def _get_issue_data(issue: github.Issue.Issue) -> Issue:
        i = Issue()
        i.identifier = str(issue.number)
        i.title = issue.title
        return i
