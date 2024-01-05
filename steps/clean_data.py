import logging
import pandas as pd
from zenml import step
from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreProcessStrategy
from typing_extensions import Annotated
from typing import Tuple


@step
def clean_data(
    df: pd.DataFrame,
) -> Tuple[
    Annotated[pd.DataFrame, "x_train"],
    Annotated[pd.DataFrame, "x_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    """Cleans data and divides it into train and test sets
    Args:
        df: Input data
        Returns:
            x_train: Training data
            x_test: Testing data
            y_train: Training labels
            y_test: Testing labels"""

    try:
        process_strategy = DataPreProcessStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy()
        data_cleaning = DataCleaning(processed_data, divide_strategy)
        x_train, x_test, y_train, y_test = data_cleaning.handle_data()
        logging.info(f"Data divided into train and test sets")
        return x_train, x_test, y_train, y_test

    except Exception as e:
        logging.error(f"Error in data cleaning: {e}")
        raise e
