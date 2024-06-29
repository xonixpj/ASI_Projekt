from kedro.pipeline import Pipeline, node
from .nodes import evaluate_model, load_test_data, load_predictor, compare_and_select_best_model

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(load_test_data, inputs=None, outputs="test_data", name="load_test_data_node"),
        node(load_predictor, inputs="predictor_path", outputs="predictor", name="load_predictor_node"),
        node(evaluate_model, inputs={"predictor": "predictor", "test_data": "test_data"}, outputs="evaluation_results", name="evaluate_model_node"),
        node(compare_and_select_best_model, inputs={"evaluation_results": "evaluation_results", "predictor": "predictor"}, outputs="best_model_path", name="compare_and_select_best_model_node"),
    ])
