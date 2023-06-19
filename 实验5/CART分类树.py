import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
X = np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 1],
               [0, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0],
               [1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 1, 2],
               [1, 0, 1, 2], [2, 0, 1, 2], [2, 0, 1, 1],
               [2, 1, 0, 1], [2, 1, 0, 2], [2, 0, 0, 0]])
y = [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]
clf = tree.DecisionTreeClassifier()   # 创建决策树分类器
clf.fit(X, y)                         # 拟合
clf.predict([[1,1,1,2]])              # 分类
#array([2])
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)  # 导出决策树
graph = graphviz.Source(dot_data)                    # 创建图形
graph.render('result')                               # 输出PDF文件