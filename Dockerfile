# 1. Python 3.11 슬림 버전 이미지 사용
FROM python:3.11-slim

# 2. 필요한 시스템 패키지 설치
RUN apt-get update && \
    apt-get install -y gcc libpq-dev libsqlite3-0 libsqlite3-dev && \
    apt-get clean

# 3. 작업 디렉토리 설정
WORKDIR /app

# 4. requirements.txt 복사하고 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 나머지 코드 파일들 복사
COPY . .

# 6. FastAPI 앱 실행 명령어
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
