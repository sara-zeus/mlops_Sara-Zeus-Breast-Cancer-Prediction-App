import logging
import pandas as pd
from zenml import step

data_path = "data/data.csv"


class IngestData:
    """Ingest data from a csv file into a pandas dataframe."""

    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Reading data from {self.data_path}")
        df = pd.read_csv(self.data_path)
        return df


@step
def ingest_data(data_path: str) -> pd.DataFrame:
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error ingesting data: {e}")
        raise e


import logging
import pandas as pd
from zenml import step

data_path = "data/data.csv"


class IngestData:
    """Ingest data from a csv file into a pandas dataframe."""

    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self):
        logging.info(f"Reading data from {self.data_path}")
        df = pd.read_csv(self.data_path)
        return df


@step
def ingest_data(data_path: str) -> pd.DataFrame:
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error ingesting data: {e}")
        raise e
