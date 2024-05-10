import tkinter as tk
import subprocess

class MachineLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Machine Learning")

        self.title_label = tk.Label(root, text="Advanced Machine Learning", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.regression_button = tk.Button(root, text="Regression Project", command=self.run_regression)
        self.regression_button.pack(pady=5)

        self.classification_button = tk.Button(root, text="Classification Project", command=self.run_classification)
        self.classification_button.pack(pady=5)

    def run_regression(self):
        subprocess.Popen(["conda", "run", "-n", "abdo", "python", r"D:\coding\Data_Science\Advanced-Machine-Learning-\GUI\Regression\main.py"])

    def run_classification(self):
        subprocess.Popen(["conda", "run", "-n", "base", "python", r"D:\coding\Data_Science\Advanced-Machine-Learning-\GUI\classification\main.py"])

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x150")
    app = MachineLearningApp(root)
    root.mainloop()
