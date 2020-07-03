# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:58:50 2020

@author: Dushant

"""

import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))


window= tk.Tk()
window.title=(" Social prediction")

#creating label for first name

age_label= ttk.Label(window,text="Please enter your age")
age_label.grid(row=0, column=0, sticky=tk.W)

#entry box
    
age_var= tk.IntVar() #we made a varile to store name
age_entrybox= ttk.Entry(window, width= 18, textvariable= age_var)
age_entrybox.grid(row=0, column=2)
age_entrybox.focus()

salary_label= ttk.Label(window,text="Please enter your Salary")
salary_label.grid(row=12, column=0, sticky=tk.W)

salary_var= tk.IntVar() #we made a varile to store name
salary_entrybox= ttk.Entry(window, width= 18, textvariable= salary_var)
salary_entrybox.grid(row=12, column=2)
salary_entrybox.focus()

def action1():
    #print('pending')
    age= age_var.get()
    salary= salary_var.get()
    age=np.dtype('int64').type(age)
    salary=np.dtype('int64').type(salary)
    #print(type(age))
    F=[]
    #age.to_numpy().reshape(-1,1)
    #age=np.array(age,salary)
    #salary=np.array(salary)
    F.extend([age,salary])
    #print(type(F))
    final = pd.Series(F)
    
    prediction = model.predict([final])
    #print(prediction)
    
    if prediction == [1]:
         msg = tk.Message(window, text = "Customer will buy the product. ")
         msg.config(bg='lightgreen', font=('times', 9, 'italic'),borderwidth= 10)
         msg.grid(row=18, column=1)
    else:
        msg = tk.Message(window, text = "Customer will not buy the product. You wana see more products? ")
        msg.config(bg='lightgreen', font=('times', 9, 'italic'),borderwidth= 10)
        msg.grid(row=18, column=1,columnspan =1, rowspan = 5)
        
        
        
first_button= ttk.Button(window, text='Submit', command= action1)
first_button.grid()


window.mainloop()