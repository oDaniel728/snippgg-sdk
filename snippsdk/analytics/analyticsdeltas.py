from typing import Optional


class AnalyticsMetricDelta():
    def __init__(self, json: dict) -> None:
        self.current: int = json["current"]
        self.previous: int = json["previous"]
        self.change: Optional[float] = json.get("change")


class AnalyticsDeltas():
    def __init__(self, json: dict) -> None:
        self.posts: AnalyticsMetricDelta = AnalyticsMetricDelta(json["posts"])
        self.uploads: AnalyticsMetricDelta = AnalyticsMetricDelta(json["uploads"])
        self.views: AnalyticsMetricDelta = AnalyticsMetricDelta(json["views"])
        self.bytes: AnalyticsMetricDelta = AnalyticsMetricDelta(json["bytes"])
        self.comments: AnalyticsMetricDelta = AnalyticsMetricDelta(json["comments"])
        self.likes: AnalyticsMetricDelta = AnalyticsMetricDelta(json["likes"])
        self.followers: AnalyticsMetricDelta = AnalyticsMetricDelta(json["followers"])
