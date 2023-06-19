import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats
data = pd.read_excel('学生17门课程成绩.xls')
list1=data["期末成绩"].tolist()
list2=data["总评成绩"].tolist()
dict_score1={}
dict_score2={}
def print_statis(list_arg,dict_score):
    for i in list_arg:
        if i < 60:
            dict_score["0-60 (不及格)"] = dict_score.get("0-60 (不及格)",0) + 1
        elif i<=69:
            dict_score["60-69 (及格)"] = dict_score.get("60-69 (及格)",0) + 1
        elif i <=79:
            dict_score["70-80 (中等)"] = dict_score.get("70-80 (中等)",0) + 1
        elif i<= 89:
            dict_score["80-90 (良好)"] = dict_score.get("80-90 (良好)",0) + 1
        else :
            dict_score["90-100 (优秀)"] = dict_score.get("90-100 (优秀)",0) + 1
    for i in sorted (dict_score) : 
        print (i+"人数:", dict_score[i])
    print("最高分:",np.max(list_arg))
    print("最低分:",np.min(list_arg))
    print("平均分:",round(np.mean(list_arg),2))
    print("标准差:",round(np.std(list_arg),2))
#输出成绩分析
print("*"*18+"卷面成绩分析"+"*"*18)
print_statis(list1,dict_score1)
print("*"*18+"总评成绩分析"+"*"*18)
print_statis(list2,dict_score2)
#将字典中各个分数段的人数存为列表，以便于画图
keys1=[]
keys2=[]
values1=[]
values2=[]
for i in sorted (dict_score1) :
    keys1.append(i)
    values1.append(dict_score1[i])
for i in sorted (dict_score2) :
    keys2.append(i)
    values2.append(dict_score2[i])
#画折线图
plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
fig=plt.figure(figsize=(8,5)) #新建画布
plt.plot(keys1, values1,c='r', mec='r', mfc='w',label=u'y=x^2曲线图')
plt.plot(keys1, values2, c='g', ms=10,label=u'y=x^3曲线图')
for a, b in zip(keys1, values1):
    plt.text(a, b, b, ha="center", va='bottom', fontsize=15)  # 设置数据标签位置及大小
for a, b in zip(keys1, values2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
plt.legend(['期末成绩', '总评成绩',])  # 设置折线名称
plt.title("总评及卷面成绩分布图") #标题
plt.show()
#总评成绩QQ图
#Q-Q散点图是沿着y=x分布时, 符合标准正态分布
#Q-Q散点图沿y=ax+b分布时, 符合正态分布, 但非标准正态分布
data_qq=np.array(list2)
#create Q-Q plot with 45-degree line added to plot
fig = sm.qqplot(data_qq, line='s')
plt.title("总评成绩qq图") #标题
plt.show()
#总评成绩偏度，峰度
s = pd.Series(list2)
#直接调用库文件计算
print("*"*18+"偏度,峰度"+"*"*18)
print("总评成绩偏度",s.skew())#偏度
print("总评成绩峰度",s.kurt())#峰度
#总评成绩 ks检验
#pvalue值大于0.05就属于正太分布
#kstest参数 数组，字符串，（均值，标准差）
print("*"*18+"总评成绩 k-s检验"+"*"*18)
print("注释：pvalue值大于0.05就属于正态分布")
print(stats.kstest(list2,"norm",(np.mean(list2),np.std(list2))))
#带正态曲线的直方图
score = data['总评成绩']
mean = score.mean()
std = score.std()
fig=plt.figure(figsize=(8,5)) 
#normfun正态分布函数，mu: 均值，sigma:标准差，pdf:概率密度函数，np.exp():概率密度函数公式
def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
# x的范围为60-150，以1为单位,需x根据范围调试
x = np.arange(0, 150,1)
# x数对应的概率密度
y = normfun(x, mean, std)
# 参数,颜色，线宽
plt.plot(x,y, color='r',linewidth = 3)
#数据，数组，颜色，颜色深浅，组宽，显示频率
plt.hist(score, bins =7, color = 'b',alpha=0.8,rwidth= 0.9, density=True)
plt.title('总评成绩分布')
plt.xlabel('成绩分数')
plt.ylabel('Probability')
plt.show()