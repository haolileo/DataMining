# coding:utf-8
from unittest import result
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import matplotlib.animation as animation
#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

import pygame
url = 'Sasha Alex Sloan - Dancing With Your Ghost.mp3'
pygame.mixer.init()
m = pygame.mixer.music.load(url)
pygame.mixer.music.play()

#导出数据
df = pd.read_csv('学生33门课程成绩.csv',usecols=['课程名称', '姓名', '班级', '分数'], encoding='gbk')
print(df.info)
#定义
dff=()

fig, ax = plt.subplots(figsize=(15, 8))

group_lk = df.set_index('姓名')['班级'].to_dict()

def draw_barchart(course):
    dff = df[df['课程名称'].eq(course)].sort_values(by='分数', ascending=True).tail(10)
    print(dff)
    # 每次不清空、刷新
    ax.clear() #每次清空、刷新
    ax.barh(dff['姓名'], dff['分数'], color=['#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50', '#70DBDB', '#00FF7F', '#A67D3D', '#93DB70'])
    dx = dff['分数'].max() / 200
    for i, (value, name) in enumerate(zip(dff['分数'], dff['姓名'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
    #显示文字，x=0，y=1.10，坐标，ha=水平对准=水平线平放
    #ax.text()格式=(x,y,string,fontsize=15,verticalalignment="top",horizontalalignment="right")
    #string=字符串='文字内容'
    ax.text(0, 1.10, course+'课程成绩最高的学生',
            transform=ax.transAxes, size=18, weight=600, ha='left') #文字标题，第1层
    ax.text(0, 1.04, '分数', transform=ax.transAxes, size=18, color='#777777') #显示文字，第2层
    ax.text(1, -0.1, course, transform=ax.transAxes, color='#777777', size=46, weight=800)



courses = ['动态网站构建技术', '大学生心理健康教育', '离散数学', '数据结构', '概率统计', '数据分析与处理', '数学分析(二)', '高等代数(二)', '数据库课程设计', '常微分方程', '形势与政策(二)', '形势与政策（四）', '大学物理Ⅰ（上）', '就业指导', '软件测试技术', '软件开发综合实训', '大学英语（二）', '毛泽东思想和中国特色社会主义理论体系概论(二)', '数据挖掘技术', '形势与政策（六）', '数据库高级编程技术', '计算机图形学', '智能精准开采概论', '移动计算软件开发', '互联网+应用开发', '沟通与写作', '数据库课程设计', '马克思主义基本原理', '大学物理实验（上）', 'C语言程序设计']
animator = animation.FuncAnimation(fig, draw_barchart, frames=courses, interval=300) #以animator形式展现动画
plt.show() #以plt的形式展现图片
