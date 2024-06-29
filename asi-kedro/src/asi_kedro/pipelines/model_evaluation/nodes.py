import pickle
import sqlite3
import pandas as pd
from sklearn.metrics import f1_score, recall_score
import wandb

def load_test_data():
    conn = sqlite3.connect('weatherAUS.db')
    query = "SELECT * FROM test_data"
    test_data = pd.read_sql(query, conn)
    conn.close()
    return test_data

def load_predictor(predictor_path):
    with open(predictor_path, "rb") as f:
        predictor = pickle.load(f)
    return predictor

def evaluate_model(predictor, test_data):
    # Usuń wiersze z brakującymi wartościami w kolumnie RainTomorrow
    test_data = test_data.dropna(subset=['RainTomorrow'])

    results = predictor.evaluate(test_data)
    wandb.log({"evaluation_results": results})
    return results

def compare_and_select_best_model(evaluation_results, predictor):
    best_model = predictor  # Assuming only one model for simplicity
    best_score = evaluation_results['accuracy']  # Assuming accuracy is the evaluation metric

    wandb.log({"best_model_score": best_score})

    # Zapisanie najlepszego modelu do pliku .pkl
    best_model_path = "../ml_models/model.pkl"

    # Zapisujemy model w formacie .pkl
    with open(best_model_path, "wb") as f:
        pickle.dump(best_model, f)

    return best_model_path
