"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.4
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load_data, split_data, process_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_data,
            inputs=None,
            outputs="data",
            name="load_data_node",
        ),
        node(
            func=process_data,
            inputs='data',
            outputs='processedData',
            name='process_data',
        ),
        node(
            func=split_data,
            inputs='data',
            outputs=['train_data','test_data'],
            name='split_data_node',
        ),
    ])
