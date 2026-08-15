from typing import Optional


class UserUpload():
    def __init__(self, json: dict) -> None:
        self.url: str = json["url"]
        self.code: str = json["code"]
        self.title: str = json["title"]
        self.description: Optional[str] = json.get("description")
        self.created: str = json["created"]
        self.public: bool = json["public"]
        self.is_album: bool = json["isAlbum"]