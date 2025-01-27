from .base import BaseParser


class Playlist(BaseParser):
    def __init__(self, data: dict) -> None:
        super().__init__(data, 'lockupViewModel', 'id')

    @property
    def id(self) -> str:
        return self.data['contentId']

    @property
    def title(self) -> str:
        return self.data['metadata']['lockupMetadataViewModel']['title']['content']

    @property
    def channel_name(self) -> str:
        return self.data['metadata']['lockupMetadataViewModel']['metadata']['contentMetadataViewModel']['metadataRows'][0]['metadataParts'][0]['text']['content']

    @property
    def video_count(self) -> str:
        return self.data['contentImage']['collectionThumbnailViewModel']['primaryThumbnail']['thumbnailViewModel']['overlays'][0]['thumbnailOverlayBadgeViewModel']['thumbnailBadges'][0]['thumbnailBadgeViewModel']['text']
