import pandas as pd

# 1. 원본 CSV 로드
df = pd.read_csv("./dataset/Hugging_CSV_processed.csv")

selected_genres = [
    "sleep", "idm", "study", "new-age", "guitar", "trip-hop", "chill", "iranian",
    "bluegrass", "psych-rock", "tango", "garage", "ambient", "anime", "disney",
    "afrobeat", "children", "black-metal", "romance", "grindcore", "british",
    "comedy", "cantopop", "piano", "happy", "honky-tonk", "rockabilly", "club",
    "breakbeat", "samba"
]



# 3. 선택된 장르만 필터링
df_selected = df[df['Genre'].isin(selected_genres)].copy()

# 4. 총 샘플 수와 장르별 균등 샘플 수 계산
n_samples = 30000
n_per_genre = n_samples // len(selected_genres)

# 5. 장르별 균등 샘플링
samples = []
empty_genres = []  # 비어있는 장르 저장
for genre in selected_genres:
    df_genre = df_selected[df_selected['Genre'] == genre]
    if len(df_genre) == 0:
        empty_genres.append(genre)
        continue
    samples.append(df_genre.sample(n=n_per_genre, replace=True))

# 6. 합치기 및 CSV 저장
df_generated = pd.concat(samples).reset_index(drop=True)
df_generated.to_csv("generated_30000.csv", index=False)

print("generated_30000.csv 생성 완료")

# 7. 비어있는 장르 출력
if empty_genres:
    print("다음 장르는 CSV에 데이터가 없어 샘플링하지 못했습니다:")
    for genre in empty_genres:
        print("-", genre)
