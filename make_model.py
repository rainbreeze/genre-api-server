# 필요한 라이브러리
import pandas as pd
import numpy as np
from pycaret.classification import setup, compare_models, finalize_model, save_model, predict_model
from collections import Counter

# 1. 데이터 로드
df = pd.read_csv("generated_30000.csv")  # 파일명 변경 필요

# 2. PyCaret setup (기본 전처리 + 클래스 불균형 처리)
clf_setup = setup(
    data=df,
    target='Genre',
    session_id=42,
    normalize=True,
    transformation=True,
    remove_multicollinearity=True,
    multicollinearity_threshold=0.95,
    fix_imbalance=True  # 클래스 불균형 보정
)

# 3. 모델 비교
best_model = compare_models(sort='Accuracy')

# 4. 모델 최종화
final_model = finalize_model(best_model)

# 5. 모델 저장
save_model(final_model, "genre_classifier")
print("모델 학습 완료! 'genre_classifier.pkl'로 저장됨")