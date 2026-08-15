class UserLimitUsage():
    def __init__(self, json: dict) -> None:
        self.used: int = json["used"]
        self.limit: int = json["limit"]
        self.used_percent: float = json["usedPercent"]
        self.window_start: str = json["windowStart"]
        self.window_end: str = json["windowEnd"]
        self.resets_in_seconds: int = json["resetsInSeconds"]

class UserLimit():
    def __init__(self, json: dict) -> None:
        self.plan: str = json["plan"]
        self.max_file_size: int = json["maxFileSize"]
        self.usage: UserLimitUsage = UserLimitUsage(json["usage"])