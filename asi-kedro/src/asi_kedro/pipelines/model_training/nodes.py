"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.4
"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from autogluon.tabular import TabularPredictor


def train_model(train_data):
    # Usuń wiersze z niezdefiniowanymi etykietami
    train_data = train_data.dropna(subset=['RainTomorrow'])

    predictor = TabularPredictor(label='RainTomorrow', problem_type='binary').fit(train_data)
    return predictor
