from tkinter import *
import tkinter as tk
import tkinter.messagebox
import numpy as np
import pandas as pd 
import pickle
from tensorflow import keras
from keras.models import load_model


# Labels
labels = ['sqft_living', 'sqft_lot','sqft_basement', 'yr_built',
          'lat', 'long', 'grade', 'condition','floors', 'bathrooms', 'bedrooms']

coulmnss = ['price', 'sqft_living', 'sqft_lot', 'sqft_basement','yr_built', 'lat', 'long']
label_entries = {}

# models prediction Function
def predict_svm(values): 
    with open(r'D:\coding\Data_Science\Advanced-Machine-Learning-\Regression\model_SVM','rb') as file:
        SVM_model = pickle.load(file) # model is loaded into : ourModel
    print("SVM Model Loaded Successfully")
    predictions = SVM_model.predict(values)
    return predictions[0]

def predict_ann(values):
    model = load_model('D:\coding\Data_Science\Advanced-Machine-Learning-\Regression\model_ANN.h5')
    print("ANN Model Loaded Successfully")
    y_pred = model.predict(values)
    return y_pred[0][0]

# pre-processing function 
def preprocessing(df):
    copy = df[["grade","condition","floors","bathrooms","bedrooms"]]
    df['price'] = 0
    df = df.reindex(columns=coulmnss)
    with open(r'Regression\preprocessing\transformer_new.pkl','rb') as file:
        transform = pickle.load(file) # model is loaded into : ourModel
    with open(r'Regression\preprocessing\scaler_new.pkl','rb') as file:
        scaler = pickle.load(file) # model is loaded into : ourModel
    df = scaler.transform(df)
    transformed_df = transform.transform(df)
    transformed_df = pd.DataFrame(transformed_df, columns=coulmnss)
    transformed_df= transformed_df.drop('price',axis =1)
    transformed_df[['grade','condition','floors','bathrooms','bedrooms']] = copy[['grade','condition','floors','bathrooms','bedrooms']]
    return transformed_df

# function to reverse the transform to get the real value of price "predection"
def rev(price, df ):
    df['price'] = price
    df = df.reindex(columns=coulmnss)
    with open(r'Regression\preprocessing\transformer_new.pkl','rb') as file:
        transform = pickle.load(file) # model is loaded into : ourModel
    with open(r'Regression\preprocessing\scaler_new.pkl','rb') as file:
        scaler = pickle.load(file) # model is loaded into : ourModel
    transformed_df = transform.inverse_transform(df)
    scaled_df = scaler.inverse_transform(transformed_df)
    return scaled_df[0][0]



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
    

# frame for arranging the labels and textboxes 
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
    print("Before pre processing:")
    print(50*"-")
    print(data)

    #preprocessing operation "Function"
    df = preprocessing(data)
    print("After pre processing:")
    print(50*"-")
    print(df)

    # Predict prices for each model (SVM - ANN)
    svm_price = predict_svm(df)
    ann_price = predict_ann(df)

    # reverse the value of the price "the predction"
    svm_price_inv=rev(svm_price,df)
    ann_price_inv= rev(ann_price,df)


    # Display predicted prices
    svm_label.config(text=f"SVM Price: {str('%.2f'%svm_price_inv)} $")
    ann_label.config(text=f"ANN Price: {str('%.2f'%ann_price_inv)} $")


# Button to submit values and display predicted prices
submit_button = Button(root, text="Submit", command=display_prices)
submit_button.pack(pady=20)

# Frames to display predicted prices for each model
svm_frame = Frame(root)
svm_frame.pack(fill=X, padx=20, pady=5)
svm_label = Label(svm_frame, text="SVM Price: ", width=20, anchor='w')
svm_label.pack(side=LEFT)

ann_frame = Frame(root)
ann_frame.pack(fill=X, padx=20, pady=5)
ann_label = Label(ann_frame, text="ANN Price: ", width=20, anchor='w')
ann_label.pack(side=LEFT)

root.mainloop()