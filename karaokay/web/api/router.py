from fastapi.routing import APIRouter

from karaokay.web.api import echo, monitoring, lastfm

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(lastfm.router, prefix="/lastfm", tags=["lastfm"])
