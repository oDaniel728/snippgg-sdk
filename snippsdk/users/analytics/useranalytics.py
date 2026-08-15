from snippsdk.users.analytics.analyticsbuckets import AnalyticsBuckets
from snippsdk.users.analytics.analyticsdeltas import AnalyticsDeltas
from snippsdk.users.analytics.analyticsseries import AnalyticsSeries
from snippsdk.users.analytics.analyticstotals import AnalyticsTotals


class UserAnalytics():
    def __init__(self, json: dict) -> None:
        analytics = json["analytics"]
        self.range: int = analytics["range"]
        self.buckets: AnalyticsBuckets = AnalyticsBuckets(analytics["buckets"])
        self.totals: AnalyticsTotals = AnalyticsTotals(analytics["totals"])
        self.series: AnalyticsSeries = AnalyticsSeries(analytics["series"])
        self.deltas: AnalyticsDeltas = AnalyticsDeltas(analytics["deltas"])