import logging
import pandas as pd
from zenml import step

from src.model_dev import LogisticRegression
from sklearn.base import ClassifierMixin
from .config import ModelNameConfig


@step
def train_model(
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    config: ModelNameConfig,
) -> ClassifierMixin:
    try:
        model = None
        if config.model_name == "LogisticRegression":
            model = LogisticRegression()
            trained_model = model.train(x_train, y_train)
            return trained_model
        else:
            raise ValueError(f"Model {config.model_name} not supported")

    except Exception as e:
        logging.error(f"Error in training model: {e}")
        raise e
