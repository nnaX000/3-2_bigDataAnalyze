import pandas as pd

# CSV 파일 읽기
filename = 'attraction_list_1.csv'
try:
    df = pd.read_csv(filename, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(filename, encoding='cp949')

# 결측값을 0으로 채우기
df.fillna(0, inplace=True)

# "합계"가 포함된 행 제거
df = df[~df['자치구별'].str.contains("합계", na=False)]

# 사용자 정의 클래스 생성
class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        total_sum = 0
        count = 0
        for value in self.data:
            total_sum += value
            count += 1
        return total_sum / count if count != 0 else 0

    def calculate_std_dev(self):
        mean = self.calculate_mean()
        total_sum = 0
        count = 0
        for value in self.data:
            total_sum += (value - mean) ** 2
            count += 1
        variance = total_sum / count if count != 0 else 0
        return variance ** 0.5

# 결과를 저장할 리스트
result = []

# 구별로 "유료관광지", "내국인", "외국인"에 대한 평균 계산
for gu in df['자치구별'].unique():
    gu_data = df[df['자치구별'] == gu]
    for category in ["유료관광지", "내국인", "외국인"]:
        category_data = gu_data[gu_data['관광지별'] == category].iloc[:, 2:]  # 연도별 데이터만 선택
        if not category_data.empty and category_data.values.sum() > 0:  # 데이터가 비어있거나 전부 0인 경우 제외
            # 각 열의 값을 리스트로 변환하여 평균 계산
            data_values = category_data.values.flatten()
            calculator = StatisticsCalculator(data_values)
            mean = calculator.calculate_mean()
            result.append([gu, category, mean])

# 결과를 DataFrame으로 변환 및 CSV 파일로 저장 (표준편차 제외)
result_df = pd.DataFrame(result, columns=['자치구별', '관광지별', '평균'])
result_df.to_csv('sightsee.csv', index=False, encoding='cp949')
