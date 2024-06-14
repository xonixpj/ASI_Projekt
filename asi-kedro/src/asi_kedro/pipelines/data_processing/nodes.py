import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from autogluon.tabular import TabularDataset
import wandb

def load_data():
    data_url = '../data/weatherAUS.csv'
    data = TabularDataset(data_url)
    return data

def process_data(data: pd.DataFrame):
    data = feature_engineering(data)

    le = LabelEncoder()
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column] = le.fit_transform(data[column].astype(str))

    scaler = MinMaxScaler()
    for column in data.columns:
        if data[column].dtype == np.float64:
            data[column] = scaler.fit_transform(data[column].values.reshape(-1, 1))

    return data

def split_data(processedData: pd.DataFrame):
    train_data, test_data = train_test_split(processedData, test_size=0.2, random_state=42)
    return train_data, test_data

def feature_engineering(data: pd.DataFrame):
    data = data.dropna(subset=['RainTomorrow'])
    data = data.fillna(-1)
    data = data.dropna(how='all')
    return data
