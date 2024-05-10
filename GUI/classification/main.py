import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Toplevel
import tkinter.messagebox
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, PowerTransformer,LabelEncoder, scale,StandardScaler
from tensorflow.keras.models import load_model


# Labels
labels = ['age', 'gender', 'impulse', 'pressure_high', 'pressure_low', 'glucose', 'kcm', 'troponin']

label_entries = {}

'''
def predict_ann(values):
    model = load_model("Advanced-Machine-Learning-\GUI\classification\ANN.h5")
    print("model loaded Successfully")
    predictions = model.predict(values)
    print(f"model Done Predection Successfully: {predictions[0][0]}")
    return predictions[0]
'''
#Data Scaling 
scaler = StandardScaler()
def scaling(df):
    scaled_df = scaler.fit_transform(df)
    return scaled_df

#Log transformation
def log_transform(df,col_name):
  col_transformed = np.log(df[col_name])
  return  col_transformed


# Pre-processing
def preprocessing(df):
    df.glucose = log_transform(df,'glucose')
    df.kcm = log_transform(df,'kcm')
    df.troponin =  log_transform(df,'troponin')
    df_done = scaling(df)
    return df_done 


def display_prediction():
    values = {}
    for label_text, entry in label_entries.items():
        value = entry.get()
        if not value:  # Check if the entry is empty
            # Display a message and return
            tk.messagebox.showwarning("Warning", "Please fill in all values.")
            return
        values[label_text] = float(entry.get())
    data = pd.DataFrame([values])
    print(f"values of input: \n{data}")
    #df = preprocessing(data)
    # Predict using ANN
    ann_prediction = predict_ann(data)
    print(f"the prediction:\n{data}")
    # Create a new window to display results
    result_window = Toplevel(root)
    result_window.title("Prediction Results")
    result_window.geometry("500x100")

    # Display ANN prediction
    ann_result_label = Label(result_window, text=f"ANN Prediction: {ann_prediction[0]}")
    ann_result_label.pack()

    # Combine the predictions and display final result
    final_result = "You have a heart attack!" if ann_prediction[0] >= 0.5 else "You don't have a heart attack."
    final_result_label = Label(result_window, text=f"Final Result: {final_result}")
    final_result_label.pack()

root = tk.Tk()
root.title("Heart Attack Classification Prediction")
root.geometry("550x200")

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


# Button to submit values and display result
submit_button = Button(root, text="Predict", command=display_prediction)
submit_button.pack(pady=20)

# Rest of your code for UI creation

root.mainloop()
