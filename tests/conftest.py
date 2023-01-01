# type: ignore
# pylint: disable=missing-module-docstring,missing-class-docstring,no-self-use
# pylint: disable=missing-function-docstring,too-few-public-methods

import asyncio
import json
import sys

import pytest
import simplejson


# pylint: disable=unused-argument
def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    # The default event loop on Windows causes an exception saying Event loop
    # closed to be thrown on Python 3.8 with Windows
    # https://github.com/encode/httpx/issues/914
    if (
        sys.version_info[0] == 3
        and sys.version_info[1] >= 8
        and sys.platform.startswith("win")
    ):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


@pytest.fixture
def response_mock(use_json_decoder=True):
    class ResponseMock:
        def __init__(self):
            self.status_code = 403
            # simulate a banned user
            self.text = """<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.15.5 (Ubuntu)</center>
</body>
</html>
"""

        def json(self):
            if use_json_decoder:
                raise json.decoder.JSONDecodeError("Failed", "", 0)
            raise simplejson.JSONDecodeError("Failed", "", 0)

    return ResponseMock()


@pytest.fixture
def aio_response_mock(use_json_decoder=True):
    class ResponseMock:
        def __init__(self):
            self.status = 403

        async def json(self):
            if use_json_decoder:
                raise json.decoder.JSONDecodeError("Failed", "", 0)
            raise simplejson.JSONDecodeError("Failed", "", 0)

        async def text(self):
            """Simulate a banned user"""
            return """<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.15.5 (Ubuntu)</center>
</body>
</html>
"""

    return ResponseMock()


@pytest.fixture
def response_non_dict_mock():
    class ResponseMock:
        def __init__(self):
            self.status_code = 200
            self.headers = {"Content-Type": "application/json"}

        def json(self):
            return ["One Piece", "Jojo"]

    return ResponseMock()


@pytest.fixture
def aio_response_non_dict_mock():
    class ResponseMock:
        def __init__(self):
            self.status = 200
            self.headers = {"Content-Type": "application/json"}

        async def json(self):
            return ["One Piece", "Jojo"]

    return ResponseMock()


@pytest.fixture
def anime_keys():
    return {
        "mal_id",
        "url",
        "images",
        "trailer",
        "approved",
        "titles",
        "title",
        "title_english",
        "title_japanese",
        "title_synonyms",
        "type",
        "source",
        "episodes",
        "status",
        "airing",
        "aired",
        "duration",
        "rating",
        "score",
        "scored_by",
        "rank",
        "popularity",
        "members",
        "favorites",
        "synopsis",
        "background",
        "season",
        "year",
        "broadcast",
        "producers",
        "licensors",
        "studios",
        "genres",
        "explicit_genres",
        "themes",
        "demographics",
    }


@pytest.fixture
def paginated_answer_keys():
    return {
        "pagination",
        "data",
    }


@pytest.fixture
def episode_keys():
    return {
        "mal_id",
        "url",
        "title",
        "title_japanese",
        "title_romanji",
        "score",
        "aired",
        "filler",
        "recap",
        "forum_url",
    }


@pytest.fixture
def manga_keys():
    return {
        "mal_id",
        "url",
        "images",
        "approved",
        "titles",
        "title",
        "title_english",
        "title_japanese",
        "type",
        "chapters",
        "volumes",
        "status",
        "publishing",
        "published",
        "score",
        "scored_by",
        "rank",
        "popularity",
        "members",
        "favorites",
        "synopsis",
        "background",
        "authors",
        "serializations",
        "genres",
        "explicit_genres",
        "themes",
        "demographics",
    }


@pytest.fixture
def character_keys():
    return {
        "mal_id",
        "url",
        "images",
        "name",
        "name_kanji",
        "nicknames",
        "favorites",
        "about",
    }


@pytest.fixture
def person_keys():
    return {
        "mal_id",
        "url",
        "website_url",
        "images",
        "name",
        "given_name",
        "family_name",
        "alternate_names",
        "birthday",
        "favorites",
        "about",
    }


@pytest.fixture
def search_keys():
    return {
        "pagination",
        "data",
    }


@pytest.fixture
def season_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "season_name",
        "season_year",
        "anime",
    }


@pytest.fixture
def seasonal_anime_keys():
    return {
        "mal_id",
        "url",
        "title",
        "image_url",
        "synopsis",
        "type",
        "airing_start",
        "episodes",
        "members",
        "genres",
        "source",
        "producers",
        "score",
        "licensors",
        "r18",
        "kids",
        "continuing",
    }


@pytest.fixture
def season_archive_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "archive"}


@pytest.fixture
def archived_years_keys():
    return {"year", "seasons"}


@pytest.fixture
def schedule_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "monday"}


@pytest.fixture
def top_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "top"}


@pytest.fixture
def top_anime_keys():
    return {
        "mal_id",
        "rank",
        "url",
        "image_url",
        "title",
        "type",
        "score",
        "members",
        "start_date",
        "episodes",
    }


@pytest.fixture
def genre_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_url",
        "item_count",
        "anime",
    }


@pytest.fixture
def producer_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "meta", "anime"}


@pytest.fixture
def subset_anime_keys():
    return {
        "mal_id",
        "url",
        "title",
        "image_url",
        "synopsis",
        "type",
        "episodes",
        "members",
        "genres",
        "source",
        "producers",
        "score",
        "licensors",
        "r18",
        "kids",
    }


@pytest.fixture
def magazine_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "meta", "manga"}


@pytest.fixture
def magazine_manga_keys():
    return {
        "mal_id",
        "url",
        "title",
        "image_url",
        "synopsis",
        "type",
        "volumes",
        "members",
        "genres",
        "authors",
        "score",
        "serialization",
    }


@pytest.fixture
def user_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "username",
        "url",
        "image_url",
        "last_online",
        "gender",
        "birthday",
        "location",
        "joined",
        "anime_stats",
        "manga_stats",
        "favorites",
        "about",
    }


@pytest.fixture
def animelist_keys():
    return {"request_hash", "request_cached", "request_cache_expiry", "anime"}


@pytest.fixture
def club_keys():
    return {
        "request_hash",
        "request_cached",
        "request_cache_expiry",
        "mal_id",
        "url",
        "image_url",
        "title",
        "members_count",
        "pictures_count",
        "category",
        "created",
        "type",
        "staff",
        "anime_relations",
        "manga_relations",
        "character_relations",
    }


@pytest.fixture
def header_keys():
    return {
        "Expires",
        "Last-Modified",
        "X-Request-Fingerprint",
    }
