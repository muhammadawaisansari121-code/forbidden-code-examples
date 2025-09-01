import pandas as pd
from sklearn.metrics import confusion_matrix

# Sample dataset with demographic bias
data = {
    "applicant_id": [1, 2, 3, 4, 5, 6],
    "gender": ["M", "F", "M", "F", "M", "F"],
    "approved": [1, 0, 1, 0, 1, 0],  # 1 = approved, 0 = denied
    "prediction": [1, 0, 1, 1, 1, 0] # Model predictions
}
df = pd.DataFrame(data)
print(df)
