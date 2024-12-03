import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv('student_health_2.csv', encoding='cp949')

# Rename columns to English for simplicity
df.rename(columns={'학년': 'Grade', '키': 'Height', '몸무게': 'Weight', '수축기': 'SystolicBP', '이완기': 'DiastolicBP'}, inplace=True)

# 1) 학년당 학생 수 계산
students_per_grade = df['Grade'].value_counts().sort_index()

# 학년당 학생 수를 numpy 배열로 변환
students_per_grade_np = np.array(students_per_grade)

# Plot 1: 학년당 학생 수
plt.figure()
plt.bar(students_per_grade.index, students_per_grade_np)
plt.title('Number of Students per Grade')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2) 학년별 평균 계산 (키, 몸무게, 수축기, 이완기)
average_stats = df.groupby('Grade')[['Height', 'Weight', 'SystolicBP', 'DiastolicBP']].mean()

# 각 열의 평균값을 numpy 배열로 변환
average_stats_np = average_stats.to_numpy()

# Plot 2-5: 학년별 평균 (Height, Weight, SystolicBP, DiastolicBP)
columns = ['Height', 'Weight', 'SystolicBP', 'DiastolicBP']
for i, column in enumerate(columns):
    plt.figure()
    plt.bar(average_stats.index, average_stats_np[:, i])
    plt.title(f'Average {column} per Grade')
    plt.xlabel('Grade')
    plt.ylabel(f'Average {column}')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# 평균 출력 (numpy 배열로)
print("\nAverage stats per grade (as numpy array):")
print(average_stats_np)
