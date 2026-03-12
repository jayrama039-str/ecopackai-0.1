import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


# LOAD DATASET
data = pd.read_csv("ml_model/ecopack_material_dataset_5000.csv")


# FEATURES
X = data[[
    "durability_score",
    "weight_capacity_kg",
    "biodegradability_score",
    "recyclability_percent",
    "co2_emission_score"
]]

# TARGET
y = data["material_type"]


# LABEL ENCODER
le_material = LabelEncoder()
y = le_material.fit_transform(y)


# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# MODEL
model = RandomForestClassifier(n_estimators=100)


# TRAIN MODEL
model.fit(X_train, y_train)


# SAVE MODEL
pickle.dump(model, open("ml_model/packaging_model.pkl", "wb"))
pickle.dump(le_material, open("ml_model/le_material.pkl", "wb"))


print("Model trained successfully")