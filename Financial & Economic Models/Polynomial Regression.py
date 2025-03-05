import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Example data for price and quantity demanded
prices = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
quantity_demanded = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190])

# Create a DataFrame to hold the data
data = pd.DataFrame({'Price': prices, 'Quantity_Demanded': quantity_demanded})

# Fit a polynomial regression model
degree = 2  # Degree of the polynomial (you can adjust this)
poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(data[['Price']])
model = LinearRegression()
model.fit(X_poly, quantity_demanded)

# Calculate the demand for the product at a given price
given_price = 8
given_price_poly = poly_features.transform(np.array([given_price]).reshape(-1, 1))
predicted_demand = model.predict(given_price_poly)[0]

print(f"Demand for the product at ${given_price} price: {predicted_demand:.2f} units")

# Plot the actual data and the polynomial regression curve
plt.scatter(data['Price'], data['Quantity_Demanded'], label='Actual Data')
plt.plot(data['Price'], model.predict(X_poly), color='red', label='Polynomial Regression')
plt.xlabel('Price')
plt.ylabel('Quantity Demanded')
plt.title('Price vs. Quantity Demanded')
plt.legend()
plt.show()
