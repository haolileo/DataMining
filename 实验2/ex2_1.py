import numpy as np
import pandas as pd
import math
data=pd.read_csv("normalization_data.csv",header=None)
print(data)
# min-max标准化
arr1=np.zeros((7,4))
for j in range(0,4):
    for i in range(0,7):
        x=data[j][i]
        Min=np.min(data[j])
        Max=np.max(data[j])
        arr1[i][j]=(x-Min)/(Max-Min)
print("min-max标准化:")
print(arr1)
# z_score标准化
arr2=np.zeros((7,4))
for j in range(0,4):
    for i in range(0,7):
        x=data[j][i]
        mean=np.mean(data[j])
        std=np.std(data[j])
        arr2[i][j]=(x-mean)/std
print("z_score标准化:")
print(arr2)
# sigmod标准化
arr3=np.zeros((7,4))
for j in range(0,4):
    for i in range(0,7):
        x=data[j][i]
        arr3[i][j]=1.0/(1+np.exp(-float(x)))
print("sigmod标准化:")
print(arr3)