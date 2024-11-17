import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Step 1: Generate random values for x1 and x2 (1000 samples)
np.random.seed(42)  # For reproducibility
x1 = np.random.rand(1000)  # Random values between 0 and 1
x2 = np.random.rand(1000)  # Random values between 0 and 1

# Step 2: Calculate y based on the given polynomial function
c = np.random.rand(1000)  # Random values for c between 0 and 1
y = x1**12 + 3 * x2**2 + c  # Polynomial function

# Step 3: Prepare the feature matrix and target vector
X = np.column_stack((x1, x2))  # Features: x1, x2
y = y  # Target: y

# Step 4: Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Apply Polynomial Features (degree=2, since it's a polynomial regression)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Step 6: Train a Polynomial Regression model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Step 7: Predict and calculate R-squared score on the test set
y_pred = model.predict(X_test_poly)
r2 = r2_score(y_test, y_pred)

# Print R-squared score
print(f"R-squared score for Polynomial Regression model: {r2}")

# Optional: Plot the predicted vs actual values for visualization (only for 2 features)
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values (Polynomial Regression)')
plt.show()
