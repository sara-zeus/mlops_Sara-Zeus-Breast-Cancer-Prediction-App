from Model_Training_Pipeline import train_model
from Data_Ingestion_Pipeline import ingested_data
from Data_Preprocessing_Pipeline import data_preprocessing_pipeline
from sklearn.metrics import accuracy_score, classification_report


def evaluate_model(model, X_test, y_test):
    # Predict on test set
    y_pred = model.predict(X_test)

    # Print accuracy score and classification report
    print(
        "Accuracy score of the model used for prediction is: ",
        accuracy_score(y_test, y_pred),
    )
    print("Classification report: \n", classification_report(y_test, y_pred))

    return accuracy_score(y_test, y_pred), classification_report(y_test, y_pred)


# Example usage of the Model Evaluation Pipeline
def model_evaluation_pipeline(trained_model, X_test, y_test):
    # Step 1: Evaluate the trained model
    accuracy, report = evaluate_model(trained_model, X_test, y_test)

    # Step 2: Print evaluation metrics
    print(f"Accuracy: {accuracy}")
    print("Classification Report:\n", report)

    # Additional steps can be added like saving the evaluation results, visualization, etc.


# Assuming 'trained_model', 'X_test', 'y_test' are available from previous steps
if __name__ == "__main__":
    # Your trained model, test data (X_test), and corresponding labels (y_test)
    # Replace these placeholders with your actual data

    # Assuming you have trained_model, X_test, y_test available from your training step

    # Evaluate the trained model using the test data
    processed_data = data_preprocessing_pipeline(ingested_data)
    scaled_data, X_train, X_test, y_train, y_test = processed_data

    # Train the model
    trained_model = train_model(X_train, y_train)

    # Evaluate the model using the evaluation pipeline
    model_evaluation_pipeline(trained_model, X_test, y_test)
