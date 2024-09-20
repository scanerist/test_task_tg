
FROM python:3.11-slim

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY bot/ /app/bot/
COPY main.py /app/main.py

WORKDIR /app


CMD ["python", "main.py"]
