import pandas as pd

# 读取 CSV 文件
file_path = 'hd-data.csv'  # 替换为你的 CSV 文件路径
data = pd.read_csv(file_path)

# 定义需要排名的列
ranking_columns = ['one_month_return', 'three_month_return', 'six_month_return', 'one_year_return']

# 为每列添加排名
for col in ranking_columns:
    rank_col = f'{col}_rank'
    data[rank_col] = data[col].rank(ascending=False, method='min')

# 使用 apply 计算总和
data['total_rank_number'] = data[[f'{col}_rank' for col in ranking_columns]].apply(lambda row: row.sum(), axis=1)

# 将 total_rank_number 转换为整数
data['total_rank_number'] = data['total_rank_number'].astype(int)

# 打印 Fund Name, Fund Code 和 total_rank_number
print(data[['Fund Name', 'Fund Code', 'total_rank_number']])

# 打印 total_rank_number 列，仅显示数字
# for value in data['total_rank_number']:
#     print(value)