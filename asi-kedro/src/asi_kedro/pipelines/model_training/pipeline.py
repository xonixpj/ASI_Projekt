from kedro.pipeline import Pipeline, node
from ..model_training.nodes import train_model, load_train_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(load_train_data, inputs=None, outputs="train_data", name="load_train_data_node"),
        node(train_model, inputs="train_data", outputs="predictor", name="train_model_node"),
    ])
