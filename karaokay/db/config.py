from databases import Database

from karaokay.settings import settings

database = Database(str(settings.db_url))
