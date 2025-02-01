# Використовуємо офіційний образ Python
FROM python:3.9-slim

# Встановлюємо залежності
RUN pip install psycopg2-binary

# Копіюємо скрипт в контейнер
COPY app.py /app.py

# Вказуємо команду, яка має виконуватись
CMD ["python", "/app.py"]
