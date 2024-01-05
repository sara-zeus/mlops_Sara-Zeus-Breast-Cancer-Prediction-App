import pandas as pd


def ingest_data(file_path):
    # Read the CSV file directly
    ingested_data = pd.read_csv(file_path)

    # Perform any necessary data preprocessing or validation here

    return ingested_data


# Example usage
file_to_ingest = "/Users/yasara/Desktop/o/data/data.csv"
ingested_data = ingest_data(file_to_ingest)
print(ingested_data.head())
