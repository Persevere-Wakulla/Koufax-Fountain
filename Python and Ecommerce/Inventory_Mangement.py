"""Inventory Management: Python can help automate inventory tracking, forecasting, and reordering processes, ensuring you never run out of popular items or overstock on slow sellers.
    """

import pandas as pd

# Load current inventory
inventory = pd.read_csv("inventory.csv")


# Update stock levels
def update_inventory(sku, quantity):
    if sku in inventory["sku"].values:
        inventory.loc[inventory["sku"] == sku, "stock"] += quantity
    else:
        new_item = pd.DataFrame({"sku": [sku], "stock": [quantity]})
        inventory = pd.concat([inventory, new_item], ignore_index=True)
    inventory.to_csv("updated_inventory.csv", index=False)


# Example usage
update_inventory("SW123", 50)
