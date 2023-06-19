#philchen CART_regression

import numpy as np

"""
    function MSE to compute the mean square error
"""
def MSE(x,y):
    return np.sum((x - y)**2)

"""
    function CARTReg is for to compute the regression tree
    input:  
        X is the train data,y is the label data,y is continues value
    output:
        out is optimal split point compute by Least Square Error
"""
def CARTRegTree(X,y):
    split_point = np.zeros(X.size-1)
    for i in range(X.size):
        split_point[i-1] = (X[i-1] + X[i]) / 2

    cm = np.zeros(split_point.size)
    for j in range(split_point.size):
        X_LOW = X[X < split_point[j]]
        X_HIGH = X[X >= split_point[j]]
        c1 = np.mean(y[X_LOW - 1])
        c2 = np.mean(y[X_HIGH - 1])
        cm[j] = MSE(y[X_LOW-1],c1) + MSE(y[X_HIGH -1],c2)

    split_pos = np.argmin(cm)

    low_limit = y[X < split_point[split_pos]]
    high_limit = y[X >= split_point[split_pos]]
    low = np.mean(low_limit)
    high = np.mean(high_limit)
    Tree = np.array([split_point[split_pos],low,high])
    return Tree

"""
    updata the error of predict and label yi
"""
def computeError(tree,y):
    temp = y[X < tree[0]]
    temp = temp - tree[1]
    temp1 = y[X >= tree[0]]
    temp1 = temp1 - tree[2]
    res = np.append(temp, temp1)
    error = np.sum(res ** 2)
    return res,error
"""
    function Compute the mse of predict and real label
"""
def train(X,y,threshold = 0.1,iter_time = 10):
    Tree = np.array([])
    Error = np.array([])
    for i in range(iter_time):
        tree = CARTRegTree(X,y)
        res,error = computeError(tree,y)
        Tree = np.append(Tree, tree)
        Error = np.append(Error, error)
        y = res
        if error <= threshold:
            break
    Error = Error.flatten()
    Tree = Tree.reshape(-1,3)
    return Tree,Error

threshold = 0.1
iter_time = 20
X = np.arange(1,11)
y = np.array([5.56,5.7,5.91,6.4,6.8,7.05,8.9,8.7,9,9.05])
Tree,Error = train(X,y,threshold,iter_time)

print(Tree,'\n',Error)
