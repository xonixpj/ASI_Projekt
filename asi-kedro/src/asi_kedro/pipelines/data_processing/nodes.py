"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.4
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


def load_data():
    data = pd.read_csv('data/weatherAUS.csv')

    return data

def process_data(data: pd.DataFrame):
    data = data.fillna(-1)
    data = data.dropna(how='all')

    le = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column] = le.fit_transform(data[column].astype(str))

    scaler = MinMaxScaler()
    for column in data.columns:
        if data[column].dtype == np.float64:
            data[column] = scaler.fit_transform(data[column].values.reshape(-1, 1))

    X = data.drop('RainTomorrow', axis=1)
    y = data['RainTomorrow']

    return X, y

def split_data(X: pd.DataFrame, y: pd.Series):
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test