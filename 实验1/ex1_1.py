import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
nums = []
x = 10
y = 0.5
for i in range(1000):
    temp = random.gammavariate(x, y)
    nums.append(temp)
# plotting a graph
plt.hist(nums, bins=30)
plt.show()
nums = []
x = 10
y = 0.5
for i in range(1000):
    temp = random.betavariate(x, y)
    nums.append(temp)
# plotting a graph
plt.hist(nums, bins=30)
plt.show()
nums = []
x = 10
y = 0.5
for i in range(1000):
    temp = random.triangular(x, y)
    nums.append(temp)
# plotting a graph
plt.hist(nums, bins=30)
plt.show()
nums = []
x = 10
y = 0.5
for i in range(1000):
    temp = random.gammavariate(x, y)
    nums.append(temp)
# plotting a graph
plt.hist(nums, bins=30)
plt.show()
nums = []
x = 10
y = 0.5
for i in range(1000):
    temp = random.normalvariate(x, y)
    nums.append(temp)
# plotting a graph
plt.hist(nums, bins=30)
plt.show()