import logging
from abc import ABC, abstractmethod
from typing import Union

import numpy as np
import pandas as pd
from pandas.core.api import Series as Series

from sklearn.model_selection import train_test_split


class DataStrategy(ABC):
    """Abstract class for data cleaning strategies"""

    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        pass


class DataPreProcessStrategy(DataStrategy):
    """Data cleaning strategy for pre-processing"""

    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Pre-process data"""
        try:
            data = data.drop(["Unnamed: 32", "id"], axis=1)
            data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})
            return data
        except Exception as e:
            logging.error(f"Error in data pre-processing: {e}")
            raise e


class DataDivideStrategy(DataStrategy):
    """Data cleaning strategy for dividing data into train and test sets"""

    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        try:
            x = data.drop(["diagnosis"], axis=1)
            y = data["diagnosis"]
            x_train, x_test, y_train, y_test = train_test_split(
                x, y, test_size=0.2, random_state=42
            )
            return x_train, x_test, y_train, y_test
        except Exception as e:
            logging.error(f"Error in data dividing: {e}")
            raise e


class DataCleaning:
    """Data cleaning class"""

    def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
        self.data = data
        self.strategy = strategy

    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        """Handle data"""
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error(f"Error in data handling: {e}")
            raise e
