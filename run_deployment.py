from typing import cast

import click
from pipelines.deployment_pipeline import continuous_deployment_pipeline
from rich import print
from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer,
)
from zenml.integrations.mlflow.services import MLFlowDeploymentService

DEPLOY = "deploy"
PREDICT = "predict"
DEPLOY_AND_PREDICT = "deploy_and_predict"


@click.command()
@click.option(
    "--config",
    "-c",
    type=click.Choice([DEPLOY, PREDICT, DEPLOY_AND_PREDICT]),
    default=DEPLOY_AND_PREDICT,
    help="Optionally you can choose to only run the deployment "
    "pipeline to train and deploy a model (`deploy`), or to "
    "only run a prediction against the deployed model "
    "(`predict`). By default both will be run "
    "(`deploy_and_predict`).",
)
@click.option(
    "--min-accuracy",
    default=0.92,
    help="Minimum accuracy required to deploy the model",
)
def run_deployment(config: str, min_accuracy: float):
    mlflow_model_deployer_component = MLFlowModelDeployer.get_active_model_deployer()
    DEPLOY = config == DEPLOY or config == DEPLOY_AND_PREDICT
    PREDICT = config == PREDICT or config == DEPLOY_AND_PREDICT

    if DEPLOY:
        continuous_deployment_pipeline(
            min_accuracy=min_accuracy, workers=3, timeout=120
        )

        # if PREDICT:
        # inference_pipeline()
        print(
            "You can run:\n "
            f"[italic green]    mlflow ui --backend-store-uri '{get_tracking_uri()}"
            "[/italic green]\n ...to inspect your experiment runs within the MLflow"
            " UI.\nYou can find your runs tracked within the "
            "`mlflow_example_pipeline` experiment. There you'll also be able to "
            "compare two or more runs.\n\n"
        )


if __name__ == "__main__":
    run_deployment()
