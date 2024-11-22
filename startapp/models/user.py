import sys
import os

from psycopg2.extensions import connection as psycopg2_connection
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from startapp.settings.connection import CONNECTION
from PySql.models.base import BaseModel


# class User(BaseModel):
#     def __init__(self, connection: psycopg2_connection = CONNECTION) -> None:
#         super().__init__(connection)
#         self.add_field('name', max_length=100, unique=True)
#         self.add_field('email', max_length=255, unique=True)
#         self.add_field('password', max_length=255)
#         self.create_table()

class Category(BaseModel):
    def __init__(self, connection: psycopg2_connection = CONNECTION):
        super().__init__(connection)
        self.add_field('name', max_length=100, unique=True)
        self.create_table()
            
class Product(BaseModel):
    def __init__(self, connection: psycopg2_connection = CONNECTION) -> None:
        super().__init__(connection)
        self.add_field('name', max_length=50)
        self.add_field('price', max_length=9)
        self.add_field('category', foreign_key=Category())
        self.create_table();


# USER = User()
CATEGORY = Category()
PRODUCT = Product()
