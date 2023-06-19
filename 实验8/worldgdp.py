'''import glob
from unittest import result'''
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import matplotlib.animation as animation
#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def gdpvalue(x):
    if '万亿' in x:
        x = float(x.replace('万亿', '')) * 10000
    elif '亿' in x:
        x = float(x.replace('亿', ''))
    elif '万' in x:
        x = float(x.replace('万', '')) / 10000
    return x

#导出数据
df = pd.read_csv('GDP.csv',usecols=['年数', '国家/地区', '所在洲', 'GDP(美元/亿)'])
df['GDP(美元/亿)'] = df['GDP(美元/亿)'].apply(lambda x : gdpvalue(x))
print(df.info)

#定义
current_year = 2021
dff=()

fig, ax = plt.subplots(figsize=(15, 8))

colors = dict(zip(
    ['美国', '中国', '日本', '英国', '德国', '法国', '加拿大', '西班牙', '墨西哥', '韩国', '印度', '巴西', '意大利', '俄罗斯'],
    ['#adb0ff', '#FF0000', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50', '#70DBDB', '#00FF7F', '#A67D3D', '#93DB70', '#23238E', '#DB7093']
))
group_lk = df.set_index('国家/地区')['所在洲'].to_dict()

def draw_barchart(year):
    dff = df[df['年数'].eq(year)].sort_values(by='GDP(美元/亿)', ascending=True).tail(10)
    print(dff)
    ax.clear() #每次清空、刷新
    ax.barh(dff['国家/地区'], dff['GDP(美元/亿)'], color=[colors[x] for x in dff['国家/地区']])
    dx = dff['GDP(美元/亿)'].max() / 200
    for i, (value, name) in enumerate(zip(dff['GDP(美元/亿)'], dff['国家/地区'])):
        ax.text(value-dx, i,     name,           size=14, weight=600, ha='right', va='bottom')
        ax.text(value-dx, i-.25, group_lk[name], size=10, color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,     f'{value:,.0f}',  size=14, ha='left',  va='center')
    #显示文字，x=0，y=1.10，坐标，ha=水平对准=水平线平放
    #ax.text()格式=(x,y,string,fontsize=15,verticalalignment="top",horizontalalignment="right")
    #string=字符串='文字内容'
    ax.text(0, 1.10, '1968年至2020年间全球 GDP 最高的国家',
            transform=ax.transAxes, size=18, weight=600, ha='left') #文字标题，第1层
    ax.text(0, 1.04, 'GDP(美元/亿)', transform=ax.transAxes, size=12, color='#777777') #显示文字，第2层
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800) #右边固定显示动图年份
    #va=verticalalignment="top",垂直对准
    #ha=horizontalalignment="right"，alignment=对准，水平对准
    ax.xaxis.set_ticks_position('top')  #x轴在上面

    ax.set_yticks([]) #默认是显示y轴的名称，左边垂直的城市名字，设为[]就是不显示
    ax.margins(0, 0.01) #不设置就是默认值,缩放比例（0,0.05）
    ax.grid(which='major', axis='x', linestyle='--') #垂直线，布局和格式
    ax.set_axisbelow(True)  #默认是true的

    plt.box(False) #默认是True，False之后不显示黑色线框
    
animator = animation.FuncAnimation(fig, draw_barchart, frames=range(2001, 2021), interval=500) #以animator形式展现动画
plt.show() #以plt的形式展现图片