import pandas as pd
import numpy as np

# 读取 CSV 文件
file_path = 'hd-data.csv'  # 替换为你的 CSV 文件路径
data = pd.read_csv(file_path)

# 定义需要排名的列
ranking_columns = ['one_month_return', 'three_month_return', 'six_month_return', 'one_year_return']

for col in ranking_columns:
    rank_col = f'{col}_rank'
    
    # 给每个值加上一点随机数，这里乘以 1e-9 保证只在小数点后极小扰动，不影响原本排序层级
    # method='first' 会根据数据出现顺序进行排名；加上随机噪声后，相同值就不会再完全相同，从而打破并列
    data[rank_col] = (
        data[col] 
        + np.random.rand(len(data)) * 1e-9
    ).rank(ascending=False, method='first')

# 使用 apply 计算总和
data['total_rank_number'] = data[[f'{col}_rank' for col in ranking_columns]].apply(lambda row: row.sum(), axis=1)

# 将 total_rank_number 转换为整数
data['total_rank_number'] = data['total_rank_number'].astype(int)

# 打印 Fund Name, Fund Code 和 total_rank_number
# print(data[['Fund Name', 'Fund Code', 'total_rank_number']])

# 打印 total_rank_number 列，仅显示数字
for value in data['total_rank_number']:
    print(value)