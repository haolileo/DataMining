import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
X = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
              [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
y = [0, 1, 1, 1, 2, 3, 3, 4]
clf = tree.DecisionTreeClassifier()   # 创建决策树分类器
clf.fit(X, y)                         # 拟合
# DecisionTreeClassifier(class_weight=None, criterion='gini',
#                        max_depth=None,
#                        max_features=None, max_leaf_nodes=None,
#                        min_impurity_decrease=0.0,
#                        min_samples_leaf=1, min_samples_split=2,
#                        min_weight_fraction_leaf=0.0, presort=False,
#                        random_state=None, splitter='best')
clf.predict([[1, 0, 0]])                # 分类
#array([2])
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)  # 导出决策树
graph = graphviz.Source(dot_data)                    # 创建图形
graph.render('result')                               # 输出PDF文件