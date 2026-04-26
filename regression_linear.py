from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier


import numpy as np


X = np.array([[1], [2], [3], [4], [5]])

#-- Linear Regression
#-------------------------------------------------------------
y_reg = np.array([2.5, 3.5, 4.5, 5.5, 6.5])  # Linear relationship with some noise continuos, decimals
reg_model = LinearRegression()
reg_model.fit(X, y_reg)
print("Linear Regression Coefficients:", reg_model.coef_)
print("Linear Regression Intercept:", reg_model.intercept_)
print("prediction :", reg_model.predict([[6]]))  # Predicting for a new value


#-- Decision Tree Classifier
#-------------------------------------------------------------
y_clf = np.array([0, 0, 1, 1, 1])  # Binary classification labels decreate
clf_model = DecisionTreeClassifier()
clf_model.fit(X, y_clf)
print("Decision Tree Classifier Feature Importances:", clf_model.feature_importances_)
print("prediction :", clf_model.predict([[6]]))  # Predicting for a new value   
print("prediction probabilities:", clf_model.predict_proba([[6]]))  # Predicting probabilities for a new value


