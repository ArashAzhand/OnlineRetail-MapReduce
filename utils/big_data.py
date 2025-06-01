import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import timedelta

# Load original dataset
df = pd.read_csv("Online_Retail_Clean.csv", encoding='ISO-8859-1')

# Initialize Faker and config
faker = Faker()
multiplier = 10  # Adjust this for final size (100 ~ 800MB if original has ~8K rows)

# Clean and prepare base data
df = df.dropna(subset=['CustomerID'])
df = df[df['Quantity'] > 0]

# Expand data
expanded_rows = []
for i in range(multiplier):
    temp = df.copy()

    # Randomize InvoiceNo
    temp['InvoiceNo'] = temp['InvoiceNo'].apply(lambda x: f"{random.randint(100000,999999)}")

    # Randomize InvoiceDate (within a 1-year window)
    base_date = pd.to_datetime('2023-01-01')
    temp['InvoiceDate'] = temp['InvoiceDate'].apply(
        lambda x: base_date + timedelta(days=random.randint(0, 364), seconds=random.randint(0, 86400))
    )

    # Slight variations in Quantity and UnitPrice
    temp['Quantity'] = temp['Quantity'].apply(lambda q: max(1, int(q * np.random.uniform(0.8, 1.2))))
    temp['UnitPrice'] = temp['UnitPrice'].apply(lambda p: round(p * np.random.uniform(0.9, 1.1), 2))

    # Shuffle CustomerID
    temp['CustomerID'] = temp['CustomerID'].apply(lambda x: int(x) + random.randint(1000, 9999))

    # Optionally randomize Country
    countries = df['Country'].unique()
    temp['Country'] = temp['Country'].apply(lambda x: random.choice(countries))

    expanded_rows.append(temp)

# Combine all
big_df = pd.concat(expanded_rows, ignore_index=True)

# Save to CSV (this can be large!)
big_df.to_csv("OnlineRetail_Large.csv", index=False)

print("✅ Large dataset generated:", big_df.shape)