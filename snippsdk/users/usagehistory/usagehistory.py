from snippsdk.users.usagehistory.historystats import HistoryStats
from snippsdk.users.usagehistory.usagehistorychunk import UsageHistoryChunk

class UsageHistory():
    def __init__(self, json: dict) -> None:
        self.history: list[UsageHistoryChunk] = [
            UsageHistoryChunk(chunk) for chunk in json.get("history", [])
        ]
        self.stats: HistoryStats = HistoryStats(json["stats"])