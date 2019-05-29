# -*- coding: utf-8 -*-
"""
Create a Logistic Regression model for classification using one independent variable (3
classes 0,1 and 2) and 5 dependent variables (consider suitable random data or any suitable
dataset) by importing LogisticRegression from sklearn.

@author: Sagnik
"""

import numpy as np
from sklearn.metrics import confusion_matrix,recall_score,precision_score,f1_score
from sklearn.linear_model import LogisticRegression

"""
outlook=np.array([0,0,1,2,2])
temp=np.array([0,0,0,1,2])
humid=np.array([0,0,0,0,1])
windy=np.array([0,1,0,0,0])
play=np.array([0,0,1,1,1])
"""
x=np.array([[0,0,0,0,0],[0,0,0,1,0],[1,0,0,0,1],[2,1,0,0,1],[2,2,1,0,1]])
y=np.array([0,0,1,1,1])

clf=LogisticRegression()
clf.fit(x,y)
pred=clf.predict(x)
print(y)
print(pred)
cm=confusion_matrix(y,pred)
#print(cm)

print('f-score=',f1_score(y,pred, average=None)) 

print('f-score=',f1_score(y,pred, average='macro')) 


for i in range(0,3):
    print('recall of',i,'is',recall_score(y,pred,labels=[i], average='micro'))
    print('precision=',i,'is',precision_score(y,pred,labels=[i], average='micro'))
    print('f-score=',i,'is',f1_score(y,pred,labels=[i], average='micro'))