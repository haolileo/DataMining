import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
plt.rcParams['font.sans-serif'] = ['SimHei']
# 导入数据
df_final = pd.read_csv("../iris.csv")
# 绘制平行坐标图
plt.figure(figsize=(8,6), dpi= 80)
parallel_coordinates(df_final, 'Species', colormap='Dark2')
# 设置边框
plt.gca().spines["top"].set_alpha(0)
plt.gca().spines["bottom"].set_alpha(.3)
plt.gca().spines["right"].set_alpha(0)
plt.gca().spines["left"].set_alpha(.3)
# 设置标签
plt.title('鸢尾花平行坐标图', fontsize=22)
plt.grid(alpha=0.3)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()