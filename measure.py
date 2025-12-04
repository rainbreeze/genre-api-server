import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
from collections import Counter

# 1. 모델 불러오기
model = load_model("genre_classifier")

# 2. 학습 데이터 불러오기 (컬럼별 min/max 확인용)
df_train = pd.read_csv("filtered_file.csv")

feature_cols = [
    "danceability", "energy", "loudness", "mode",
    "acousticness", "instrumentalness", "liveness", "valence", "tempo"
]

# 각 컬럼별 최소/최대값 계산
feature_stats = {}
for col in feature_cols:
    if col == "mode":  # mode는 0 또는 1
        feature_stats[col] = [0, 1]
    else:
        feature_stats[col] = [df_train[col].min(), df_train[col].max()]

# 3. 학습 데이터 분포 기반 랜덤 샘플 생성
n_samples = 1000
random_samples = []

for _ in range(n_samples):
    sample = {}
    for col in feature_cols:
        min_val, max_val = feature_stats[col]
        if col == "mode":
            sample[col] = np.random.choice([0, 1])
        else:
            sample[col] = np.random.uniform(min_val, max_val)
    random_samples.append(sample)

df_random = pd.DataFrame(random_samples)

# 4. 예측
preds = predict_model(model, data=df_random)

# 5. 장르별 분포 확인
genre_counts = Counter(preds["prediction_label"])
print("랜덤 데이터 기반 장르 분포:")
for genre, count in genre_counts.items():
    print(f"{genre}: {count}")
