import numpy as np
import pandas as pd
from mid_1 import StatisticsCalculator  # StatisticsCalculator 클래스 가져오기

# 1) 정규 분포와 균등 분포 데이터 생성 및 오차 확인
tolerance = 0.001  # 오차 기준
sample_size = 1000  # 초기 샘플 크기

while True:
    # 데이터 생성
    normal_data = np.random.normal(0, 1, sample_size)
    uniform_data = np.random.uniform(-1, 1, sample_size)

    # StatisticsCalculator로 평균 및 표준편차 계산
    normal_calculator = StatisticsCalculator(normal_data)
    uniform_calculator = StatisticsCalculator(uniform_data)

    normal_mean = normal_calculator.calculate_mean()
    normal_std = normal_calculator.calculate_std_dev()
    uniform_mean = uniform_calculator.calculate_mean()
    uniform_std = uniform_calculator.calculate_std_dev()

    # 이론적 값과의 차이 (오차) 계산
    error_normal_mean = abs(0 - normal_mean)
    error_normal_std = abs(1 - normal_std)
    error_uniform_mean = abs(0 - uniform_mean)
    error_uniform_std = abs((2 / np.sqrt(12)) - uniform_std)  # 균등 분포의 이론적 표준편차: 2/sqrt(12)

    # 오차가 기준을 충족하면 루프 종료
    if (error_normal_mean < tolerance and error_normal_std < tolerance and
        error_uniform_mean < tolerance and error_uniform_std < tolerance):
        break

    # 샘플 크기를 증가
    sample_size += 1000

# 결과를 저장할 데이터프레임 생성 (오차 제외하고 평균과 표준편차만 저장)
results = {
    'Distribution': ['Normal', 'Uniform'],
    'Mean': [normal_mean, uniform_mean],
    'Std Dev': [normal_std, uniform_std]
}

# DataFrame 생성 및 CSV 파일로 저장
results_df = pd.DataFrame(results)
results_df.to_csv('stat_ms.csv', index=False)

# 2) CSV 파일에서 평균과 표준편차 값을 불러와 새로운 정규 분포 데이터 생성
stat_data = pd.read_csv('stat_ms.csv')
mu = stat_data.loc[0, 'Mean']  # Normal 분포의 평균
sigma = stat_data.loc[0, 'Std Dev']  # Normal 분포의 표준편차
new_normal_data = np.random.normal(mu, sigma, 1000)

# 3) 새롭게 생성된 데이터의 평균과 표준편차 계산
new_normal_calculator = StatisticsCalculator(new_normal_data)
new_normal_mean = new_normal_calculator.calculate_mean()
new_normal_std = new_normal_calculator.calculate_std_dev()

# 결과 출력
print(f"Generated Normal Distribution Mean: {new_normal_mean}, Std Dev: {new_normal_std}")
print(f"Sample Size Used for Convergence: {sample_size}")
