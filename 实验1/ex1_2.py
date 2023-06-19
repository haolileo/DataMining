import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import pyplot
import seaborn
data = pd.read_csv("iris.csv")
data.describe()
print (data.head(10))
data.info()
data["SepalLengthCm"].describe()
fig, ax = pyplot.subplots(figsize =(9, 7))
sns.violinplot(ax = ax, y = data["SepalLengthCm"])
fig, ax = pyplot.subplots(figsize =(9, 7))
sns.violinplot(ax = ax,  y = data["SepalWidthCm"])
fig, ax = pyplot.subplots(figsize =(9, 7))
sns.violinplot(ax = ax, data = data.iloc[:, 1:3])
fig, ax = pyplot.subplots(figsize =(9, 7))
sns.violinplot(ax = ax, x = data["Species"],y = data["SepalLengthCm"])
plt.show()