from snippsdk.users.analytics.analyticsbuckets import AnalyticsBuckets
from snippsdk.users.analytics.analyticsdeltas import AnalyticsDeltas
from snippsdk.users.analytics.analyticsseries import AnalyticsSeries
from snippsdk.users.analytics.analyticstotals import AnalyticsTotals


class UserAnalytics():
    """
    Represents the analytics of the API key's owner: posts, uploads,
    bytes, comments, likes and followers over time, plus lifetime totals.
    """
    def __init__(self, json: dict) -> None:
        analytics = json["analytics"]
        self.range: int = analytics["range"]
        """
        The window used for series and deltas (7, 30, 90 or 365).
        """
        self.buckets: AnalyticsBuckets = AnalyticsBuckets(analytics["buckets"])
        """
        Bucket counts for today, last 7 days and last 30 days.
        """
        self.totals: AnalyticsTotals = AnalyticsTotals(analytics["totals"])
        """
        Lifetime totals.
        """
        self.series: AnalyticsSeries = AnalyticsSeries(analytics["series"])
        """
        Daily series across the window, oldest first.
        """
        self.deltas: AnalyticsDeltas = AnalyticsDeltas(analytics["deltas"])
        """
        Changes against the preceding window of equal length.
        """