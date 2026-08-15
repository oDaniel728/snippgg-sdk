class UserBadges():
    """
    Represents an user's badges.

    Attributes:
        verified (bool): Whether the user is verified.
        staff (bool): Whether the user is a staff member.
        partner (bool): Whether the user is a partner.
        bug_hunter_tier (int): The user's bug hunter tier.
        translator (bool): Whether the user is a translator.
        plus (bool): Whether the user is a plus user.    
    """
    def __init__(self, json: dict) -> None:
        self.verified: bool = json["verified"]
        self.staff: bool = json["staff"]
        self.partner: bool = json["partner"]
        self.bug_hunter_tier: int = json["bugHunterTier"]
        self.translator: bool = json["translator"]
        self.plus: bool = json["plus"]
