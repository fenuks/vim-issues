from typing import List

from base import MergeRequest, ReviewsProvider


class GithubReviews(ReviewsProvider):
    def get(self) -> List[MergeRequest]:
        pass
