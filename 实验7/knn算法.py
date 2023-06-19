from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

#return_X_y = True为了返回的数据是元组而不是字典
X, y = load_iris(return_X_y = True)
#将数据集进行划分，训练集占7份，测试集占3份
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3, train_size = 0.7, stratify = y, random_state = 42)
K = []
scores = []
#使用不同的邻居数进行训练测试
for k in range(1, 6) :
    knn = KNeighborsClassifier(n_neighbors = k)
    #训练
    knn.fit(train_X, train_y)
    #预测
    pred = knn.predict(test_X)
    #准确率并保留3位小数
    score = round(knn.score(test_X, test_y), 3)
    K.append(k)
    scores.append(score)
print(K,scores)