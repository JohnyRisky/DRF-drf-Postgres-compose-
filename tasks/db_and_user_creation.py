import psycopg2


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres111",
    host="localhost",
    port="5432"
)

conn.autocommit = True

with conn.cursor() as cur:
    cur.execute("CREATE USER todolist_user WITH PASSWORD 'postgres111';")
    cur.execute("CREATE DATABASE todolist OWNER todolist_user;")
    cur.execute("GRANT ALL PRIVILEGES ON DATABASE todolist TO todolist_user;")

print("База данных и пользователь успешно созданы.")
conn.close()