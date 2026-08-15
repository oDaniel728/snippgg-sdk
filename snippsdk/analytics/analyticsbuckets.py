class AnalyticsMetricBuckets():
    def __init__(self, json: dict) -> None:
        self.today: int = json["today"]
        self.week: int = json["week"]
        self.month: int = json["month"]


class AnalyticsBuckets():
    def __init__(self, json: dict) -> None:
        self.posts: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["posts"])
        self.uploads: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["uploads"])
        self.bytes: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["bytes"])
        self.comments: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["comments"])
        self.likes: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["likes"])
        self.followers: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["followers"])
