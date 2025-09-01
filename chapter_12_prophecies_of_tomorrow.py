import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, KFold
train_test_split
from sklearn.ensemble import RandomForestClassifier
RandomForestClassifier
# Sample dataset with bias risk: gender bias in loan approvals
data = pd.DataFrame({
    "income": [40000, 50000, 60000, 35000, 80000, 90000],
"age": [22, 35, 45, 23, 40, 55],
"gender": ["M", "F", "M", "F", "M", "F"],
"approved": [1, 1, 1, 0, 1, 0]
})
# Encode gender
# Correct assignment
data["gender_encoded"] = data["gender"].map({"M": 0, "F": 1})
X = data[["income", "age", "gender_encoded"]]
y = data["approved"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# Basic accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
# Fairness check: group approval rates
grouped = pd.DataFrame({"gender": 
X_test["gender_encoded"], "approved": y_pred})
print("Approval rates by gender:")
print(grouped.groupby("gender")["approved"].mean())
