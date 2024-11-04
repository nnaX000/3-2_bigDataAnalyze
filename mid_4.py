import numpy as np
import pandas as pd

# 데이터 리스트
data = [
    955, 890, 519, 707, 634, 689, 177, 404, 375, 458, 607, 704, 219, 804, 983, 
    848, 808, 766, 868, 981, 803, 149, 237, 778, 671, 555, 693, 429, 486, 602, 
    160, 808, 382, 852, 16, 169, 4, 300, 73, 907, 199, 548, 867, 568, 242, 737, 
    312, 225, 170, 975, 539, 665, 631, 286, 78, 216, 84, 127, 19, 133, 970, 296, 
    622, 874, 949, 809, 616, 379, 451, 498, 420, 442, 461, 183, 760, 766, 958, 
    822, 2, 891, 987, 138, 231, 53, 382, 456, 694, 791, 14, 284, 861, 349, 761, 
    478, 604, 491, 582, 473, 321, 29, 706, 525, 221, 498, 684, 241, 602, 695, 
    51, 266, 342
]

# NumPy 계산
np_mean = np.mean(data)
np_var = np.var(data)
np_std = np.std(data)
np_median = np.median(data)
np_20th_percentile = np.percentile(data, 20)
np_80th_percentile = np.percentile(data, 80)

# Pandas 계산
df = pd.Series(data)
pd_mean = df.mean()
pd_var = df.var()
pd_std = df.std()
pd_median = df.median()
pd_20th_percentile = df.quantile(0.20)
pd_80th_percentile = df.quantile(0.80)

# 차이 계산
diff_mean = abs(np_mean - pd_mean)
diff_var = abs(np_var - pd_var)
diff_std = abs(np_std - pd_std)
diff_median = abs(np_median - pd_median)
diff_20th_percentile = abs(np_20th_percentile - pd_20th_percentile)
diff_80th_percentile = abs(np_80th_percentile - pd_80th_percentile)

# 결과 출력
print(f"NumPy Mean: {np_mean}, Pandas Mean: {pd_mean}, Difference: {diff_mean}")
print(f"NumPy Variance: {np_var}, Pandas Variance: {pd_var}, Difference: {diff_var}")
print(f"NumPy Std Dev: {np_std}, Pandas Std Dev: {pd_std}, Difference: {diff_std}")
print(f"NumPy Median: {np_median}, Pandas Median: {pd_median}, Difference: {diff_median}")
print(f"NumPy 20th Percentile: {np_20th_percentile}, Pandas 20th Percentile: {pd_20th_percentile}, Difference: {diff_20th_percentile}")
print(f"NumPy 80th Percentile: {np_80th_percentile}, Pandas 80th Percentile: {pd_80th_percentile}, Difference: {diff_80th_percentile}")
