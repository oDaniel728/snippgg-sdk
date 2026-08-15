from typing import Optional

from snippsdk.userbadges import UserBadges
from snippsdk.usercustomembed import UserCustomEmbed
from snippsdk.userlimits import UserLimit
from snippsdk.usersocials import UserSocials
from snippsdk.userupload import UserUpload

class UserProfile():
    def __init__(self, json: dict) -> None:
        self.userid: str = json["user"]["id"]
        self.username: str = json["user"]["username"]
        self.avatar: Optional[str] = json["user"].get("avatar")
        self.banner: Optional[str] = json["user"].get("banner")
        self.nickname: Optional[str] = json["user"].get("nickname")
        self.bio: Optional[str] = json["user"].get("bio")

        socials = json["user"].get("socials", {})
        self.socials: Optional[UserSocials] = UserSocials(socials) if socials else None

        self.plus: bool = json["user"]["plus"]
        self.enterprise: bool = json["user"]["enterprise"]
        self.suspended: bool = json["user"]["suspended"]
        self.created: str = json["user"]["created"]

        custom_embed = json["user"].get("customEmbed")
        self.custom_embed: Optional[UserCustomEmbed] = UserCustomEmbed(custom_embed) if custom_embed else None

        self.badges: UserBadges = UserBadges(json["user"]["badges"])

        self.public_uploads: list[UserUpload] = [UserUpload(upload) for upload in json["user"].get("publicUploads", [])]

        self.blocked_by_you: Optional[bool] = json["user"].get("blockedByYou")

        self.json = json

class MyUserProfile(UserProfile):
    def __init__(self, json: dict) -> None:
        super().__init__(json)
        self.uploads: int = json["user"]["uploads"]
        self.api_key: str = json["user"]["apiKey"]
        self.limits: UserLimit = UserLimit(json["user"]["limits"])