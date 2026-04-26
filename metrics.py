from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import numpy as np


y_true = np.array([0, 1, 2, 2, 0, 1])
y_pred = np.array([0, 0, 2, 2, 1, 1])

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')   
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
