import json

# from .utils import get_data_for_test
import os

import numpy as np
import pandas as pd

# from materializer.custom_materializer import cs_materializer
from steps.clean_data import clean_data
from steps.evaluation import evaluate_model
from steps.ingest_data import ingest_data
from steps.model_train import train_model
from zenml import pipeline, step
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW, TENSORFLOW
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)
from zenml.integrations.mlflow.services import MLFlowDeploymentService
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
from zenml.steps import BaseParameters, Output

# from .utils import get_data_for_test

docker_settings = DockerSettings(required_integrations=[MLFLOW])


class Deployment_trigger_config(BaseParameters):
    min_accuracy: float = 0.92


@step
def Deployment_trigger(accuracy: float, config: Deployment_trigger_config):
    return accuracy >= config.min_accuracy


@pipeline(enable_cache=True, settings={"docker": docker_settings})
def continuous_deployment_pipeline(
    min_accuracy: float = 0.92,
    workers: int = 1,
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
):
    df = ingest_data()
    x_train, x_test, y_train, y_test = clean_data(df)
    model = train_model(x_train, x_test, y_train, y_test)
    ACCURACY, PRECISION, RECALL = evaluate_model(model, x_test, y_test)
    Deployment_Decision = Deployment_trigger(ACCURACY)
    mlflow_model_deployer_step(
        model=model,
        deploy_decision=Deployment_Decision,
        workers=workers,
        timeout=timeout,
    )
