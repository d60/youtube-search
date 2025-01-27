from base64 import b64encode
from typing import Literal

DURATION = {
    '4 - 20 minutes': b'\x12\x02\x18\x03',
    'Over 20 minutes': b'\x12\x02\x18\x02',
    'Under 4 minutes': b'\x12\x02\x18\x01'
}

FEATURES = {
    '360°': b'\x12\x02x\x01',
    '3D': b'\x12\x028\x01',
    '4K': b'\x12\x02p\x01',
    'Creative Commons': b'\x12\x020\x01',
    'HD': b'\x12\x02 \x01',
    'HDR': b'\x12\x03\xc8\x01\x01',
    'Live': b'\x12\x02@\x01',
    'Location': b'\x12\x03\xb8\x01\x01',
    'Purchased': b'\x12\x02H\x01',
    'Subtitles/CC': b'\x12\x02(\x01',
    'VR180': b'\x12\x03\xd0\x01\x01'
}

SORT_BY = {
    'Rating': b'\x08\x01',
    'Relevance': b'',
    'Upload date': b'\x08\x02',
    'View count': b'\x08\x03'
}

TYPE = {
    'Channel': b'\x12\x02\x10\x02',
    'Movie': b'\x12\x02\x10\x04',
    'Playlist': b'\x12\x02\x10\x03',
    'Video': b'\x12\x02\x10\x01'
}

UPLOAD_DATE = {
    'Last hour': b'\x12\x02\x08\x01',
    'This month': b'\x12\x02\x08\x04',
    'This week': b'\x12\x02\x08\x03',
    'This year': b'\x12\x02\x08\x05',
    'Today': b'\x12\x02\x08\x02'
}

DURATION_KEYS = Literal['4 - 20 minutes', 'Over 20 minutes', 'Under 4 minutes']
FEATURES_KEYS = Literal['360°', '3D', '4K', 'Creative Commons', 'HD', 'HDR', 'Live', 'Location', 'Purchased', 'Subtitles/CC', 'VR180']
SORT_BY_KEYS = Literal['Rating', 'Relevance', 'Upload date', 'View count']
TYPE_KEYS = Literal['Channel', 'Movie', 'Playlist', 'Video']
UPLOAD_DATE_KEYS = Literal['Last hour', 'This month', 'This week', 'This year', 'Today']


def build_search_params(duration, features, sort_by, type, upload_date) -> str:
    keys = (duration, features, sort_by, type, upload_date)
    mappings = (DURATION, FEATURES, SORT_BY, TYPE, UPLOAD_DATE)
    filters = []
    for key, mapping in zip(keys, mappings):
        if key is None:
            continue
        if key not in mapping:
            raise ValueError(f'Invalid key: {key}')
        filters.append(mapping[key])
    return b64encode(b''.join(filters)).decode()
