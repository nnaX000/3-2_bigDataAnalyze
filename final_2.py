import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 데이터 불러오기
file_path = 'hw_25000.csv'
df = pd.read_csv(file_path)

# 컬럼 이름 정리
df.columns = df.columns.str.strip().str.replace('"', '').str.replace(' ', '')

# 키와 몸무게 데이터 추출
height = df['Height(Inches)']
weight = df['Weight(Pounds)']

# 1번: 히스토그램 및 확률 밀도 함수 그리기
def plot_hist_with_pdf(data, title, subplot_position):
    df_min, df_max = data.min(), data.max()  # 최소값과 최대값
    df_mean, df_std = data.mean(), data.std()  # 평균과 표준편차
    df_lins = np.linspace(df_min, df_max, 100)
    df_norm = stats.norm.pdf(df_lins, df_mean, df_std)

    plt.subplot(1, 2, subplot_position)
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Histogram')
    plt.plot(df_lins, df_norm, color='red', linewidth=2, label='PDF')
    plt.title(title)
    plt.legend()

plt.figure(figsize=(12, 6))
plot_hist_with_pdf(height, "Height Distribution with PDF", 1)
plot_hist_with_pdf(weight, "Weight Distribution with PDF", 2)
plt.tight_layout()
plt.show()

# 2번: 평균, 분산 계산 및 정규분포 값 생성
height_mean, height_var = height.mean(), height.var()
weight_mean, weight_var = weight.mean(), weight.var()

# 평균과 분산을 사용해 정규분포에서 100개 값 생성
height_generated = np.random.normal(height_mean, np.sqrt(height_var), 100)
weight_generated = np.random.normal(weight_mean, np.sqrt(weight_var), 100)

# 결과 CSV 파일 저장
output_df = pd.DataFrame({
    'Generated_Height': height_generated,
    'Generated_Weight': weight_generated
})
output_df.to_csv('resultprob2.csv', index=False)

print("Mean and Variance of Height: ", height_mean, height_var)
print("Mean and Variance of Weight: ", weight_mean, weight_var)
print("Generated file saved as 'resultprob2.csv'")
