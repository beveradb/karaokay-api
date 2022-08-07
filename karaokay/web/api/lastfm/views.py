from typing import Dict

import pylast
from fastapi import APIRouter
from loguru import logger

from karaokay.settings import settings
from karaokay.web.api.lastfm.schema import Query, RecentTracks

router = APIRouter()


@router.post("/recent_tracks", response_model=RecentTracks)
async def query_lastfm_recent_tracks(
    incoming_query: Query,
) -> Dict[str, list]:
    """
    Query Last.FM API for recent tracks for the specified user, return in response

    :param incoming_query: query with params dict and username
    :returns: simple success response
    """
    tracks = []
    username = incoming_query.username
    params = incoming_query.params
    limit = params.get('limit', 10)

    network = pylast.LastFMNetwork(
        api_key=settings.lastfm_api_key,
        api_secret=settings.lastfm_api_secret,
        username=username,
    )

    recent_tracks = network.get_user(username).get_recent_tracks(limit=limit)
    for i, track in enumerate(recent_tracks):
        printable = f"{track.playback_date}\t{track.track}"
        tracks.append(str(i + 1) + " " + printable)

    logger.debug(tracks)

    return {
        'tracks': tracks
    }
