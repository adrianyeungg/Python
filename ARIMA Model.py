import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Example data for GDP growth (quarterly data)
quarters = np.arange(1, 21)
gdp_growth = np.array([2.1, 1.9, 2.5, 3.0, 2.8, 3.2, 3.5, 3.7, 3.6, 3.9, 4.1, 4.2, 4.0, 4.3, 4.5, 4.7, 4.8, 5.0, 5.2, 5.1])

# Create a DataFrame to hold the data
data = pd.DataFrame({'Quarter': quarters, 'GDP_Growth': gdp_growth})

# Fit the ARIMA model
model = ARIMA(data['GDP_Growth'], order=(1, 1, 1))
results = model.fit()

# Forecast GDP growth for the next quarter (21st quarter)
forecasted_growth, _, _ = results.forecast(steps=1)

print(f"Forecasted GDP Growth for the next quarter: {forecasted_growth[0]:.2f}%")

# Plot the actual data and forecast
data.set_index('Quarter', inplace=True)
plt.plot(data, label='Actual GDP Growth')
plt.plot(21, forecasted_growth[0], 'ro', label='Forecast')
plt.legend()
plt.xlabel('Quarter')
plt.ylabel('GDP Growth (%)')
plt.title('Actual and Forecasted GDP Growth')
plt.show()
