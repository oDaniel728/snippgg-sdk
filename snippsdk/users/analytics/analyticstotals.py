class AnalyticsTotals():
    """
    Represents the lifetime totals for the account's analytics.
    """
    def __init__(self, json: dict) -> None:
        self.posts: int = json["posts"]
        """
        The total number of posts.
        """
        self.views: int = json["views"]
        """
        The total number of views across all posts.
        """
        self.comments: int = json["comments"]
        """
        The total number of comments received.
        """
        self.likes: int = json["likes"]
        """
        The total number of likes received.
        """
        self.bytes: int = json["bytes"]
        """
        The total number of bytes uploaded.
        """
