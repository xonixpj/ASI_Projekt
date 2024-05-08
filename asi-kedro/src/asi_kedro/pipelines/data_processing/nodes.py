"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.4
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from autogluon.tabular import TabularDataset, TabularPredictor


def load_data():
    data_url = '../data/weatherAUS.csv'
    data = TabularDataset(data_url)
    return data

def process_data(data: pd.DataFrame):
    # Usuń wiersze z niezdefiniowanymi etykietami
    data = data.dropna(subset=['RainTomorrow'])

    # Wypełnij brakujące wartości
    data = data.fillna(-1)

    # Usuń wiersze, w których wszystkie wartości są niezdefiniowane
    data = data.dropna(how='all')

    # Zakoduj kolumny obiektów
    le = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column] = le.fit_transform(data[column].astype(str))

    # Skaluj kolumny zmiennoprzecinkowe
    scaler = MinMaxScaler()
    for column in data.columns:
        if data[column].dtype == np.float64:
            data[column] = scaler.fit_transform(data[column].values.reshape(-1, 1))

    return data
def split_data(processedData: pd.DataFrame):
    train_data, test_data = train_test_split(processedData, test_size=0.2, random_state=42)

    return train_data, test_data