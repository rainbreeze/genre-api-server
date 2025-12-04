from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import os

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

# 로컬 모델 경로
LOCAL_MODEL_PATH = "genre_classifier.pkl"

# 모델 로드
model = joblib.load(LOCAL_MODEL_PATH)

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
