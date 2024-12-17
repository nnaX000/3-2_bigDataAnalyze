import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 데이터 불러오기
file_path = 'subway_1.csv'
df = pd.read_csv(file_path, encoding='cp949')

# 데이터 준비
X = df[['승차총승객수', '하차총승객수']]  # 독립 변수
y = df['노선명']  # 종속 변수 (분류 대상)

# 훈련 데이터와 테스트 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# RandomForestClassifier 모델 학습
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 예측 및 평가
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# 입력값에 대한 예측 (수정된 입력값)
input_data = pd.DataFrame({
    '승차총승객수': [1000, 6000],  # 각각 다른 값
    '하차총승객수': [5000, 20000]  # 각각 다른 값
})

predictions = model.predict(input_data)

# 예측 결과 출력
for i, pred in enumerate(predictions):
    print(f"Input {input_data.iloc[i].values} => Predicted Line: {pred}")
