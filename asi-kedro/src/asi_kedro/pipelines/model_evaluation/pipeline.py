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
            inputs=['model', 'X_test', 'y_test'],
            outputs='model_metrics',
            name='evaluate_model',
        )
    ])
