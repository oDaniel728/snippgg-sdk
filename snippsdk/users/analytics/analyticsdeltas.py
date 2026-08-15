from typing import Optional


class AnalyticsMetricDelta():
    """
    Represents the change of a single analytics metric against the
    preceding window of equal length.
    """
    def __init__(self, json: dict) -> None:
        self.current: int = json["current"]
        """
        The value of the current window.
        """
        self.previous: int = json["previous"]
        """
        The value of the preceding window.
        """
        self.change: Optional[float] = json.get("change")
        """
        The fractional change against the preceding window, or None
        when that window was zero.
        """


class AnalyticsDeltas():
    """
    Represents the deltas for every analytics metric.
    """
    def __init__(self, json: dict) -> None:
        self.posts: AnalyticsMetricDelta = AnalyticsMetricDelta(json["posts"])
        """
        Delta for posts.
        """
        self.uploads: AnalyticsMetricDelta = AnalyticsMetricDelta(json["uploads"])
        """
        Delta for uploads.
        """
        self.views: AnalyticsMetricDelta = AnalyticsMetricDelta(json["views"])
        """
        Delta for views.
        """
        self.bytes: AnalyticsMetricDelta = AnalyticsMetricDelta(json["bytes"])
        """
        Delta for bytes uploaded.
        """
        self.comments: AnalyticsMetricDelta = AnalyticsMetricDelta(json["comments"])
        """
        Delta for comments received.
        """
        self.likes: AnalyticsMetricDelta = AnalyticsMetricDelta(json["likes"])
        """
        Delta for likes received.
        """
        self.followers: AnalyticsMetricDelta = AnalyticsMetricDelta(json["followers"])
        """
        Delta for followers gained.
        """
