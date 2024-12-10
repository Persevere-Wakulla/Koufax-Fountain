"""Automated Marketing Campaigns: Python can be used to automate and personalize email marketing campaigns based on customer behavior and preferences.
    """

import pandas as pd
from datetime import datetime, timedelta

# Load customer data
customers = pd.read_csv("customer_data.csv")

# Segment customers for a new collection launch
segment = customers[
    (customers["last_purchase"] < datetime.now() - timedelta(days=30))
    & (customers["interested_categories"].str.contains("streetwear"))
]

# Create email content
email_content = """
Subject: Exclusive Preview of Our New Streetwear Collection

Hi {name},

We're excited to give you an exclusive preview of our latest streetwear collection. As a valued customer, we wanted you to be the first to see these fresh designs.

[Insert collection images and details]

Use code STREET20 for 20% off your first purchase of the new collection.

Best,
[Your Brand Name]
"""

# Send emails (simulated)
for index, row in segment.iterrows():
    print(email_content.format(name=row["name"]))
