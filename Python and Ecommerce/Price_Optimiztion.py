"""Price Optimization: Python can be used to develop dynamic pricing models based on factors like demand, seasonality, and competitor prices.
    """

import pandas as pd

# Load product data
products = pd.read_csv("products.csv")


# Define pricing strategy
def dynamic_pricing(row):
    if row["season"] == "high":
        return row["cost"] * 1.5
    elif row["season"] == "low":
        return row["cost"] * 1.2
    else:
        return row["cost"] * 1.3


# Apply dynamic pricing
products["new_price"] = products.apply(dynamic_pricing, axis=1)
products.to_csv("updated_prices.csv", index=False)
