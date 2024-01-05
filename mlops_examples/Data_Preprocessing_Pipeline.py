import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from Data_Ingestion_Pipeline import ingested_data

# Assuming 'data' is the ingested DataFrame from the previous step


def data_cleaning(data):
    # Dropping specified columns ('Unnamed: 32' and 'id')
    cleaned_data = data.drop(["Unnamed: 32", "id"], axis=1)
    return cleaned_data


def feature_encoding(data):
    # Mapping 'M' and 'B' values in 'diagnosis' column to 1 and 0 respectively
    data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})
    return data


def feature_scaling(data):
    # Assuming X contains all features except the target variable
    X = data.drop(["diagnosis"], axis=1)

    # Scaling the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Combining scaled features with the encoded target variable
    scaled_data = pd.DataFrame(X_scaled, columns=X.columns)
    scaled_data["diagnosis"] = data["diagnosis"]

    return scaled_data


def data_splitting(data):
    X = data.drop(["diagnosis"], axis=1)
    y = data["diagnosis"]

    # Splitting scaled features and target variable into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test


def data_preprocessing_pipeline(data):
    # Step 1: Data Cleaning
    cleaned_data = data_cleaning(data)

    # Step 2: Feature Encoding
    encoded_data = feature_encoding(cleaned_data)

    # Step 3: Feature Scaling
    scaled_data = feature_scaling(encoded_data)

    # Step 4: Data Splitting
    X_train, X_test, y_train, y_test = data_splitting(scaled_data)

    return scaled_data, X_train, X_test, y_train, y_test


# Example usage
# Assuming 'ingested_data' is the DataFrame from the previous step
scaled_data, X_train, X_test, y_train, y_test = data_preprocessing_pipeline(
    ingested_data
)


# 'scaled_data' contains the fully preprocessed data ready for model training
# 'X_train', 'X_test', 'y_train', and 'y_test' contain the split data for model evaluation

# 'preprocessed_data' contains the fully preprocessed data ready for model training
# 'train_set' and 'test_set' contain the split data for model evaluation

# Your entire code here...

if __name__ == "__main__":
    print("The entire script has completed the data preprocessing pipeline.")
