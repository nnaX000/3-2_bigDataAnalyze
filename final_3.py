import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'student_health_2.csv'
df = pd.read_csv(file_path, encoding='cp949')

df = df[['학교ID', '학년', '키']].dropna()
df.columns = ['School', 'Grade', 'Height']
df['Grade'] = df['Grade'].astype(int)  # 학년을 정수형으로 변환

pivot_table = df.pivot_table(index='Grade', columns='School', values='Height', aggfunc='mean')

plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Height Difference by Grade and School")
plt.show()

# 2. 학년별 평균 키 계산
grade_means = df.groupby('Grade')['Height'].mean()
print("Mean height of each grade:\n", grade_means)

# 학교별 키 데이터와 학년 평균 키의 상관계수 계산
correlation_results = {}
for school, group in df.groupby('School'):
    # 각 학교의 학년별 키 데이터와 전체 학년 평균 비교
    school_height_by_grade = group.groupby('Grade')['Height'].mean()
    aligned_means = grade_means.reindex(school_height_by_grade.index)
    correlation = school_height_by_grade.corr(aligned_means)
    correlation_results[school] = correlation

# 결과 출력
correlation_series = pd.Series(correlation_results)
highest_corr = correlation_series.max()

print("\nCorrelation Coefficients between each school and the array of mean:\n", correlation_series)
print("Highest Correlation Coefficient:", highest_corr)
