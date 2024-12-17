import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# 1. 데이터 로드 및 전처리
file_path = 'student_health_3.csv'
data = pd.read_csv(file_path, encoding='cp949')

# 필요한 열 추출 및 결측치 제거
data_cleaned = data[['수축기', '이완기', '키', '몸무게', '학년']].dropna()

# 학년(Class 1: Grade 1~3, Class 2: Grade 4~6)으로 변환
data_cleaned['학년'] = data_cleaned['학년'].apply(lambda x: 1 if x <= 3 else 2)

# 2. 특징(features)와 타겟(target) 설정
X = data_cleaned[['수축기', '이완기', '키', '몸무게']]
y = data_cleaned['학년']

# 3. 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. 데이터 표준화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. k-NN 모델 학습
knn = KNeighborsClassifier(n_neighbors=3)  # k 값은 3으로 설정
knn.fit(X_train_scaled, y_train)

# 6. 모델 평가
y_pred = knn.predict(X_test_scaled)
print("분류 성능 보고서:")
print(classification_report(y_test, y_pred))

# 7. 주어진 입력값에 대한 예측
input_data = [[80, 100, 140, 60]]  # [혈압 Lower, 혈압 Upper, 키, 몸무게]
input_data_scaled = scaler.transform(input_data)
predicted_class = knn.predict(input_data_scaled)

print(f"주어진 입력값 {input_data}에 대한 예측 클래스: Class {predicted_class[0]}")
