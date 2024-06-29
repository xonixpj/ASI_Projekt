from autogluon.tabular import TabularPredictor
import wandb
import sqlite3
import pandas as pd
import pickle

def load_train_data():
    conn = sqlite3.connect('weatherAUS.db')
    query = "SELECT * FROM train_data"
    train_data = pd.read_sql(query, conn)
    conn.close()
    return train_data

def train_model(train_data):
    train_data = train_data.dropna(subset=['RainTomorrow'])

    wandb.init(project='weather-prediction')

    # Trening modelu
    predictor = TabularPredictor(label='RainTomorrow', problem_type='binary').fit(train_data)

    # Wyodrębnienie metryk do logowania
    predictor_info = predictor.info()

    loggable_info = {
        'num_features': predictor_info.get('num_features'),
        'num_rows': predictor_info.get('num_rows'),
        'num_classes': predictor_info.get('num_classes'),
        'problem_type': predictor_info.get('problem_type'),
        'eval_metric': predictor_info.get('eval_metric'),
        'best_model': predictor_info.get('best_model'),
        'hyperparameters': predictor_info.get('hyperparameters'),
        'fit_time': predictor_info.get('fit_time'),
        'leaderboard': predictor_info['leaderboard'].to_dict() if 'leaderboard' in predictor_info else None
    }

    # Usunięcie kluczy z wartością None
    loggable_info = {k: v for k, v in loggable_info.items() if v is not None}

    # Logowanie metryk
    wandb.log(loggable_info)

    # Zapisujemy model do pliku .pkl
    with open("../ml_models/predictor.pkl", "wb") as f:
        pickle.dump(predictor, f)

    return "../ml_models/predictor.pkl"
