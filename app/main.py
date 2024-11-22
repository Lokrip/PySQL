import psycopg2
import datetime

conn_params = {
    'dbname': 'PySqlTest',
    "user": 'lokrip',
    'password': 'lol1234lol1234',
    'host': 'localhost',
    'port': '5432'
}


conn = psycopg2.connect(**conn_params)
cur = conn.cursor() #Открывает курсор для выполнения операций с базой данных


# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num INTEGER NOT NUll, data varchar(30) NOT NULL)") #Делаем запрос

# cur.execute("INSERT INTO test (num, data) VALUES (10, 'Hello world')")

conn.commit()

cur.execute("SELECT * FROM test WHERE id = 1 AND num = 10")

records = cur.fetchall() #Получить результаты запроса


cur.close()
conn.close()

print('yes')