from pipelines.training_pipelines import training_pipeline
from zenml.client import Client

if __name__ == "main":
    print(Client.activate_stack.experiment_tracker.get_tracking_uri())
    training_pipeline(data_path="data/data.csv")
