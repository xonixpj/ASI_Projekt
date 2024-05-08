"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs={"predictor": "predictor", "test_data": "test_data"},
            outputs="evaluation_results",
            name="evaluate_model_node",
        ),
    ])
