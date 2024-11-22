from PySql.settings.config import settigns
from PySql.models.base import BaseModel

PARAMS = {
    'DB_NAME': 'PySqlTest',
    "USER": 'lokrip',
    'PASSWORD': 'lol1234lol1234',
    'HOST': 'localhost',
    'PORT': '5432'
}

CONNECTION = settigns(connect=True, **PARAMS)
