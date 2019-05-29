# -*- coding: utf-8 -*-

#Created on Fri May  6 20:42:18 2005

#@author: student
import numpy as np
from sklearn.metrics import confusion_matrix,recall_score,precision_score,f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB,BernoulliNB
x=np.random.rand(2000,20)
y=np.random.randint(0,2,2000)
clf=LogisticRegression()
clf.fit(x,y)
pred=clf.predict(x)
print(y)
print(pred)
cm=confusion_matrix(y,pred)
#print(cm)

print('f-score=',f1_score(y,pred, average=None)) 

print('f-score=',f1_score(y,pred, average='macro')) 



print('--Gaussian-----')

clf=GaussianNB()
clf.fit(x,y)
pred=clf.predict(x)
print(y)
print(pred)


print('f-score=',f1_score(y,pred, average=None)) 

print('f-score=',f1_score(y,pred, average='macro')) 






"""
for i in range(0,3):
    print('recall of',i,'is',recall_score(y,pred,labels=[i], average='micro'))
    print('precision=',i,'is',precision_score(y,pred,labels=[i], average='micro'))
    print('f-score=',i,'is',f1_score(y,pred,labels=[i], average='micro'))
"""