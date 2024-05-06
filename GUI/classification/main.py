import tkinter as tk
from tkinter import messagebox
#from sklearn.externals import joblib
from tensorflow.keras.models import load_model
import numpy as np
import pickle



# Function to predict using SVM
def predict_svm(data):
    # Load saved models
    with open(r'D:\coding\Data_Science\Advanced-Machine-Learning-\classification\SVM_tuned.pkl','rb') as file:
        svm_model = pickle.load(file) # model is loaded into : ourModel

    prediction = svm_model.predict(data)
    return "classs0.9"
'''
# Function to predict using Decision Tree
def predict_dt(data):
    # Load saved models
    dt_model = joblib.load('dt_model.pkl')
    prediction = dt_model.predict(data)
    return "classs1.1"
'''

'''
# Function to predict using ANN
def predict_ann(data):
    # Load save Models
    ann_model = load_model('ann_model.h5')
    prediction = np.argmax(ann_model.predict(data), axis=-1)
    return "classs1"
'''

# Function to handle button click event
def predict_class():
    # Get input data from GUI
    input_data = [float(entry1.get()), float(entry2.get())]  # Collect all input fields
    input_data = np.array(input_data).reshape(1, -1)  # Reshape to fit model input

    # Predict using all models
    svm_pred = predict_svm(input_data)
    #dt_pred = predict_dt(input_data)
    #ann_pred = predict_ann(input_data)

    # Display results
    messagebox.showinfo("Predictions", f"SVM Prediction: {svm_pred}\nDT Prediction: '''{dt_pred}'''\nANN Prediction:''' {ann_pred}'''")

# Tkinter GUI setup
root = tk.Tk()
root.title("Model Prediction")

# Add input fields
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
# Add more entries for each feature

# Add predict button
predict_button = tk.Button(root, text="Predict", command=predict_class)
predict_button.pack()

root.mainloop()
