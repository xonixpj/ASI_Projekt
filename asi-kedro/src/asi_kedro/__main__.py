from kedro.framework.context import KedroContext, KedroContextError
from kedro.pipeline import Pipeline
from kedro.framework.hooks import hook_impl
from kedro.runner import SequentialRunner

from .pipelines.data_processing.pipeline import create_pipeline as data_processing_pipeline
from .pipelines.model_training.pipeline import create_pipeline as model_training_pipeline
from .pipelines.model_evaluation.pipeline import create_pipeline as model_evaluation_pipeline

class ProjectContext(KedroContext):

    project_name = "weather-prediction"
    project_version = "0.19.4"

    def _get_pipelines(self) -> dict:
        data_processing = data_processing_pipeline()
        model_training = model_training_pipeline()
        model_evaluation = model_evaluation_pipeline()

        return {
            "data_processing": data_processing,
            "model_training": model_training,
            "model_evaluation": model_evaluation,
            "__default__": data_processing + model_training + model_evaluation
        }

if __name__ == "__main__":
    project_context = ProjectContext("weather-prediction")
    runner = SequentialRunner()
    runner.run(project_context)
