from PySql.base.connection import Connection
import psycopg2

def settigns(connect = False, **kwrags):
    if connect:
        try:
            """ <>Connecting to the database When connecting, 
            it may give an error, you can read them at this URL 
            </>"""
            connection: Connection = Connection(**kwrags)
            connection.__connection__()
        except:
            None