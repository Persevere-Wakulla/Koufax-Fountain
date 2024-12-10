"""Data Analysis and Visualization: Python, with libraries like Pandas and Matplotlib, can help you analyze sales data, customer behavior, and market trends. This can inform your design choices, pricing strategies, and marketing campaigns.
    """

import pandas as pd
import matplotlib.pyplot as plt

# Load sales data
data = pd.read_csv("sales_data.csv")

# Analyze top-selling categories
top_categories = data["category"].value_counts().head(5)

# Visualize sales trends
plt.figure(figsize=(10, 6))
plt.plot(data["date"], data["sales"])
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
