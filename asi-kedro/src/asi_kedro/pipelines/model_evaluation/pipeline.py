"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import evaluate_model, compare_and_select_best_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=evaluate_model,
            inputs={"predictor": "predictor", "test_data": "test_data"},
            outputs="evaluation_results",
            name="evaluate_model_node",
        ),
        node(
            func=compare_and_select_best_model,
            inputs={"evaluation_results": "evaluation_results", "predictor": "predictor"},
            outputs="best_model_path",
            name="compare_and_select_best_model_node",
        ),
    ])
