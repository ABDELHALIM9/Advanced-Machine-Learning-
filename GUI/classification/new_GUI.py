import tkinter as tk
from tkinter import Button, Entry, Frame, Label
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, PowerTransformer
from keras.models import load_model



'''
def predict_svm(data):
    # Load saved models
    with open('D:\coding\Data_Science\Advanced-Machine-Learning-\classification/SVM.pkl','rb') as file:
        svm_model = pickle.load(file) # model is loaded into : ourModel
    prediction = svm_model.predict(data)
    print("################################")
    print(prediction)
    return "classs0.9"

    #############################################
# Function to predict using Support Vector Machine model
def predict_svm(values):
    with open(r'D:\coding\Data_Science\Advanced-Machine-Learning-\GUI\Regression\model_SVM.pkl', 'rb') as file:
        model = pickle.load(file)
    predictions = model.predict(values)
    return predictions
'''


# Function to predict using Artificial Neural Network model
def predict_ann(values):
    model = load_model('D:\coding\Data_Science\Advanced-Machine-Learning-\GUI\classification/ANN.h5')
    print("agogogogogogogogogogogo")
    predictions = model.predict(values)
    print(f"\n{predictions[0][0]}")
    return predictions[0]


root = tk.Tk()
root.title("Heart Attack Prediction")
root.geometry("550x200")

def center_window(frame):
    frame.update_idletasks()
    width = frame.winfo_width()
    height = frame.winfo_height()
    x = (frame.winfo_screenwidth() // 2) - (width // 2)
    y = (frame.winfo_screenheight() // 2) - (height // 2)
    frame.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Labels
labels = ['age', 'gender', 'impulse', 'pressure_high', 'pressure_low', 'glucose', 'kcm', 'troponin']

label_entries = {}

for i in range(0, len(labels), 2):
    label_frame = Frame(root)
    label_frame.pack(fill=tk.X, padx=20, pady=5, anchor='center')  # Aligning center on x-axis

    for j in range(2):
        if i + j < len(labels):
            label_text = labels[i + j]
            label = Label(label_frame, text=label_text, width=15, anchor='center')
            label.grid(row=0, column=j*2, sticky='w')

            entry = Entry(label_frame)
            entry.grid(row=0, column=j*2+1, padx=5, sticky='ew')

            label_entries[label_text] = entry

# Pre-processing
def preprocessing(df):
    
    pass 

# Function to get user input, preprocess, predict, and display result
def display_prediction():
    values = {}
    for label_text, entry in label_entries.items():
        values[label_text] = float(entry.get())
    data = pd.DataFrame([values])
    print(data)

    # Predict using SVM
    svm_prediction = predict_svm(data)
    # Predict using ANN
    ann_prediction = predict_ann(data)

    # Display result
    # commented line

    if ann_prediction[0] == 1 or svm_prediction[0] == 1:
        result = "You have a heart attack!"
    else:
        result = "You don't have a heart attack."

    result_label.config(text=result)

# Button to submit values and display result
submit_button = Button(root, text="Predict", command=display_prediction)
submit_button.pack(pady=20)

# Frame to display the result
result_frame = Frame(root)
result_frame.pack(fill=tk.X, padx=20, pady=5)
result_label = Label(result_frame, text="", width=30, anchor='w')
result_label.pack(side=tk.LEFT)

root.mainloop()
