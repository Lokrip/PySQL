import psycopg2
from psycopg2.extensions import connection as psycopg2_connection
from contextlib import contextmanager
from PySql.logs.log import errors

class PsyCopgMixins:
    def __init__(self, connection: psycopg2_connection) -> None:
        self.connection = connection
    
    @staticmethod
    def cursor_fetchall(cursor, is_get = False):
        if not is_get:
            cursor.fetchall()
        else:
            return cursor.fetchall()
     
    @staticmethod
    def execute_query(cursor, query):
        errors.execute_query_log(f"Executing query: {query}")
        cursor.execute(query)
    
    def commit(self) -> None:
        self.connection.commit()
    
    @contextmanager
    def get_cursor(self):
        cursor = self.connection.cursor()
        try:
            yield cursor
        finally:
            cursor.close()


class ModelFields(PsyCopgMixins):
    def __init__(self, connection: psycopg2_connection, model_name) -> None:
        super().__init__(connection)
        self.modelName = model_name
        self.fields = {}
        self.add_default_id_field()
        
    def add_default_id_field(self):
        # Добавляем поле 'id' по умолчанию
        self.fields['id'] = {'type': 'SERIAL PRIMARY KEY'}

    def add_field(
        self, 
        field_name, 
        max_length=None, 
        unique=False,
        foreign_key=None,
    ):
        field_info = {}
        
        if foreign_key:
            field_info['foreign_key'] = foreign_key
        else:
            field_info['max_length'] = max_length
            field_info['unique'] = unique
        
        self.fields[field_name] = field_info
    
    def get_fields(self):
        return self.fields

class SQLManager(ModelFields):
    def __init__(self, connection, model_name):
        super().__init__(connection, model_name)
        
        
    def create_table(self):
        table_name = self.modelName.lower()
        
        if not self.get_fields():
            raise ValueError('Not Found fields')
        
        query = self._build_create_table_query(table_name)
        return query;
        with self.get_cursor() as cursor:
            self.execute_query(cursor, query)
            self.commit()
            
    def _build_create_table_query(self, table_name):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        fields_query = []

        for field_name, attributes in self.fields.items():
            if field_name.lower() == 'id' and attributes.get('type') == 'SERIAL PRIMARY KEY':
                fields_query.append(f"{field_name} {attributes['type']}")
                continue
            
            max_length = attributes.get('max_length', None)
            unique = attributes.get('unique', False)
            
            if 'foreign_key' in attributes:
                foreign_key = attributes.get('foreign_key', None)
                if foreign_key is not None:
                    id_model = foreign_key.fields.get('id', None)
                    class_name = foreign_key.__name__
                    
                    print(id_model, class_name)
                else:
                    class_name = None
                    
                return
                
                # field_type = (
                    
                # )
            else:
                field_type = (
                    f"VARCHAR({max_length})" 
                    if max_length is not None
                    else "TEXT"
                )
            
            field_definition = f"{field_name} {field_type} NOT NULL"
            
            if unique: 
                field_definition += ' UNIQUE'
                
            fields_query.append(field_definition)
            
        query += ", ".join(fields_query) + ');'
        return query

class BaseModel(SQLManager):
    def __init__(self, connection: psycopg2_connection) -> None:
        super().__init__(connection, self.get_table_name())
        
    def get_table_name(self):
        return f'"{self.__class__.__name__.lower()}"' if self.__class__.__name__.lower() in (
            'user', 'select', 'insert', 'update', 'delete', 'where'
        ) else self.__class__.__name__.lower()
    
    @staticmethod
    def print_connect(cls):
        print(cls)