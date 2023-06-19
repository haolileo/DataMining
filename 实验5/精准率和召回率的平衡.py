# -*- coding: utf-8 -*-
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.datasets import load_iris
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False


def threshold(decision_scores):
    precisions = []
    recalls = []
    thresholds = np.arange(np.min(decision_scores), np.max(decision_scores), 0.1)
    for threshold in thresholds:
        y_predict = np.array(decision_scores >= threshold, dtype='int')
        precisions.append(precision_score(y_test, y_predict))
        recalls.append(recall_score(y_test, y_predict))

    plt.plot(thresholds, precisions, label='精准率')
    plt.plot(thresholds, recalls, label='召回率')
    plt.xlabel('阈值')
    plt.legend()
    plt.title('精准率和召回率随阈值的变化曲线')
    plt.show()

    plt.plot(precisions, recalls)
    plt.title('精准率和召回率的相关曲线')
    plt.xlabel('精准率')
    plt.ylabel('召回率')
    plt.show()

    precisions, recalls, thresholds = precision_recall_curve(y_test, decision_scores)
    plt.plot(thresholds, precisions[:-1], label='精准率')
    plt.plot(thresholds, recalls[:-1], label='召回率')
    plt.title('sklearn中精准率和召回率随阈值的变化曲线')
    plt.xlabel('阈值')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # 乳腺癌数据集
    digits = load_iris()
    X= digits.data
    y=digits.target
    print(y)
    y[load_iris().target ==1] = 0
    y[load_iris().target !=1] = 1
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
    log_reg = LogisticRegression(max_iter=100000)
    log_reg.fit(X_train, y_train)
    y_predict = log_reg.predict(X_test)
    decision_scores = log_reg.decision_function(X_test)
    threshold(decision_scores)
