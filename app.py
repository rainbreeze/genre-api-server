from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from pycaret.classification import load_model, predict_model

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

model = load_model("best_model_gbc")


# 입력 데이터 스키마 정의 (장르 제외한 9개 특성)
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


@app.post("/predict")
def predict(data: InputData):
    # Pydantic 모델을 DataFrame으로 변환
    input_df = pd.DataFrame([data.dict()])

    # PyCaret 모델로 예측 수행
    prediction = predict_model(model, data=input_df)

    # 예측 결과 로그 출력
    print("예측 결과:")
    print(prediction)

    # 예측 결과에서 가장 마지막 열을 예측 장르로 추출
    predicted_label = prediction["prediction_label"][0]  # 컬럼명 맞춰서 수정
    
    return {"predicted_genre": predicted_label}

