"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load_data, process_data, split_data


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
    ])
