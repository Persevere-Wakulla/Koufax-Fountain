"""Customer Segmentation: Python can help analyze customer data to create targeted marketing campaigns and personalized shopping experiences.
    """

import pandas as pd
from sklearn.cluster import KMeans

# Load customer data
customers = pd.read_csv("customer_data.csv")

# Prepare data for clustering
X = customers[["purchase_frequency", "average_order_value", "brand_loyalty"]]

# Apply K-means clustering
kmeans = KMeans(n_clusters=3)
customers["segment"] = kmeans.fit_predict(X)

# Save segmented customer data
customers.to_csv("segmented_customers.csv", index=False)
