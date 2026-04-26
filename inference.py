import joblib


def load_model(filename="logistic_regression_model.pkl"):
    model = joblib.load(filename)
    print(f"Model loaded from {filename}")
    print("Model coefficients:", model.coef_)
    print("Model intercept:", model.intercept_)
    print("Model parameters:", model.get_params())
    return model

def make_predictions(model, x_test):
    predictions = model.predict(x_test)
    print("Predictions:", predictions)
    return predictions


if __name__ == "__main__":
    model = load_model()
    # Example test data (you can replace this with actual test data)
    x_test = [[25, 50000, 2], [40, 80000, 10]]
    predictions = make_predictions(model, x_test)