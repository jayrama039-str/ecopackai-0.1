import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecopackai",
    user="postgres",
    password="1234",
    port=5432
)

cursor = conn.cursor()

print("Database connected successfully")