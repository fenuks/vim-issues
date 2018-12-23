from typing import List

from base import MergeRequest, ReviewsProvider


class GithubReviews(ReviewsProvider):
    def __init__(self, config)
    def get(self) -> List[MergeRequest]:
        pass
