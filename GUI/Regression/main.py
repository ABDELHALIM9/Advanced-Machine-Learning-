import sys
from tkinter import *
from tkinter import messagebox



#  functions ay kalam for model predictions
def predict_decision_tree(values):
    return 300000

def predict_svm(values):
    return 280000

def predict_ann(values):
    return 320000

root = Tk()
root.title("House Price Prediction")
root.geometry("550x600")

def center_window(frame):
    frame.update_idletasks()
    width = frame.winfo_width()
    height = frame.winfo_height()
    x = (frame.winfo_screenwidth() // 2) - (width // 2)
    y = (frame.winfo_screenheight() // 2) - (height // 2)
    frame.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
# Labels
labels = ['price', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement', 'yr_built', 
          'lat', 'long', 'sqft_living15', 'sqft_lot15', 'date', 'grade', 'condition', 
          'floors', 'bathrooms', 'bedrooms']

label_entries = {}

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
        values[label_text] = entry.get()

    # Predict prices using each model
    decision_tree_price = predict_decision_tree(values)
    svm_price = predict_svm(values)
    ann_price = predict_ann(values)

    # Display predicted prices
    decision_tree_label.config(text=f"DecisionTree Price: {decision_tree_price}")
    svm_label.config(text=f"SVM Price: {svm_price}")
    ann_label.config(text=f"ANN Price: {ann_price}")


# Button to submit values and display predicted prices
submit_button = Button(root, text="Submit", command=display_prices)
submit_button.pack(pady=20)

# Frames to display predicted prices for each model
decision_tree_frame = Frame(root)
decision_tree_frame.pack(fill=X, padx=20, pady=5)
decision_tree_label = Label(decision_tree_frame, text="DecisionTree Price: ", width=20, anchor='w')
decision_tree_label.pack(side=LEFT)

svm_frame = Frame(root)
svm_frame.pack(fill=X, padx=20, pady=5)
svm_label = Label(svm_frame, text="SVM Price: ", width=20, anchor='w')
svm_label.pack(side=LEFT)

ann_frame = Frame(root)
ann_frame.pack(fill=X, padx=20, pady=5)
ann_label = Label(ann_frame, text="ANN Price: ", width=20, anchor='w')
ann_label.pack(side=LEFT)

root.mainloop()
