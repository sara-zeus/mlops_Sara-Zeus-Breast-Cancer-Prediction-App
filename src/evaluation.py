import logging
from abc import ABC, abstractmethod
import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report,
)
from sklearn.linear_model import LogisticRegression


class Evaluation(ABC):
    """Abstract class for evaluation of models."""

    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        """Calculates scores of the model.
        Args:
           y_true: true labels
           y_pred: predicted labels
           Returns:
            scores: None"""
        pass


class accuracy(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("calculating accuracy score")
            accuracy = accuracy_score(y_true, y_pred)
            logging.info("accuracy score calculated to be: %s", accuracy)
            return accuracy

        except Exception as e:
            logging.error("error calculating accuracy score: %s", e)
            raise e


class precision(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("calculating precision score")
            precision = precision_score(y_true, y_pred)
            logging.info("precision score calculated to be: %s", precision)
            return precision

        except Exception as e:
            logging.error("error calculating precision score: %s", e)
            raise e


class recall(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            logging.info("calculating recall score")
            recall = recall_score(y_true, y_pred)
            logging.info("recall score calculated to be: %s", recall)
            return recall

        except Exception as e:
            logging.error("error calculating recall score: %s", e)
            raise e


# class classif_report(Evaluation):
#     def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
#         try:
#             logging.info("calculating classification report")
#             classification_report = classification_report(y_true, y_pred)
#             logging.info(
#                 "classification report calculated to be: %s", classification_report
#             )
#             return classification_report

#         except Exception as e:
#             logging.error("error calculating classification report: %s", e)
#             raise e
