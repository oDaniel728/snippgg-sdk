class AnalyticsTotals():
    def __init__(self, json: dict) -> None:
        self.posts: int = json["posts"]
        self.views: int = json["views"]
        self.comments: int = json["comments"]
        self.likes: int = json["likes"]
        self.bytes: int = json["bytes"]
