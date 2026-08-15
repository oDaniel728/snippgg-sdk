class HistoryStats():

    class _UBiggestDay():
        def __init__(self, json: dict) -> None:
            self.day: str = json["day"]
            self.bytes: int = json["bytes"]

    def __init__(self, json: dict) -> None:
        self.total_bytes: int = json["totalBytes"]
        self.total_uploads: int = json["totalUploads"]
        self.active_days: int = json["activeDays"]
        self.current_streak: int = json["currentStreak"]
        self.biggest_day: HistoryStats._UBiggestDay = HistoryStats._UBiggestDay(json["biggestDay"])
        self.window_days: int = json["windowDays"]
