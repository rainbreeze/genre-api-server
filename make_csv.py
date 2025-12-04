import pandas as pd
import numpy as np

# 원본 CSV 로드
df = pd.read_csv("./dataset/Hugging_CSV_processed.csv")

# 랜덤으로 30개 장르 선택
np.random.seed(42)
selected_genres = np.random.choice(df['Genre'].unique(), size=30, replace=False)

# 선택된 장르만 필터링
df_selected = df[df['Genre'].isin(selected_genres)].copy()

# 총 샘플 수
n_samples = 30000
n_per_genre = n_samples // len(selected_genres)  # 장르별 균등 샘플 수

samples = []

for genre in selected_genres:
    df_genre = df_selected[df_selected['Genre'] == genre]
    # 원본 데이터를 그대로, 균등 샘플링
    samples.append(df_genre.sample(n=n_per_genre, replace=True))

# 데이터 합치기
df_generated = pd.concat(samples).reset_index(drop=True)

# CSV 저장
df_generated.to_csv("generated_30000.csv", index=False)
print("generated_30000.csv 생성 완료")
