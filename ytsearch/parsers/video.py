from .base import BaseParser


class Video(BaseParser):
    def __init__(self, data: dict) -> None:
        super().__init__(data, 'videoRenderer', 'id')

    @property
    def id(self) -> str:
        return self.data.get('videoId')

    @property
    def thumbnails(self) -> dict:
        return self.data['thumbnail']['thumbnails']

    @property
    def title(self) -> str:
        return self.data['title']['runs'][0]['text']

    @property
    def channel_name(self) -> str:
        return self.data['ownerText']['runs'][0]['text']

    @property
    def published_time(self) -> str:
        return self.data['publishedTimeText']['simpleText']

    @property
    def length(self) -> str:
        return self.data['lengthText']['simpleText']

    @property
    def view_count(self) -> str:
        return self.data['viewCountText']['simpleText']
