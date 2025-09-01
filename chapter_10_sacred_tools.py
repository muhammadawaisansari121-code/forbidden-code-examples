import pandas as pd
from sklearn.metrics import accuracy_score
# Example: fairness check across groups
def group_accuracy(y_true, y_pred, group_labels):
    results = {}
    for group in set(group_labels):
        mask = (group_labels == group)
        acc = accuracy_score(y_true[mask], y_pred[mask])
        results[group] = acc
    return results
# Simulated example
y_true = pd.Series([1,0,1,0,1,0])
y_pred = pd.Series([1,0,0,0,1,1])
groups = pd.Series(['A','A','B','B','B','A'])
print("Accuracy by group:", group_accuracy(y_true, y_pred, groups))
