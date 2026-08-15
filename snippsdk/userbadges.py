class UserBadges():
    def __init__(self, json: dict) -> None:
        self.verified: bool = json["verified"]
        self.staff: bool = json["staff"]
        self.partner: bool = json["partner"]
        self.bug_hunter_tier: int = json["bugHunterTier"]
        self.translator: bool = json["translator"]
        self.plus: bool = json["plus"]
