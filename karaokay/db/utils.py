from sqlalchemy import text
from sqlalchemy.engine import create_engine

from karaokay.settings import settings


def create_database() -> None:
    """Create a databse."""
    engine = create_engine(str(settings.db_url.with_path("/mysql")))

    with engine.connect() as conn:
        database_existance = conn.execute(
            text(
                "SELECT 1 FROM INFORMATION_SCHEMA.SCHEMATA"  # noqa: S608
                f" WHERE SCHEMA_NAME='{settings.db_base}';",
            ),
        )
        database_exists = database_existance.scalar() == 1

    if database_exists:
        drop_database()

    with engine.connect() as conn:  # noqa: WPS440
        conn.execute(
            text(
                f"CREATE DATABASE {settings.db_base};",
            ),
        )


def drop_database() -> None:
    """Drop current database."""
    engine = create_engine(str(settings.db_url.with_path("/mysql")))
    with engine.connect() as conn:
        conn.execute(text(f"DROP DATABASE {settings.db_base};"))
