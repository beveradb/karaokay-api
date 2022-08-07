from pydantic import BaseModel


class Query(BaseModel):
    """Simple Query model."""

    username: str


class Response(BaseModel):
    """Simple Response model."""

    message: str
    username: str
