FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y gcc libpq-dev libsqlite3-0 libsqlite3-dev && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 환경변수 PORT가 주어질 때만 사용되도록 CMD 수정
CMD uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}
