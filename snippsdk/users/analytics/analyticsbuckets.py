class AnalyticsMetricBuckets():
    """
    Represents the bucket counts for a single analytics metric
    (posts, uploads, bytes, comments, likes or followers).
    """
    def __init__(self, json: dict) -> None:
        self.today: int = json["today"]
        """
        The count for today.
        """
        self.week: int = json["week"]
        """
        The count for the last 7 days.
        """
        self.month: int = json["month"]
        """
        The count for the last 30 days.
        """


class AnalyticsBuckets():
    """
    Represents the analytics buckets for every metric.
    """
    def __init__(self, json: dict) -> None:
        self.posts: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["posts"])
        """
        Buckets for posts.
        """
        self.uploads: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["uploads"])
        """
        Buckets for uploads.
        """
        self.bytes: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["bytes"])
        """
        Buckets for bytes uploaded.
        """
        self.comments: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["comments"])
        """
        Buckets for comments received.
        """
        self.likes: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["likes"])
        """
        Buckets for likes received.
        """
        self.followers: AnalyticsMetricBuckets = AnalyticsMetricBuckets(json["followers"])
        """
        Buckets for followers gained.
        """
