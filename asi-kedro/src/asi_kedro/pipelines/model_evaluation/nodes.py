"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.4
"""
import h5py
import pandas as pd
from sklearn.metrics import f1_score, recall_score
from tensorflow.python.keras.engine.sequential import Sequential
import wandb


def evaluate_model(predictor, test_data):
    results = predictor.evaluate(test_data)

    # Logowanie wyników ewaluacji do W&B
    wandb.log({"evaluation_results": results})

    return results


def compare_and_select_best_model(evaluation_results, predictor):
    best_model = predictor  # Assuming only one model for simplicity
    best_score = evaluation_results['accuracy']  # Assuming accuracy is the evaluation metric

    wandb.log({"best_model": best_model})

    # Zapisanie najlepszego modelu do pliku .h5
    best_model_path = "best_model.h5"

    # Używamy h5py do zapisywania modelu w formacie .h5
    with h5py.File(best_model_path, "w") as h5file:
        for key, value in predictor.info().items():
            if isinstance(value, (int, float, str, list, dict)):
                h5file.attrs[key] = value
            elif isinstance(value, pd.DataFrame):
                for col in value.columns:
                    h5file.create_dataset(f"{key}_{col}", data=value[col].values)
            else:
                pass  # Skipping any non-serializable attributes

    return best_model_path
