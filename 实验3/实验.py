import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import OrdinalEncoder
dataSet1 = [['<=30', 'high', 'no', 'fair', 'no'],
               ['<=30', 'high', 'no', 'excellent', 'no'],
               ['31…40', 'high', 'no', 'fair', 'yes'],
               ['>40', 'medium', 'no', 'fair', 'yes'],
               ['>40', 'low', 'yes', 'fair', 'yes'],
               ['>40', 'low', 'yes', 'excellent', 'no'],
               ['31…40', 'low', 'yes', 'excellent', 'yes'],
               ['<=30', 'medium', 'no', 'fair', 'no'],
               ['<=30', 'low', 'yes', 'fair', 'yes'],
               ['>40', 'medium', 'yes', 'fair', 'yes'],
               ['<=30', 'medium', 'yes', 'excellent', 'yes'],
               ['31…40', 'medium', 'no', 'excellent ', 'yes'],
               ['31…40', 'high', 'yes', 'fair', 'yes'],
               ['>40', 'medium', 'no', 'excellent', 'no']]
enc = OrdinalEncoder()
enc.fit(dataSet1)
dataSet1 = enc.transform(dataSet1)
dataSet1 = pd.DataFrame(dataSet1)
print(dataSet1)
clf = tree.DecisionTreeClassifier()
clf.fit(dataSet1[[0,1,2,3]],dataSet1[4])
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('电脑')

dataSet2 = [['晴', '热', '高', '否', '否'],
            ['晴', '热', '高', '是', '否'],
            ['阴', '热', '高', '否', '是'],
            ['雨', '温', '高', '否', '是'],
            ['雨', '凉爽', '中', '否', '是'],
            ['雨', '凉爽', '中', '是', '否'],
            ['阴', '凉爽', '中', '是', '是'],
            ['晴', '温', '高', '否', '否'],
            ['晴', '凉爽', '中', '否', '是'],
            ['雨', '温', '中', '否', '是'],
            ['晴', '温', '中', '是', '是'],
            ['阴', '温', '高', '是', '是'],
            ['阴', '热', '中', '否', '是'],
            ['雨', '温', '高', '是', '否']]
enc.fit(dataSet2)
dataSet2 = enc.transform(dataSet2)
dataSet2 = pd.DataFrame(dataSet2)
print(dataSet2)
clf.fit(dataSet2[[0,1,2,3]],dataSet2[4])
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('打球')