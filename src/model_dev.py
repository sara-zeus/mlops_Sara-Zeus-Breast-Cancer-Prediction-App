from abc import ABC, abstractmethod
from sklearn.linear_model import LogisticRegression
import logging


class Model(ABC):
    """Abstract class for model"""

    @abstractmethod
    def train(self, x_train, y_train):
        pass


class LogisticRegressionModel(Model):
    """Logistic Regression Model"""

    def train(self, x_train, y_train, **kwargs):
        """Trains the logistic regression model"""
        try:
            logistics = LogisticRegression(**kwargs)
            logistics.fit(x_train, y_train)
            logging.info(f"Model trained successfully")
            return logistics

        except Exception as e:
            logging.error(f"Error in training model: {e}")
            raise e
