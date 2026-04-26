import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

"""

Problem statement: We want to analyze customer churn data to understand the factors that contribute to customers leaving a service. We will perform exploratory data analysis (EDA) on a synthetic dataset, train a logistic regression model, and evaluate its performance.
Dataset: The dataset contains 1000 samples with the following features:
- age: The age of the customer (integer between 18 and 70)
- income: The annual income of the customer (integer between 30,000 and 100,000)
- experience: The number of years the customer has been with the service (integer between
0 and 40)
- churned: A binary target variable indicating whether the customer has churned (1) or
EDA
FEATURE ENGINEERING
model training
evaluation


"""





np.random.seed(45)

def load_data():

    data = {
    "age" : np.random.randint(18, 70, 1000),
    "income" : np.random.randint(30000, 100000, 1000),
    "experience" : np.random.randint(0, 40, 1000),
    "churned" : np.random.choice([0, 1], 1000, p=[0.7, 0.3])
    }

    df = pd.DataFrame(data)
    df.to_csv("customer_churn.csv", index=False)
    return df

def perform_eda(df):

    if df.endswith(".csv"):
        df = pd.read_csv(df)


    x = df.drop("churned", axis=1)
    y = df["churned"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=45)

    print("Shape of training data:", x_train.shape)
    print("Shape of testing data:", x_test.shape)
    print("Shape of training labels:", y_train.shape)
    print("Shape of testing labels:", y_test.shape)

    print("Class distribution in training set:")
    print(y_train.value_counts())
    print("Class distribution in testing set:") 
    print(y_test.value_counts())

    return x_train, x_test, y_train, y_test

def train_model(x_train, y_train):
    model = LogisticRegression(C=1.0, max_iter=1000)
    model.fit(x_train, y_train)
    return model

def save_model(model, filename="logistic_regression_model.pkl"):
    import joblib
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

def evaluate_model(model, x_test, y_test):
    accuracy = model.score(x_test, y_test)
    print("Model accuracy on test set:", accuracy)


if __name__ == "__main__":
    # df = load_data()
    x_train, x_test, y_train, y_test = perform_eda("customer_churn.csv")
    model = train_model(x_train, y_train)
    save_model(model)
    evaluate_model(model, x_test, y_test)
    # print("Model trained successfully!")

