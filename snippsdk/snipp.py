from typing import Literal, Optional, overload

import httpx

from snippsdk.analytics.useranalytics import UserAnalytics
from snippsdk.profile.profile import MyUserProfile, UserProfile
from snippsdk.usagehistory.usagehistory import UsageHistory

def _remove_nil_values(dict: dict) -> dict:
    return {k: v for k, v in dict.items() if v is not None}

class Snipp():
    __base_path = "https://api.snipp.gg"
    def __init__(self, API_KEY: str) -> None:
        self.API_KEY = API_KEY

    def __request(self, method: str, url: str, params: dict = {}, headers: dict = {}) -> httpx.Response:
        return httpx.request(method, f"{self.__base_path}/{url}", params=params, headers={"api-key": self.API_KEY} | headers)

    def __get(self, url: str, params: dict = {}, headers: dict = {}) -> httpx.Response:
        return self.__request("GET", url, params=params, headers=headers)

    def __post(self, url: str, params: dict = {}, headers: dict = {}) -> httpx.Response:
        return self.__request("POST", url, params=params, headers=headers)

    @overload
    def get_user(
        self, 
        user_id: int, 
        include_posts: Optional[bool] = None, 
        posts_limit: Optional[int] = None,
    ) -> UserProfile: ...
    @overload
    def get_user(
        self, 
        user_id: Literal["@me"], 
        include_posts: Optional[bool] = None, 
        posts_limit: Optional[int] = None,
    ) -> MyUserProfile: ...

    def get_user(self, user_id: int | Literal["@me"], include_posts: Optional[bool] = None, posts_limit: Optional[int] = None) -> UserProfile | MyUserProfile:

        if posts_limit:
            if posts_limit > 50:
                raise ValueError("Posts limit must be less than or equal to 50")
            elif posts_limit < 0:
                raise ValueError("Posts limit must be greater than or equal to 0")
            
        data = self.__get(
            f"users/{user_id}", 
            params=_remove_nil_values(
                {
                    "includePosts": include_posts, 
                    "postsLimit": posts_limit
                }
            )
        )
        if user_id == "@me":
            return MyUserProfile(data.json())
        return UserProfile(data.json())

    def get_usage_history(self) -> UsageHistory:
        data = self.__get("usage-history")
        return UsageHistory(data.json())

    def get_analytics(self, range: Literal["7", "30", "90", "365"] = "30") -> UserAnalytics:
        data = self.__get(
            "analytics",
            params=_remove_nil_values({"range": int(range)})
        )
        return UserAnalytics(data.json())

