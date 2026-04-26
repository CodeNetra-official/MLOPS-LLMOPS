import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier

np.random.seed(45)
n = 1000
X = pd.DataFrame({
    "age" : np.random.randint(18, 70, n),
    # "income" : np.random.randint(30000, 100000, n),
    "experience" : np.random.randint(0, 40, n),
    "noise1" : np.random.rand(n),
    "noise2" : np.random.rand(n),
})
y = np.random.choice([0, 1], n)  # Binary target variable

selector = SelectKBest(score_func=f_classif, k=3)
X_best = selector.fit_transform(X, y)
selected_features = selector.get_support(indices=True)
print("Selected feature indices:", selected_features)


rf = RandomForestClassifier(n_estimators=500, random_state=45)
rf.fit(X, y)
feature_importances = rf.feature_importances_
print("Feature importances from Random Forest:", feature_importances)
feature_names = X.columns
feature_importance_df = pd.DataFrame({
    "feature": feature_names,
    "importance": feature_importances
}).sort_values(by="importance", ascending=False)
print("Feature importances from Random Forest:")
print(feature_importance_df.head(3))

final_data = X[feature_importance_df["feature"].head(3).values]
print("Final dataset with selected features:")
print(final_data.head())
# print(y)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=10.0, max_iter=100)
model.fit(final_data, y)
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)


y_pred = model.predict(final_data)
print("Predictions:", y_pred)

y_true = y
print("True labels:", y_true)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)