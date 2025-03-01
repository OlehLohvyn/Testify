FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get update && apt-get install -y procps net-tools


COPY . /app/

CMD ["python", "/app/users_project/manage.py", "runserver", "0.0.0.0:8000"]
