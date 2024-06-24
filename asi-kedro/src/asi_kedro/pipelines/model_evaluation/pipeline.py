from kedro.pipeline import Pipeline, node
from ..model_evaluation.nodes import evaluate_model, load_test_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(load_test_data, inputs=None, outputs="test_data", name="load_test_data_node"),
        node(evaluate_model, inputs={"predictor": "predictor", "test_data": "test_data"}, outputs="evaluation_results", name="evaluate_model_node"),
    ])
