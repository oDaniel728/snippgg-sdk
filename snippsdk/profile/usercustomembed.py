from typing import Optional


class UserCustomEmbed():
    def __init__(self, json: dict) -> None:
        self.title: Optional[str] = json.get("title")
        self.small_text: Optional[str] = json.get("smallText")
        self.theme_color: Optional[str] = json.get("themeColor")