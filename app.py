from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 허용할 출처 목록 (예: 로컬호스트, 특정 도메인)
origins = [
    "*",  # 테스트용으로 모든 도메인 허용 (실서비스 시엔 제한 권장)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
def say_hello():
    return {"message": "hello"}
