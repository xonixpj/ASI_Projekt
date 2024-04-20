import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


def process_data():
    data = pd.read_csv('./Data/weatherAUS.csv')
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
