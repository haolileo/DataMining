from math import log
import operator
import pandas as pd
import numpy as np
def calcShannonEnt(dataSet):  # calculate entropy
    numEntries=len(dataSet)  #  the data length
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1] # the catalogy of each row of the data(the last one)
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1  # count the catalogies and the num of each catalogy
    shannonEnt=0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries # caculate the entropy of each catalogy
        shannonEnt-=prob*log(prob,2) # sum the entropy of each catalogy
    return shannonEnt

def createDataSet1():    # initialize the input datasets
    dataSet = [['晴', '热', '高', '否', '否'],
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
    labels = ['weather', 'temp', 'humidity', 'wind']
    return dataSet,labels

def splitDataSet(dataSet,axis,value): # the data of classifies by a feature
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec =featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):  # choose the best classifying feature
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)  # base entropy
    bestInfoGain = 0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob =len(subDataSet)/float(len(dataSet))
            newEntropy +=prob*calcShannonEnt(subDataSet)  # the entropy of classified
        infoGain = baseEntropy - newEntropy  # the difference entropy
        if (infoGain>bestInfoGain):   # the second best feature choose
            bestInfoGain=infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):    #sort the classified data
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]  # classify
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}} #store the result in dict
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet\
                            (dataSet,bestFeat,value),subLabels)
    return myTree

if __name__=='__main__':
    dataSet, labels=createDataSet1()  #create the dataset
    labels_tmp=labels[:]
    mytree=createTree(dataSet, labels)
    # print(labels_tmp)
    print(classify(mytree,labels_tmp,['雨','热','中','否']))