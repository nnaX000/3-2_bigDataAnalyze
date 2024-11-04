import pandas as pd

# 데이터 불러오기
file_path = 'seoul_ems_test.csv'
data = pd.read_csv(file_path)

# 각 지역별로 2012~2017 합계와 Total 값 비교
for index, row in data.iterrows():
    sum_2012_2017 = row[['2012', '2013', '2014', '2015', '2016', '2017']].sum()
    total = row['Total']
    if sum_2012_2017 == total:
        print(f"Region {row['Region ID']}: True")
    else:
        gap = abs(sum_2012_2017 - total)
        print(f"Region {row['Region ID']}: False, Gap: {gap}")
