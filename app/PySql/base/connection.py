import psycopg2
from psycopg2 import DatabaseError

from PySql.logs.log import errors

class Connection:
    """
    A class to manage PostgreSQL database connections.

    Attributes:
    -----------
    db_name : str
        The name of the database to connect to.
    user : str
        The username to authenticate with.
    password : str
        The password for the user.
    host : str
        The host address of the database (default: 'localhost').
    port : str
        The port to connect to (default: '5432').
    """
    
    def __init__(self, **kwargs) -> None:
        self.db_name = kwargs.get('DB_NAME')
        self.user = kwargs.get('USER')
        self.password = kwargs.get('PASSWORD')
        self.host = kwargs.get('HOST', 'localhost')
        self.port = kwargs.get('PORT', '5432')
        
        if not self.db_name:
            raise ValueError("Database name is required.")
        if not self.user or not self.password:
            raise ValueError("User and password are required.")
    
    def is_valid_connect(self, **kwargs):
        """Проверка валидности данных для подключения к базе данных"""
        try:
            conn_params = {
                'dbname': self.db_name,
                'user': self.user,
                'password': self.password,
                'host': self.host,
                'port': self.port
            }
            
            return conn_params  
        except KeyError as ke:
            print(f"Key error: {ke}")
            raise KeyError(f"Missing connection parameter: {ke}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise e
            
    
    def __connection__(self):
        """
        Establish a connection to the PostgreSQL database.

        Returns:
        --------
        connection:
            A psycopg2 connection object.
        """
        
        if not self.db_name:
            errors.database_error()
        
        try:
            conn_params = self.is_valid_connect()
            if conn_params: 
                conn = psycopg2.connect(
                    **conn_params
                )
                return conn
        except DatabaseError as db_err:
            errors.database_error()
            raise
        except Exception as e:
            print(f"An unexpected error occurred while connecting: {e}")
            raise
        