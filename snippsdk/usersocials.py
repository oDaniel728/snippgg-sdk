from typing import Optional


class UserSocials():
    def __init__(self, json: dict) -> None:
        self.github: Optional[str] = json.get("github")
        self.discord: Optional[str] = json.get("discord")
        self.roblox: Optional[str] = json.get("roblox")