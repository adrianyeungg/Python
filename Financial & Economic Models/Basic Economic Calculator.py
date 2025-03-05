# Example data for price and quantity demanded
prices = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
quantity_demanded = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190])

# Create a DataFrame to hold the data
data = pd.DataFrame({'Price': prices, 'Quantity_Demanded': quantity_demanded})

# Split the data into features (price) and target variable (quantity demanded)
X = data[['Price']]
y = data['Quantity_Demanded']

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)

# Calculate the demand for the product at a given price
given_price = 8
predicted_demand = model.predict(np.array([given_price]).reshape(-1, 1))[0]

print(f"Demand for the product at ${given_price} price: {predicted_demand:.2f} units")
