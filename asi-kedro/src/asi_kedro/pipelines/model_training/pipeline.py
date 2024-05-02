"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, pipeline, node

from ..data_processing.nodes import load_data, process_data, split_data
from ..model_evaluation.nodes import evaluate_model
from .nodes import train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs=None,
            outputs='raw_data',
            name='load_data',
        ),
        node(
            func=process_data,
            inputs='raw_data',
            outputs=['X', 'y'],
            name='process_data',
        ),
        node(
            func=split_data,
            inputs=['X', 'y'],
            outputs=['X_train', 'X_test', 'y_train', 'y_test'],
            name='split_data',
        ),
        node(
            func=train_model,
            inputs=['X_train', 'y_train'],
            outputs='model',
            name='train_model',
        ),
        node(
            func=evaluate_model,
            inputs=['model', 'X_test', 'y_test'],
            outputs='model_metrics',
            name='evaluate_model',
        )
    ])
