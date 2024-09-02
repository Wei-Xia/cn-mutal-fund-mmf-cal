import pandas as pd
import numpy as np

# 假设你已经将数据读入到一个pandas DataFrame中，名为df
df = pd.read_csv('data.csv')

# 去除百分号并将列转换为浮点数类型
df['one_year_rank'] = df['one_year_rank'].str.replace('%', '').astype(float)
df['six_month_rank'] = df['six_month_rank'].str.replace('%', '').astype(float)
df['three_month_rank'] = df['three_month_rank'].str.replace('%', '').astype(float)

# 将 "one_year_return"、"six_month_return" 和 "three_month_return" 按照从高到低的顺序进行排名
df['one_year_return_rank'] = df['one_year_return'].rank(ascending=False, method='first')
df['six_month_return_rank'] = df['six_month_return'].rank(ascending=False, method='first')
df['three_month_return_rank'] = df['three_month_return'].rank(ascending=False, method='first')

# 将 "one_year_rank"、"six_month_rank" 和 "three_month_rank" 按照从低到高的顺序进行排名
df['one_year_rank_rank'] = df['one_year_rank'].rank(ascending=True)
df['six_month_rank_rank'] = df['six_month_rank'].rank(ascending=True)
df['three_month_rank_rank'] = df['three_month_rank'].rank(ascending=True)

# 计算排名得分
df['rank_point'] = df['one_year_rank_rank'] + df['six_month_rank_rank'] + df['three_month_rank_rank'] + df['one_year_return_rank'] + df['six_month_return_rank'] + df['three_month_return_rank']

# sharpe_ratio 从高到低的顺序进行排名
df['sharpe_ratio_rank'] = df['sharpe_ratio'].rank(ascending=True, method='first')

# 设置权重
weights = {'收益得分': 0.9, '风险得分': 0.1}

# 计算综合得分
df['综合得分'] = df['rank_point'] * weights['收益得分'] + df['sharpe_ratio_rank'] * weights['风险得分']

# 根据综合得分进行排名
df['排名'] = df['综合得分'].rank(ascending=False)

# 输出排名结果
print(df[['Code', 'Name', '综合得分']].to_string(index=False))
# print(df[['综合得分']].to_string(index=False))

# print(df[['Name','sharpe_ratio_rank']].to_string(index=False))
