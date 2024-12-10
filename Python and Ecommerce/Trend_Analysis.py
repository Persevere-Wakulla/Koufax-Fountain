"""Trend Analysis and Forecasting: Python can be used to analyze fashion trends and forecast future styles, helping you stay ahead in the competitive streetwear/high fashion market.
    """

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load trend data
trends = pd.read_csv("trend_data.csv")

# Prepare data for forecasting
X = np.array(range(len(trends))).reshape(-1, 1)
y = trends["popularity"]

# Apply linear regression
model = LinearRegression()
model.fit(X, y)

# Forecast future trend popularity
future = model.predict(np.array(range(len(trends), len(trends) + 12)).reshape(-1, 1))
print("Future trend popularity:", future)
