from snippsdk.analytics.analyticsbuckets import AnalyticsBuckets
from snippsdk.analytics.analyticsdeltas import AnalyticsDeltas
from snippsdk.analytics.analyticsseries import AnalyticsSeries
from snippsdk.analytics.analyticstotals import AnalyticsTotals


class UserAnalytics():
    def __init__(self, json: dict) -> None:
        analytics = json["analytics"]
        self.range: int = analytics["range"]
        self.buckets: AnalyticsBuckets = AnalyticsBuckets(analytics["buckets"])
        self.totals: AnalyticsTotals = AnalyticsTotals(analytics["totals"])
        self.series: AnalyticsSeries = AnalyticsSeries(analytics["series"])
        self.deltas: AnalyticsDeltas = AnalyticsDeltas(analytics["deltas"])