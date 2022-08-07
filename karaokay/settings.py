import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic import BaseSettings
from yarl import URL

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters are just default values - they can be configured
    with environment variables, prefixed as per inline examples below.
    """

    # env var: KARAOKAY_HOST
    host: str = "127.0.0.1"
    # env var: KARAOKAY_PORT
    port: int = 8000
    # quantity of workers for uvicorn  | env var: KARAOKAY_WORKERS_COUNT
    workers_count: int = 1
    # Enable uvicorn reloading | env var: KARAOKAY_RELOAD
    reload: bool = False

    # Current environment | env var: KARAOKAY_ENVIRONMENT
    environment: str = "dev"

    # env var: KARAOKAY_LOG_LEVEL
    log_level: LogLevel = LogLevel.INFO

    # env var: KARAOKAY_LASTFM_API_KEY
    lastfm_api_key: str = "test"
    # env var: KARAOKAY_LASTFM_API_SECRET
    lastfm_api_secret: str = "test"

    # Variables for the database
    # env var: KARAOKAY_DB_HOST / KARAOKAY_DB_PORT / KARAOKAY_DB_USER / KARAOKAY_DB_PASS
    db_host: str = "localhost"
    db_port: int = 3306
    db_user: str = "karaokay"
    db_pass: str = "karaokay"
    db_base: str = "karaokay"
    db_echo: bool = False

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="mysql",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
        )

    class Config:
        env_file = ".env"
        env_prefix = "KARAOKAY_"
        env_file_encoding = "utf-8"


settings = Settings()
