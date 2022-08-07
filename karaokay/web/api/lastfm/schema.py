from pydantic import BaseModel


class Query(BaseModel):
    """Simple Query model."""

    username: str
    params: dict


class RecentTracks(BaseModel):
    """Simple RecentTracks model."""

    tracks: list
