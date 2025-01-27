# YouTube Search

## Installing
```
pip install git+https://github.com/d60/youtube-search.git
```

## Quick Examples
```python
from ytsearch import Search

search = Search()

# Search videos
videos = search.search_videos(
    'search query here',
    duration='4 - 20 minutes',
    sort_by='Rating',
    upload_date='This year'
)
next_videos = videos.next()

# Search channels
channels = search.search_channels(
    'search query here',
)
next_channels = channels.next()

# Search playlists
playlists = search.search_playlists(
    'search query here',
)
next_playlists = playlists.next()
```