import pandas as pd
import numpy as np

# 1. 원본 CSV 로드
df = pd.read_csv("./dataset/Hugging_CSV_processed.csv")

# 2. 선택할 30개 장르 지정
selected_genres = [
    "guitar", "trip-hop", "ambient", "breakbeat", "comedy", "british", "hard-rock",
    "disney", "tango", "kids", "show-tunes", "anime", "afrobeat", "garage", "chicago-house",
    "grindcore", "happy", "club", "rock", "french", "latin", "death-metal", "turkish",
    "pop-film", "progressive-house", "electro", "malay", "soul", "acoustic", "forro"
]

# 3. 선택된 장르만 필터링
df_selected = df[df['Genre'].isin(selected_genres)].copy()

# 4. 총 샘플 수와 장르별 균등 샘플 수 계산
n_samples = 30000
n_per_genre = n_samples // len(selected_genres)

# 5. 장르별 균등 샘플링
samples = []
for genre in selected_genres:
    df_genre = df_selected[df_selected['Genre'] == genre]
    samples.append(df_genre.sample(n=n_per_genre, replace=True))

# 6. 합치기 및 CSV 저장
df_generated = pd.concat(samples).reset_index(drop=True)
df_generated.to_csv("generated_30000.csv", index=False)

print("generated_30000.csv 생성 완료")
