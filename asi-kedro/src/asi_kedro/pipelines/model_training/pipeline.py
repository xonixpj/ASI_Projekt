"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, pipeline, node

from ..data_processing.nodes import load_data, split_data
from ..model_evaluation.nodes import evaluate_model
from .nodes import train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=train_model,
            inputs="train_data",
            outputs="predictor",
            name="train_model_node",
        ),
    ])
