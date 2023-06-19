from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
Xtrain,Xtest,Ytrain,Ytest = train_test_split(iris.data,iris.target,test_size=0.3)

clf = tree.DecisionTreeClassifier(max_depth=2  #最大深度是2，这个也可以填3或4试试看
                                 ,min_samples_leaf=5 #下一个叶子节点大于5会进行，小于5就不会再分
                                 ,min_samples_split=10 #最小分支节点，当前样本大于10才会分
                                 ,max_features=3 #最大特征数，有一个重要程度为0
                                    )
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)
print(score)