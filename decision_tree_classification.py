# -*- coding: utf-8 -*-
"""Decision Tree Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SKTMof1Fs8UCxbyrdRCd973QG8tOF0iw
"""

import numpy as n
import pandas as p
import matplotlib.pyplot as plt

df=p.read_csv('/content/Social_Network_Ads (1).csv')
df

x=df.iloc[:,[2,3]].values
y=df.iloc[:,4 ].values
x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
x_train

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
x_train

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
y_pred

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

cm

