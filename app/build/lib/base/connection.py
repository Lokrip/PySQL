import psycopg2
from app.PySql.logs.errors import errors

class Connection:
    
    def __init__(self, **kwargs) -> None:
        self.db_name = kwargs.get('DATEBASE_NAME')
        self.user = kwargs.get('USER')
        self.password = kwargs.get('PASSWORD')
        self.host = kwargs.get('HOST')
        self.port = kwargs.get('PORT')
        
    
    def __connection__(self):
        if not self.db_name:
            errors.database_error()
        
        print(self.db_name, self.user)