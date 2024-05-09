#from sklearn.tree import DecisionTreeRegressor
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import numpy as np
import pandas as pd 
import pickle
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras.models import load_model
#import tensorflow as tf
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import  StandardScaler
import joblib

'''
def predict_decision_tree(values):
    # load model 
    with open(r'D:\coding\Data_Science\Advanced-Machine-Learning-\GUI\Regression/model_DT','rb') as file:
        DT_model = pickle.load(file) # model is loaded into : ourModel
    predictions = DT_model.predict(values)
    return predictions
'''

# Labels
labels = ['sqft_living', 'sqft_lot','sqft_basement', 'yr_built', 
          'lat', 'long', 'grade', 'condition', 
          'floors', 'bathrooms', 'bedrooms']

label_entries = {}

def predict_svm(values):
    # load model 
    with open(r'D:\coding\Data_Science\Advanced-Machine-Learning-\GUI\Regression/model_SVM','rb') as file:
        DT_model = pickle.load(file) # model is loaded into : ourModel
    predictions = DT_model.predict(values)
    return predictions[0]

def predict_ann(values):
    #start here the fitting the data and know the accurecy
    model = load_model('D:\coding\Data_Science\Advanced-Machine-Learning-\GUI\Regression/model_ANN.h5')
    print("mega")
    y_pred = model.predict(values)
    return y_pred[0][0]

# pre-processing 
def preprocessing(df):
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df)
    transformer = PowerTransformer(method = "yeo-johnson")
    transformed_df = transformer.fit_transform(scaled_df)
    return transformed_df

def PriceScaleTra(price):
    transformer = PowerTransformer(method = "yeo-johnson")
    price_reshaped = np.array(price).reshape(1, -1)
    inverse_transformed_value = transformer.inverse_transform(price_reshaped)
    # Then, inverse transform using the StandardScaler
    scaler = StandardScaler()
    final_predicted_value = scaler.inverse_transform(inverse_transformed_value)
    return final_predicted_value

root = Tk()
root.title("House Price Prediction Regression")
root.geometry("550x400")

def center_window(frame):
    frame.update_idletasks()
    width = frame.winfo_width()
    height = frame.winfo_height()
    x = (frame.winfo_screenwidth() // 2) - (width // 2)
    y = (frame.winfo_screenheight() // 2) - (height // 2)
    frame.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    


for i in range(0, len(labels), 2):
    label_frame = Frame(root)
    label_frame.pack(fill=X, padx=20, pady=5, anchor='center')  # Aligning center on x-axis
    
    for j in range(2):
        if i + j < len(labels):
            label_text = labels[i + j]
            label = Label(label_frame, text=label_text, width=15, anchor='center')
            label.grid(row=0, column=j*2,sticky='w')
            
            entry = Entry(label_frame)
            entry.grid(row=0, column=j*2+1, padx=5,sticky='ew')
            
            label_entries[label_text] = entry


# Function to calculate predicted prices and display them
def display_prices():
    values = {}
    for label_text, entry in label_entries.items():
        value = entry.get()
        if not value:  # Check if the entry is empty
            # Display a message and return
            tk.messagebox.showwarning("Warning", "Please fill in all values.")
            return
        values[label_text] = entry.get()
    data = pd.DataFrame([values])
    print(data)
    print("After pre processing:")
    print(500*"-")
    df = preprocessing(data)
    print("After pre processing:")
    print(500*"-")
    print(df)
    # Predict prices using each model
    #decision_tree_price = predict_decision_tree(df)
    svm_price = predict_svm(df)
    ann_price = predict_ann(df)

    # inverse the transform 
    svm_price_tra = PriceScaleTra(svm_price)
    ann_price_tra = PriceScaleTra(ann_price)

    # Display predicted prices
    #decision_tree_label.config(text=f"DecisionTree Price: {decision_tree_price}")
    svm_label.config(text=f"SVM Price: {pd.DataFrame({'price':svm_price_tra})}")
    ann_label.config(text=f"ANN Price: {pd.DataFrame({'price':ann_price_tra})}")


# Button to submit values and display predicted prices
submit_button = Button(root, text="Submit", command=display_prices)
submit_button.pack(pady=20)

# Frames to display predicted prices for each model
'''
decision_tree_frame = Frame(root)
decision_tree_frame.pack(fill=X, padx=20, pady=5)
decision_tree_label = Label(decision_tree_frame, text="DecisionTree Price: ", width=20, anchor='w')
decision_tree_label.pack(side=LEFT)
'''
svm_frame = Frame(root)
svm_frame.pack(fill=X, padx=20, pady=5)
svm_label = Label(svm_frame, text="SVM Price: ", width=20, anchor='w')
svm_label.pack(side=LEFT)

ann_frame = Frame(root)
ann_frame.pack(fill=X, padx=20, pady=5)
ann_label = Label(ann_frame, text="ANN Price: ", width=20, anchor='w')
ann_label.pack(side=LEFT)

root.mainloop()