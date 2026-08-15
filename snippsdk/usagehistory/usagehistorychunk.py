class UsageHistoryChunk():
    def __init__(self, json: dict) -> None:
        self.day: str = json["day"]
        self.bytes: int = json["bytes"]
        self.count: int = json["count"]