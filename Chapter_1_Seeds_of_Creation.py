# Chapter 1: The Seeds of Creation – Data as the Fruit of Eden

import pandas as pd

# Load sample dataset

data = {
    "gender": ["male", "female", "male", "female", "male", "female"],
    "income": [50000, 52000, 48000, 51000, 47000, 53000],
    "loan_approved": [1, 0, 1, 0, 1, 0]}
df = pd.DataFrame(data)

# Calculate approval rates by gender

approval_rates = df.groupby("gender")["loan_approved"].mean()
print(approval_rates)
