import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model # type: ignore

values_neative = {"age": 64,
          "gender": 1,
          "impluse": 66,
          "pressurehight": 160,
          "pressurelow": 83.0,
          "glucose": 5.075174,
          "kcm": 0.587787,
          "troponin": -4.422849
          }


values_positive = {"age": 21,
          "gender": 1,
          "impluse": 94,
          "pressurehight": 98,
          "pressurelow": 46,
          "glucose": 5.690359,
          "kcm": 1.909543,
          "troponin": 0.058269
          }

mymodel = load_model("GUI\classification\ANN.h5")

# Convert values dictionary to DataFrame
input_df = pd.DataFrame(values_positive, index=[0])

scaler = StandardScaler()

def scaling(df):
    scaled_df = scaler.fit_transform(df)
    return scaled_df

# Log transformation
# Log transformation
def log_transform(df, col_name):
    col_transformed = np.log(df[col_name] + 1e-10)  # Adding a small constant to prevent zero or negative values
    return col_transformed

# Apply log transformation to each column

input_df['glucose'] = log_transform(input_df, "glucose")
input_df['kcm'] = log_transform(input_df, "kcm")
input_df['troponin'] = log_transform(input_df, "troponin")

# Scale the transformed data
sc_df = scaling(input_df)

# Now you can use the input_list for predictions with your model
predictions = mymodel.predict(sc_df)

threshold = 0.5
y_pred_ann = mymodel.predict(sc_df)
print(y_pred_ann)
y_pred_binary = np.where(y_pred_ann >= threshold, 1, 0)

print("Predictions:", predictions[0][0])
print("Predictions:", y_pred_binary[0][0])
if y_pred_binary[0] == 0:
     print("The patient does not have heart problems")
else:
     print("The patient has heart problems")