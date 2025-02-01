# app.py

import psycopg2
from psycopg2 import sql

# Параметри підключення до БД
DB_HOST = "postgres"
DB_PORT = "5432"
DB_USER = "app_user"
DB_PASSWORD = "secure_password"
DB_NAME = "app_db"

try:
    # Підключення до бази даних
    connection = psycopg2.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    cursor = connection.cursor()

    # Створення таблиці
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );
    """)

    # Вставка даних
    cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30), ('Jane Doe', 25) ON CONFLICT DO NOTHING;")
    connection.commit()

    # Вибірка даних
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    # Виведення результатів
    print("Users in database:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")
finally:
    if connection:
        cursor.close()
        connection.close()
