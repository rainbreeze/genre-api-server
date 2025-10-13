import pandas as pd
from pycaret.classification import *

# 1. CSV 파일 불러오기
df = pd.read_csv('./dataset/1001_CSV.csv')  # 실제 파일명으로 변경하세요

# 2. Genre 컬럼 결측값 제거
df = df.dropna(subset=['Genre'])

# 3. PyCaret 셋업
clf = setup(
    data=df,
    target='Genre',
    session_id=42,
    verbose=False
)

# 4. 모델 비교 후 최적 모델 선택 (gbc가 가장 좋았음)
best_model = compare_models()

# 5. 최적 모델 저장
save_model(best_model, 'best_model_gbc')

print("모델 학습 및 저장 완료!")
