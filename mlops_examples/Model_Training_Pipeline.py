from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle as pkl

from sklearn.linear_model import LogisticRegression
from Data_Preprocessing_Pipeline import data_preprocessing_pipeline
from Data_Preprocessing_Pipeline import data_preprocessing_pipeline
from Data_Ingestion_Pipeline import ingested_data


def train_model(X_train, y_train):
    # Initialize the model (Example: LogisticRegression)
    model = LogisticRegression()

    # Train the model
    model.fit(X_train, y_train)

    return model


# def evaluate_model(model, X_test, y_test):
#     # Predict on test set
#     y_pred = model.predict(X_test)

#     # Print accuracy score and classification report
#     print(
#         "Accuracy score of the model used for prediction is: ",
#         accuracy_score(y_test, y_pred),
#     )
#     print("Classification report: \n", classification_report(y_test, y_pred))

#     return model, accuracy_score(y_test, y_pred), classification_report(y_test, y_pred)


def save_model(model, file_path):
    # Save the trained model using pickle
    with open(file_path, "wb") as f:
        pkl.dump(model, f)


# Example usage of the Model Training Pipeline
def model_training_pipeline(X_train, X_test, y_train, y_test, model_save_path):
    # Step 1: Train the model
    trained_model = train_model(X_train, y_train)

    # Step 2: Evaluate the model (Optional)
    # accuracy, report = evaluate_model(trained_model, X_test, y_test)
    # print(f"Accuracy: {accuracy}")
    # print("Classification Report:\n", report)

    # Step 3: Save the trained model


# Assuming 'X_train', 'X_test', 'y_train', 'y_test' are available from previous steps

if __name__ == "__main__":
    # Your data ingestion pipeline should provide 'ingested_data'
    # Replace with your ingested data

    # Perform data preprocessing using the imported function
    processed_data = data_preprocessing_pipeline(ingested_data)
    scaled_data, X_train, X_test, y_train, y_test = processed_data

    # Define model save path
    model_save_path = "trained_model.pkl"

    # Using preprocessed data for training
    trained_model = train_model(X_train, y_train)

    # Save the trained model
    save_model(trained_model, model_save_path)

    # Evaluate the model
    # model, accuracy, report = evaluate_model(trained_model, X_test, y_test)

    # Print accuracy and classification report
    # print(f"Accuracy: {accuracy}")
    # print("Classification Report:\n", report)
