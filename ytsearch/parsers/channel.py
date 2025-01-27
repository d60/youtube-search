from .base import BaseParser


class Channel(BaseParser):
    def __init__(self, data: dict) -> None:
        super().__init__(data, 'channelRenderer', 'id')

    @property
    def id(self) -> str:
        return self.data.get('channelId')

    @property
    def name(self) -> str:
        return self.data['title']['simpleText']

    @property
    def thumbnails(self) -> str:
        return self.data['thumbnail']['thumbnails']

    @property
    def description(self) -> str:
        return ''.join((
            run['text']
            for run in self.data['descriptionSnippet']['runs']
        ))

    @property
    def canonical(self) -> str:
        return self.data['subscriberCountText']['simpleText']

    @property
    def subscribers(self) -> str:
        return self.data['videoCountText']['simpleText']