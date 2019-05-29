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

x=np.random.randint(0,3,20)

#prediction function
def predme(x,y):
    
    clf.fit(x,y)
    pred=clf.predict(x)
    print("\nDependent data:\n",y)
    print("\nPredicted data:\n",pred)
    cm=confusion_matrix(y,pred)
    print("\nConfusion Matrix:\n",cm)
    for i in range(0,3):
        print('recall of',i,'is',recall_score(y,pred,labels=[i], average='micro'))
        print('precision of',i,'is',precision_score(y,pred,labels=[i], average='micro'))
        print('f-score of',i,'is',f1_score(y,pred,labels=[i], average='micro'))
    


y1=np.random.randint(0,3,20)
y2=np.random.randint(0,3,20)
y3=np.random.randint(0,3,20)
y4=np.random.randint(0,3,20)
y5=np.random.randint(0,3,20)
clf=LogisticRegression()
x2=x.reshape(-1,1)
print("Independent data:\n",x)
predme(x2,y1)
predme(x2,y2)
predme(x2,y3)
predme(x2,y4)
predme(x2,y5)

