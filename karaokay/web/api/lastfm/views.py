from typing import Dict

from fastapi import APIRouter

from karaokay.web.api.lastfm.schema import Query, Response

router = APIRouter()


@router.post("/", response_model=Response)
async def query_lastfm_songs(
    incoming_query: Query,
) -> Dict[str, str]:
    """
    Sends echo back to user.

    :param incoming_query: incoming query (should include username).
    :returns: simple success response
    """

    return {'message': 'ok', 'username': incoming_query.username}
