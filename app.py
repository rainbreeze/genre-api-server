from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import boto3
import joblib  # PyCaret 모델 로드용
import os
from dotenv import load_dotenv  # dotenv 추가

# .env 파일 로드
load_dotenv()

app = FastAPI()

# CORS 설정
origins = ["*"]  # 테스트용
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 환경변수에서 S3 정보 가져오기
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("BUCKET_NAME")
MODEL_KEY = os.getenv("MODEL_KEY")
LOCAL_MODEL_PATH = os.getenv("LOCAL_MODEL_PATH")

# S3에서 모델 다운로드
def download_model_from_s3():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )
    if not os.path.exists(LOCAL_MODEL_PATH):
        print("모델 다운로드 중...")
        s3.download_file(BUCKET_NAME, MODEL_KEY, LOCAL_MODEL_PATH)
        print("모델 다운로드 완료.")
    else:
        print("모델 이미 존재함, 다운로드 생략.")

# 모델 다운로드 및 로드
download_model_from_s3()
model = joblib.load(LOCAL_MODEL_PATH)  # PyCaret 모델 로드

# 입력 데이터 스키마 정의
class InputData(BaseModel):
    danceability: float
    energy: float
    loudness: float
    mode: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.post("/predict")
def predict(data: InputData):
    input_df = pd.DataFrame([data.dict()])
    
    # PyCaret 예측
    from pycaret.classification import predict_model
    prediction = predict_model(model, data=input_df)
    
    predicted_label = prediction["prediction_label"][0]  # 컬럼명 확인 필요
    return {"predicted_genre": predicted_label}