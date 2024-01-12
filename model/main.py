import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle as pkl


def create_model(data):
    """Creates model from data"""

    X = data.drop(["diagnosis"], axis=1)
    y = data["diagnosis"]

    # Scaling the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Splitting the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Training the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Predicting the test set results and calculating accuracy score for the model used for prediction
    y_pred = model.predict(X_test)
    print(
        "Accuracy score of the model used for prediction is: ",
        accuracy_score(y_test, y_pred),
    )
    print("Classification report: \n", classification_report(y_test, y_pred))

    # Training the XGBoost model
    xgb_model = xgb.XGBClassifier()
    xgb_model.fit(X_train, y_train)

    # Predicting using the XGBoost model
    y_pred_xgb = xgb_model.predict(X_test)
    print(
        "Accuracy score of the XGBoost model is: ",
        accuracy_score(y_test, y_pred_xgb),
    )
    print(
        "Classification report for XGBoost model: \n",
        classification_report(y_test, y_pred_xgb),
    )


    return model, scaler, xgb_model


def get_clean_data():
    """Gets clean data from data.csv file"""
    data = pd.read_csv("/Users/yasara/Desktop/o/data/data.csv")
    data = data.drop(["Unnamed: 32", "id"], axis=1)
    data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})
    # print(data.head())

    return data


def main():
    """Runs main script"""
    data = get_clean_data()

    model, scaler, xgb_model = create_model(data)

    with open("model/model.pkl", "wb") as f:
        pkl.dump(model, f)
    with open("model/scaler.pkl", "wb") as f:
        pkl.dump(scaler, f)
    with open("model/xgb_model.pkl", "wb") as f:
        pkl.dump(xgb_model, f)



if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
