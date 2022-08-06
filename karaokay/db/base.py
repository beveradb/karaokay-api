from ormar import ModelMeta

from karaokay.db.config import database
from karaokay.db.meta import meta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
