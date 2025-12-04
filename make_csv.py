import pandas as pd
import numpy as np

# 원본 CSV 로드
df = pd.read_csv("./dataset/Hugging_CSV_processed.csv")

# 🔥 랜덤 30개 장르 선택 (매번 다른 결과)
selected_genres = df['Genre'].drop_duplicates().sample(n=30, replace=False).values

# 선택된 장르만 필터링
df_selected = df[df['Genre'].isin(selected_genres)].copy()

# 총 샘플 수
n_samples = 30000
n_per_genre = n_samples // len(selected_genres)

samples = []

for genre in selected_genres:
    df_genre = df_selected[df_selected['Genre'] == genre]
    samples.append(df_genre.sample(n=n_per_genre, replace=True))

df_generated = pd.concat(samples).reset_index(drop=True)

# CSV 저장
df_generated.to_csv("generated_30000.csv", index=False)
print("generated_30000.csv 생성 완료")
