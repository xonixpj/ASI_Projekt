from kedro.pipeline import Pipeline, node
from ..data_processing.nodes import create_database, load_data, process_data, split_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(create_database, inputs=None, outputs="db_creation_status", name="create_database_node"),
        node(load_data, inputs=None, outputs="data", name="load_data_node"),
        node(process_data, inputs="data", outputs="processed_data", name="process_data_node"),
        node(split_data, inputs="processed_data", outputs="split_data_status", name="split_data_node"),
    ])
