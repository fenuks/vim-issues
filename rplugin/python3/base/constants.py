from enum import Enum, unique


@unique
class IssuesSoftware(Enum):
    bitbucket = 0
    bugzilla = 1
    github = 2
    gitlab = 3
    jira = 4
    phabricator = 5


@unique
class ReviewSoftware(Enum):
    bitbucket = 0
    fisheye = 1
    github = 2
    gitlab = 3
    phabricator = 4


@unique
class VcsSoftware(Enum):
    hg = 0
    git = 1
