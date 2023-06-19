import numpy as np
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB

x = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
y = np.array([1,1,1,2,2,2])
clf = BernoulliNB()
print(clf.fit(x,y))
print(clf.predict([[-0.8,-1]]))
print(clf.predict_proba([[-0.8,-1]]))
print(clf.score([[-0.8,-1]],[1]))
print(clf.score([[-0.8,-1],[0,0]],[1,2]))

a = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
b = np.array([1,1,1,2,2,2])
clf = GaussianNB()
print(clf.fit(a,b))
print(clf.predict([[-0.8,-1]]))
print(clf.predict_proba([[-0.8,-1]]))
print(clf.score([[-0.8,-1]],[1]))
print(clf.score([[-0.8,-1],[0,0]],[1,2]))

c = np.array([[1,2],[2,1],[3,2],[1,1],[2,1],[3,3]])
d = np.array([1,1,1,2,2,2])
clf = MultinomialNB()
print(clf.fit(c,d))
print(clf.predict([[-0.8,-1]]))
print(clf.predict_proba([[-0.8,-1]]))
print(clf.score([[-0.8,-1]],[1]))
print(clf.score([[-0.8,-1],[0,0]],[1,2]))

e=np.array([[1, 3, 0, 0],
            [1, 3, 0, 1],
            [1, 3, 0, 0],
            [3, 2, 0, 0],
            [3, 1, 1, 0],
            [3, 1, 1, 1],
            [2, 1, 1, 1],
            [1, 2, 0, 0],
            [1, 1, 1, 0],
            [3, 2, 1, 0],
            [1, 2, 1, 1],
            [2, 2, 0, 1],
            [2, 3, 1, 0],
            [3, 2, 0, 1]])
f=np.array([0,0,1,1,1,0,1,0,1,1,1,1,1,0])
clf = GaussianNB()
print(clf.fit(e,f))
print(clf.predict([[1,2,1,0]]))