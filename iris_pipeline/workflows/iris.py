import os
from typing import Tuple

import mlflow

from flytekit import task, workflow


@task
def train_model() -> Tuple[str, str]:
    """
    Train a RandomForestClassifier on the Iris dataset and log it into Mlflow.

    Returns:
        run_id (str): the id of the mlflow run
        artifact_uri (str): the blob storage uri of the model artifact
    """
    
    return "tmp", "tmp"
    


@task
def deploy_model(run_id: str, model_uri: str) -> str:
    """
    Deploy the model saved at model_uri with seldon core.

    Args:
        run_id (str): the Mlflow run id of the training run for which the model is deployed
        model_uri (str): the blob storage uri of the model artifact to be deployed

    Returns:
        endpoint_uri (str): the path of the deployed model endpoint.
    """
    
    return "endpoint_uri"
    


@workflow
def train_and_deploy_iris_model() -> str:
    run_id, model_artifact_uri = train_model()
    endpoint_uri = deploy_model(run_id=run_id, model_uri=model_artifact_uri)
    
    return endpoint_uri
