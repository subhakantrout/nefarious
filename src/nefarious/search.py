import requests
from typing import List
from nefarious.jackett import get_jackett_search_url
from nefarious.models import NefariousSettings
from nefarious.utils import fetch_jackett_indexers

MEDIA_TYPE_TV = 'tv'
MEDIA_TYPE_MOVIE = 'movie'


class SearchTorrents:
    results: list = None
    ok = True
    error_content = None
    nefarious_settings: NefariousSettings
    search_seed_only = False

    def __init__(self, media_type: str, query: str, search_seed_only: bool = False):
        assert media_type in [MEDIA_TYPE_TV, MEDIA_TYPE_MOVIE]
        self.search_seed_only = search_seed_only
        self.nefarious_settings = NefariousSettings.get()

        params = {
            'apikey': self.nefarious_settings.jackett_token,
            'Query': query,
            'Category[]': self._categories(media_type),
            'Tracker[]': self._trackers(),
        }

        res = requests.get(get_jackett_search_url(self.nefarious_settings), params, timeout=90)

        if res.ok:
            response = res.json()
            self.results = response['Results']
        else:
            self.ok = False
            self.error_content = res.content

    def _categories(self, media_type: str) -> list:
        # https://github.com/nZEDb/nZEDb/blob/dev/docs/newznab_api_specification.txt
        cat_movies = [2000, 2010, 2030, 2040, 2050, 2060, 2070]
        cat_tv = [5000, 5010, 5020, 5030, 5040, 5060, 5070, 5080]
        if media_type == MEDIA_TYPE_MOVIE:
            return cat_movies
        else:
            return cat_tv

    def _trackers(self) -> list:
        trackers = fetch_jackett_indexers(self.nefarious_settings)
        seed_only_trackers = []

        # fetch all active indexers and remove any configured as "seed only"
        if self.nefarious_settings.jackett_indexers_seed:
            for tracker, seed_only in self.nefarious_settings.jackett_indexers_seed.items():
                if seed_only and tracker in trackers:
                    seed_only_trackers.append(tracker)
                    trackers.remove(tracker)

        if self.search_seed_only:
            return seed_only_trackers
        else:
            return trackers


class SearchTorrentsCombined:
    results = []
    ok = True
    error_content = ''

    def __init__(self, search_torrents: List[SearchTorrents]):
        self.ok = any([search.ok for search in search_torrents])
        for search in search_torrents:
            if search.ok:
                self.results += search.results
            else:
                self.error_content += '\n{}'.format(search.error_content)
