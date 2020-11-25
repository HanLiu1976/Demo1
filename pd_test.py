import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
from pyecharts.charts import Bar
import pandas as pd
import numpy as np
name_list = ["Monday","Tuesday", "Friday", "unday"]
num_list = [1.5, 0.6, 7.8, 6]
num_list1 = [1, 2, 3, 1]
plt.bar(range(len(num_list)), num_list, label="boy", fc ="y")
plt.bar(range(len(num_list)), num_list1, bottom=num_list, label="girl", tick_label = name_list, fc ="r")
plt.legend()
plt.show()

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar(stacked=True)
plt.show()

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
waters = ('碳酸饮料', '绿茶', '矿泉水', '果汁', '其他')
buy_number_male = [6, 7, 6, 1, 2]
buy_number_female = [9, 4, 4, 5, 6]

bar_width = 0.3  # 条形宽度
index_male = np.arange(len(waters))  # 男生条形图的横坐标
index_female = index_male + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=buy_number_male, width=bar_width, color='b', label='男性')
plt.bar(index_female, height=buy_number_female, width=bar_width, color='g', label='女性')

plt.legend()  # 显示图例
plt.xticks(index_male + bar_width/2, waters)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('购买量')  # 纵坐标轴标题
plt.title('购买饮用水情况的调查结果')  # 图形标题

plt.show()

plt.figure()
plt.subplot(2,2,1)
plt.bar(index_male, height=buy_number_male, width=bar_width, color='b', label='男性')

plt.show() # 展示
