# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:35:06 2020

@author: HP
"""


import tkinter as tk
import pandas as pd
import re
import numpy as n
from tkinter import ttk
import pickle

data= pd.read_csv("D:\All Python\Social_Network_Ads.csv")
#print(data.head())

X= data.drop('Purchased',axis=1)
Y= data['Purchased']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.22, random_state = 0)


#Decision Tree
from sklearn.tree import DecisionTreeClassifier
decisiontree = DecisionTreeClassifier()
decisiontree.fit(x_train, y_train)
#y_pred = decisiontree.predict(x_test)
#acc_decisiontree = round(accuracy_score(y_pred, y_test) * 100, 2)
#print(acc_decisiontree)

# Saving model to disk
pickle.dump(decisiontree, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[12, 9000]]))