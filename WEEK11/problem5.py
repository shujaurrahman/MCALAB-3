import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('WEEK11/demo.csv')

# Step a: Clean independent features
# Assuming nominal data in x1 and x2 needs to be converted to numeric using one-hot encoding
df = pd.get_dummies(df, columns=['x1', 'x2'], drop_first=True)

# Step b: Add feature x7 with random values between 0 and 1
df['x7'] = np.random.rand(len(df))

# Step c: Perform scaling on independent features
# Separate independent and dependent features
X = df.drop('y', axis=1)  # Independent features
y = df['y']  # Dependent feature

# Scale independent features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step d: Train using Logistic Regression, Decision Tree, and Random Forest
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define the models
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

# Store performance metrics
results = {}

for model_name, model in models.items():
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Make predictions
    
    # Calculate accuracy and F1 score
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    results[model_name] = {
        'Accuracy': accuracy,
        'F1 Score': f1,
        'Confusion Matrix': confusion_matrix(y_test, y_pred)
    }

# Print the performance metrics
for model_name, metrics in results.items():
    print(f"Model: {model_name}")
    print(f"Accuracy: {metrics['Accuracy']:.2f}")
    print(f"F1 Score: {metrics['F1 Score']:.2f}")
    print("\nConfusion Matrix:")
    print(metrics['Confusion Matrix'])
    print("\n")

# Step e: Draw confusion matrix for each model
for model_name, metrics in results.items():
    plt.figure(figsize=(5, 4))
    sns.heatmap(metrics['Confusion Matrix'], annot=True, fmt='d', cmap='Blues')
    plt.title(f'Confusion Matrix for {model_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
