import logging
import pandas as pd
from zenml import step
from typing import Tuple
from typing_extensions import Annotated

from sklearn.base import ClassifierMixin
from src.evaluation import accuracy, precision, recall


@step
def evaluate_model(
    model: ClassifierMixin, x_test: pd.DataFrame, y_test: pd.DataFrame
) -> Tuple[
    Annotated[float, "ACCURACY"],
    Annotated[float, "PRECISION"],
    Annotated[float, "RECALL"],
]:
    """Evaluate the model on the test set.
    Args:
        ingested data"""
    try:
        prediction = model.predict(x_test)
        accuracy_class = accuracy()
        ACCURACY = accuracy_class.calculate_scores(y_test, prediction)

        precision_class = precision()
        PRECISION = precision_class.calculate_scores(y_test, prediction)

        recall_class = recall()
        RECALL = recall_class.calculate_scores(y_test, prediction)

        return ACCURACY, PRECISION, RECALL

    except Exception as e:
        logging.error("error evaluating model: %s", e)
        raise e
