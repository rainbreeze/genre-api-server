import pandas as pd
from pycaret.classification import *

# 1. CSV 파일 불러오기
df = pd.read_csv('./dataset/1001_CSV.csv')

# 2. Genre 컬럼의 결측값 있는 행 제거
df = df.dropna(subset=['Genre'])

# 3. PyCaret 셋업
clf = setup(
    data=df,
    target='Genre',
    session_id=42,
    verbose=False
)

# 4. 모델 비교
best_model = compare_models()

# 5. 결과 보기
results = pull()
print(results)