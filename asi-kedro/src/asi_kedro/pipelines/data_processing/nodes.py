import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import sqlite3
import wandb


def create_database():
    # Połącz się z bazą danych SQLite (tworzy nową bazę danych, jeśli nie istnieje)
    conn = sqlite3.connect('weatherAUS.db')
    data_url = '../data/weatherAUS.csv'

    # Wczytaj dane z CSV
    data = pd.read_csv(data_url)

    # Zapisz dane do tabeli w bazie danych SQLite
    data.to_sql('weather', conn, if_exists='replace', index=False)

    conn.close()
    return "Database created successfully"


def load_data():
    # Połącz się z bazą danych SQLite
    conn = sqlite3.connect('weatherAUS.db')
    query = "SELECT * FROM weather"

    # Wczytaj dane z tabeli do DataFrame
    data = pd.read_sql(query, conn)

    conn.close()
    return data


def process_data(data: pd.DataFrame):
    # Usuń wiersze z brakującymi wartościami w kolumnie RainTomorrow
    data = data.dropna(subset=['RainTomorrow'])

    # Usuń wiersze, w których wszystkie wartości są niezdefiniowane
    data = data.dropna(how='all')

    # Wypełnij brakujące wartości w pozostałych kolumnach
    data = data.fillna(-1)

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


def split_data(processed_data: pd.DataFrame):
    # Usuń wiersze z brakującymi etykietami w RainTomorrow
    processed_data = processed_data.dropna(subset=['RainTomorrow'])

    train_data, test_data = train_test_split(processed_data, test_size=0.2, random_state=42)

    # Zapisz dane jako tabelę w bazie danych SQLite
    conn = sqlite3.connect('weatherAUS.db')
    train_data.to_sql('train_data', conn, if_exists='replace', index=False)
    test_data.to_sql('test_data', conn, if_exists='replace', index=False)

    conn.close()

    return "Train and test data saved successfully"
