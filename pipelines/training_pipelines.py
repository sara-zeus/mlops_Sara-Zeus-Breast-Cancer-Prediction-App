from zenml import pipeline

from steps.ingest_data import ingest_data
from steps.clean_data import clean_data
from steps.model_train import train_model
from steps.evaluation import evaluate_model


@pipeline(enable_cache=False)
def training_pipeline(data_path: str):
    df = ingest_data(data_path)
    x_train, y_train, x_test, y_test = clean_data(df)
    model = train_model(x_train, x_test, y_train, y_test)
    ACCURACY, PRECISION, RECALL = evaluate_model(model, x_test, y_test)
