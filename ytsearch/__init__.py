from typing import Any

import requests

from .params import DURATION_KEYS, FEATURES_KEYS, SORT_BY_KEYS, UPLOAD_DATE_KEYS, build_search_params
from .parsers.channel import Channel
from .parsers.playlist import Playlist
from .parsers.result import Result, parse_response
from .parsers.video import Video


class Search:
    def __init__(self) -> None:
        self.base_url = 'https://www.youtube.com/youtubei/v1'
        self.data = {
            "context": {
                "client": {
                    "clientName": "WEB",
                    "clientVersion": "2.20231110.00.00",
                }
            }
        }

    def fetch_json(self, method, path, *args, **kwargs) -> Any:
        response = requests.request(method, self.base_url + path, *args, **kwargs)
        return response.json()

    def base_search(self, query: str, sp: str, continuation: str = None) -> dict:
        """Base search function"""
        data = self.data
        if continuation:
            data.update(continuation=continuation)
        else:
            data.update(query=query, params=sp)
        response = self.fetch_json('POST', '/search', json=data)
        return response

    def search_videos(
        self,
        query: str | None = None,
        duration: DURATION_KEYS | None = None,
        features: list[FEATURES_KEYS] | None = None,
        sort_by: SORT_BY_KEYS | None = None,
        upload_date: UPLOAD_DATE_KEYS | None = None,
        continuation: str | None = None
    ) -> Result[Video]:
        """Searches videos and returns parsed Video object."""
        sp = build_search_params(duration, features, sort_by, 'Video', upload_date)
        response = self.base_search(query, sp, continuation)
        return parse_response(response, self.search_videos)

    def search_channels(
        self,
        query: str | None = None,
        sort_by: SORT_BY_KEYS | None = None,
        continuation: str | None = None
    ) -> Result[Channel]:
        """Searches channels and returns parsed Channel object."""
        sp = build_search_params(None, None, sort_by, 'Channel', None)
        response = self.base_search(query, sp, continuation)
        return parse_response(response, self.search_channels)

    def search_playlists(
        self,
        query: str | None = None,
        sort_by: SORT_BY_KEYS | None = None,
        continuation: str | None = None
    ) -> Result[Playlist]:
        """Searches channels and returns parsed Channel object."""
        sp = build_search_params(None, None, sort_by, 'Playlist', None)
        response = self.base_search(query, sp, continuation)
        return parse_response(response, self.search_playlists)

    def search(self, query: str | None = None, continuation: str | None = None):
        """Mixed search"""
        sp = build_search_params(None, None, None, None, None)
        response = self.base_search(query, sp, continuation)
        return parse_response(response, self.search)
