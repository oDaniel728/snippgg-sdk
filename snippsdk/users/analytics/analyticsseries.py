class AnalyticsSeriesPoint():
    """
    Represents a single day's value within an analytics series.
    """
    def __init__(self, json: dict) -> None:
        self.day: str = json["day"]
        """
        The UTC date of the point (YYYY-MM-DD).
        """
        self.value: int = json["value"]
        """
        The value for that day.
        """


class AnalyticsSeries():
    """
    Represents the daily series for every analytics metric.
    """
    def __init__(self, json: dict) -> None:
        self.posts: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("posts", [])]
        """
        Daily series for posts.
        """
        self.uploads: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("uploads", [])]
        """
        Daily series for uploads.
        """
        self.views: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("views", [])]
        """
        Daily series for views.
        """
        self.bytes: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("bytes", [])]
        """
        Daily series for bytes uploaded.
        """
        self.comments: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("comments", [])]
        """
        Daily series for comments received.
        """
        self.likes: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("likes", [])]
        """
        Daily series for likes received.
        """
        self.followers: list[AnalyticsSeriesPoint] = [AnalyticsSeriesPoint(point) for point in json.get("followers", [])]
        """
        Daily series for followers gained.
        """
