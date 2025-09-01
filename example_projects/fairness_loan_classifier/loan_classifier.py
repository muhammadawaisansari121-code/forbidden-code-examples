import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from fairlearn.metrics import MetricFrame, selection_rate, demographic_parity_difference

# Sample dataset
data = pd.DataFrame({
    "income": [50, 40, 60, 80, 30, 45, 70, 65],
    "gender": ["M", "F", "M", "M", "F", "F", "M", "F"],
    "approved": [1, 0, 1, 1, 0, 0, 1, 0]
})

X = data[["income"]]
y = data["approved"]
gender = data["gender"]

# Split data
X_train, X_test, y_train, y_test, g_train, g_test = train_test_split(X, y, gender, test_size=0.3, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Fairness metrics
mf = MetricFrame(metrics={"accuracy": accuracy_score, "selection_rate": selection_rate},
                 y_true=y_test, y_pred=y_pred, sensitive_features=g_test)

print("Group-wise metrics:")
print(mf.by_group)

dpd = demographic_parity_difference(y_test, y_pred, sensitive_features=g_test)
print("Demographic parity difference:", dpd)
