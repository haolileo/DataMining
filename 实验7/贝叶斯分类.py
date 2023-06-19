import bayes as bayes
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import sklearn.naive_bayes as bayes
iris = load_iris()  #iris数据集
X_iris=iris.data
Y_iris=iris.target
train_x_iris,test_x_iris,train_y_iris,test_y_iris=train_test_split(X_iris,Y_iris,test_size=0.3,random_state=2)
#1.获取朴素贝叶斯分类器的高斯模型,并训练
gaussian = bayes.GaussianNB()
bernoulli = bayes.BernoulliNB()
multionmial =bayes.MultinomialNB()

gaussian.fit(train_x_iris,train_y_iris)
bernoulli.fit(train_x_iris,train_y_iris)
multionmial.fit(train_x_iris,train_y_iris)    #输入数据出现负值,不能使用MultinomialNB

#2.进行预测
test_y_gaussianHat_iris = gaussian.predict(test_x_iris)
test_y_bernoulliHat_iris = bernoulli.predict(test_x_iris)
test_y_multionmialHat_iris = multionmial.predict(test_x_iris)

#3.输出准确率
score_gaussian = gaussian.score(test_x_iris,test_y_iris)
score_bernoulli = bernoulli.score(test_x_iris,test_y_iris)
score_multionmial = multionmial.score(test_x_iris,test_y_iris)
print("gaussian score:"+str(score_gaussian))
print("bernoulli score:"+str(score_bernoulli))
print("multionmial score:"+str(score_multionmial))