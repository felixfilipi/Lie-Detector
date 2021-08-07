#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

class single_layer_perceptron:
    
    def __init__(self ,x ,y ,epoch ,learning_rate):
        self.layer = {
            "input":3,
            "output":1
        }
        self.weight = np.random.rand(self.layer['input'])
        self.bias = np.random.rand(self.layer['output'])
        self.epoch = epoch
        self.learning_rate = learning_rate
        self.feature = x
        self.target = y
                
    def feed_forward(self, z):
        self.feed = np.matmul(self.weight, z) + self.bias
        return self.heaviside_activation(self.feed)

    def heaviside_activation(self, feed):
        if self.feed >= 0:
            return 1
        else:
            return 0

    def train(self):
        for i in range (self.epoch):
            self.stochastic = np.random.randint(0 ,self.feature.shape[0])
            self.data = self.feature[self.stochastic]
            
            self.prediction = self.feed_forward(self.data)
            self.error = self.target[self.stochastic] - self.prediction
            self.weight = self.weight + self.data * self.learning_rate * self.error
            self.bias = self.bias + self.learning_rate * self.error
    
    def train_accuracy(self):
        match = 0
        for index, data in enumerate(feature):
            self.output = self.feed_forward(data)
            print("Target = ", self.target[index])
            print("Prediction = ", self.output)
            if (self.target[index]==self.output):
                match += 1
                
        print("Accuracy = {} %".format(round(match*100/feature.shape[0],2)))

    def predict(self, test):
        self.output = self.feed_forward(test)
        if (self.output == 1):
            return "Not Lying"
        else:
            return "Lying"


# In[2]:


dataset = pd.read_csv('lie-dataset.csv').values
feature = dataset[:,:-1]
target = dataset[:,-1:]
target = np.vstack([np.unique(target[:,:],return_inverse=True)[1]]).reshape(-1)
clf = single_layer_perceptron(feature,target,epoch = 2000, learning_rate = 0.001)
clf.train()
clf.train_accuracy()


# In[3]:


import tkinter as tk
from tkinter import messagebox

class lie_detector(tk.Tk):
        
    def __init__(self):
        
        #init windows
        tk.Tk.__init__(self)
        self.title("Lie Detector")
        self.geometry('400x400')
        self.label_heart = tk.Label(self, text="Heart Rate")
        self.label_heart.grid(row = 0,column = 0)
        
        self.label_blink = tk.Label(self, text="Blink Frequency")
        self.label_blink.grid(row = 1, column = 0)
        
        self.label_eye = tk.Label(self, text="Eye Contact")
        self.label_eye.grid(row = 2, column = 0)
        
        self.entry_heart = tk.Entry(self)
        self.entry_heart.grid(row = 0, column = 1)
        
        self.entry_blink = tk.Entry(self)
        self.entry_blink.grid(row = 1, column = 1)
        
        self.entry_eye = tk.Entry(self)
        self.entry_eye.grid(row = 2, column = 1)
        
        self.button = tk.Button(self,text="Enter",bg="#000",fg="#fff", command = self.close_window)
        self.button.grid(row=3, column = 1)
        
    def close_window(self):
        self.heart = int(self.entry_heart.get())
        self.blink = int(self.entry_blink.get())
        self.eye = int(self.entry_eye.get())
        self.test = [self.heart ,self.blink ,self.eye]
        self.result = clf.predict(self.test)
        messagebox.showinfo("Result",'He is {}'.format(self.result))
        self.destroy()
        
app = lie_detector()
app.mainloop()

