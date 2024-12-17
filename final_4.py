import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress
import numpy as np

# 데이터 불러오기
file_path = 'London.csv'
df = pd.read_csv(file_path)

# 총 방 개수(Total Rooms) 계산
df['Total Rooms'] = df['No. of Bedrooms'] + df['No. of Bathrooms']

# 1. House Type 별로 Price와 Area in sq ft의 선형 회귀선 및 허용 구간 플롯
house_types = df['House Type'].unique()

for house_type in house_types:
    subset = df[df['House Type'] == house_type]
    
    # 선형 회귀 계산
    slope, intercept, r_value, _, _ = linregress(subset['Area in sq ft'], subset['Price'])
    line = slope * subset['Area in sq ft'] + intercept
    
    # 허용 구간 계산 (신뢰 구간)
    x = subset['Area in sq ft']
    y_pred = slope * x + intercept
    y_std = np.std(subset['Price'] - y_pred)  # 잔차의 표준편차
    confidence_interval = 1.96 * y_std  # 95% 허용 구간
    
    # 플롯 그리기
    plt.figure(figsize=(8, 6))
    plt.scatter(x, subset['Price'], color='blue', alpha=0.5, label='Data Points')
    plt.plot(x, y_pred, color='red', label='Regression Line')
    plt.fill_between(x, y_pred - confidence_interval, y_pred + confidence_interval,
                     color='red', alpha=0.2, label='Tolerance Interval')
    
    plt.xlabel('Area (sq ft)')
    plt.ylabel('Price (£)')
    plt.title(f'Price vs Area for {house_type}')
    plt.legend()
    plt.show()

# 2. House Type 별 평균값 계산 및 출력
averages = df.groupby('House Type').agg({
    'Price': 'mean',
    'Area in sq ft': 'mean',
    'Total Rooms': 'mean'
})

print("Averages per House Type:")
print(averages)
print("\nGuide:")
print(" - Price: Average housing price")
print(" - Area in sq ft: Average area")
print(" - Total Rooms: Average total number of rooms (Bedrooms + Bathrooms)")
