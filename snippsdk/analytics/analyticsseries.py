class AnalyticsSeriesPoint():
    def __init__(self, json: dict) -> None:
        self.day: str = json["day"]
        self.value: int = json["value"]


class AnalyticsSeries():
    def __init__(self, json: dict) -> None:
        self.posts: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("posts", [])]
        self.uploads: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("uploads", [])]
        self.views: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("views", [])]
        self.bytes: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("bytes", [])]
        self.comments: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("comments", [])]
        self.likes: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("likes", [])]
        self.followers: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("followers", [])]
