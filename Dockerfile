# Використовуємо офіційний образ Python
FROM python:3.11-slim

# Встановлюємо робочий каталог
WORKDIR /app

# Копіюємо необхідні файли в контейнер
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі інші файли проєкту в контейнер
COPY . /app/

# Вказуємо команду для запуску
CMD ["python", "/app/testify/manage.py", "runserver", "0.0.0.0:8000"]

