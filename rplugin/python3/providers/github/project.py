from typing import Optional

from github import Github

from base import IssuesProvider, Project, ReviewsProvider


class GithubProject(Project):
    def __init__(self, repo_url: str, token: Optional[str]):
        self.repo_url = repo_url
        self.token = token

        if token is not None:
            self._api = Github()
