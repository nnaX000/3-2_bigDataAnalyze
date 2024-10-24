import numpy as np
import pandas as pd

# 1. 100,000개의 데이터를 각각의 분포에서 생성
np.random.seed(42)  # 재현성을 위한 시드 고정

# 정규 분포 (평균=0, 표준편차=1)
normal_values = np.random.normal(0, 1, 100000)

# 카이제곱 분포: x^2 (정규 분포로부터 변환, 자유도 1)
chi_square_values = np.random.normal(0, 1, 100000) ** 2

# 균등 분포 (0과 1 사이의 값)
uniform_values = np.random.uniform(0, 1, 100000)

# test.csv로 저장
df = pd.DataFrame({
    'Normal Distribution': normal_values,
    'Chi-square Distribution': chi_square_values,
    'Uniform Distribution': uniform_values
})
df.to_csv('test.csv', index=False)

# 2. 샘플 크기별 통계 결과를 계산하고 저장 (10000, 20000, 30000, 50000, 100000)
sample_sizes = [10000, 20000, 30000, 50000, 100000]
stats_data = []

# 통계 계산 함수 (numpy로 계산)
def calculate_stats_numpy(sample, sample_size, dist_name):
    stats = {
        'Sample Size': sample_size,
        'Distribution': dist_name,
        'Mean': np.mean(sample),
        'Standard Deviation': np.std(sample),
        'Variance': np.var(sample),
        'Max': np.max(sample),
        'Min': np.min(sample),
        '10th Percentile': np.percentile(sample, 10),
        '20th Percentile': np.percentile(sample, 20),
        '40th Percentile': np.percentile(sample, 40),
        '80th Percentile': np.percentile(sample, 80),
        '90th Percentile': np.percentile(sample, 90),
    }
    return stats

# 통계 계산 함수 (pandas로 계산)
def calculate_stats_pandas(sample, sample_size, dist_name):
    sample_series = pd.Series(sample)
    stats = {
        'Sample Size': sample_size,
        'Distribution': dist_name,
        'Mean': sample_series.mean(),
        'Standard Deviation': sample_series.std(),
        'Variance': sample_series.var(),
        'Max': sample_series.max(),
        'Min': sample_series.min(),
        '10th Percentile': sample_series.quantile(0.10),
        '20th Percentile': sample_series.quantile(0.20),
        '40th Percentile': sample_series.quantile(0.40),
        '80th Percentile': sample_series.quantile(0.80),
        '90th Percentile': sample_series.quantile(0.90),
    }
    return stats

# 번갈아 가며 numpy와 pandas로 계산
for size in sample_sizes:
    stats_data.append(calculate_stats_numpy(normal_values[:size], size, 'Normal Distribution'))
    stats_data.append(calculate_stats_pandas(chi_square_values[:size], size, 'Chi-square Distribution'))
    stats_data.append(calculate_stats_numpy(uniform_values[:size], size, 'Uniform Distribution'))
    
    stats_data.append(calculate_stats_pandas(normal_values[:size], size, 'Normal Distribution'))
    stats_data.append(calculate_stats_numpy(chi_square_values[:size], size, 'Chi-square Distribution'))
    stats_data.append(calculate_stats_pandas(uniform_values[:size], size, 'Uniform Distribution'))

# DataFrame으로 변환 후 result.csv로 저장
result_df = pd.DataFrame(stats_data)
result_df.to_csv('result.csv', index=False)

print("CSV 파일들이 생성되었습니다: test.csv, result.csv")
