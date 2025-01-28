from typing import Generator, Generic, TypeVar

from .channel import Channel
from .playlist import Playlist
from .video import Video

PARSER_MAPPING = {
    'videoRenderer': Video,
    'channelRenderer': Channel,
    'lockupViewModel': Playlist
}


def get_parser(item: str):
    renderer_name = list(item.keys())[0]
    return PARSER_MAPPING.get(renderer_name)

T = TypeVar('T')


class Result(Generic[T]):
    def __init__(self, items, next, continuation) -> None:
        """Next: Callable that takes one argument (continuation) and returns Result object."""
        self.__items = items
        self.__next = next
        self.__continuation = continuation

    def next(self) -> 'Result[T]':
        return self.__next(continuation=self.__continuation)

    def __iter__(self) -> Generator[T, None, None]:
        for item in self.__items:
            parser = get_parser(item)
            if parser:
                yield parser(item)

    def __repr__(self) -> str:
        return f'<Result count={len(self.__items)}>'


def extract_contents(response):
    return response['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents']


def extract_continuation_items(response):
    return response['onResponseReceivedCommands'][0]['appendContinuationItemsAction']['continuationItems']


def extract_continuation(content):
    return content['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']


def parse_response(response, next):
    try:
        contents = extract_contents(response)
    except KeyError:
        contents = extract_continuation_items(response)
    items = contents[0]['itemSectionRenderer']['contents']
    continuation = None
    if len(contents) > 1:
        continuation = extract_continuation(contents[1])
    return Result(items, next, continuation)
