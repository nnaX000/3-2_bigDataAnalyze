import pandas as pd
import numpy as np

# 데이터 불러오기
data = pd.read_csv("kbo_baseball_test.csv")

# 승률 계산 및 정렬
data['Rating'] = data['Win'] / data['Game']
b = data.sort_values(by='Rating', ascending=False).reset_index(drop=True)

# 상위 5개 팀 출력
print("Top 5 of Winning Percentage")
for i in range(0,5):
    print("{},{}".format(b["Team"][i], b["Rating"][i]))
