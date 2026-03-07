# Predictive Maintenance - Full Working Code

# Step 1: Import libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from xgboost import XGBClassifier


# Step 2: Load dataset
df = pd.read_csv("ai4i2020.csv")

# Step 3: Show first rows
print("First 5 rows:")
print(df.head())


# Step 4: Encode categorical column (Type)
le = LabelEncoder()
df['Type'] = le.fit_transform(df['Type'])


# Step 5: Remove unnecessary columns (if present)
if 'UDI' in df.columns:
    df = df.drop('UDI', axis=1)

if 'Product ID' in df.columns:
    df = df.drop('Product ID', axis=1)


# Step 6: Define features and target
X = df.drop('Machine failure', axis=1)
y = df['Machine failure']


# Step 7: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 8: Train XGBoost model
model = XGBClassifier(
    random_state=42,
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1
)

model.fit(X_train, y_train)


# Step 9: Make predictions
y_pred = model.predict(X_test)


# Step 10: Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)


# Step 11: Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Step 12: Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Step 13: Predict single example (optional)
sample = X_test.iloc[0:1]
prediction = model.predict(sample)

print("\nSample Prediction:", prediction)