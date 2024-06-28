import pickle

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

MODEL_PATH = "../ml_models/model.pkl"


def predict(request):

    request.Date = pd.to_datetime(request.Date)

    request_dict = request.dict()
    del request_dict['model']
    request_df = pd.DataFrame([request_dict])

    le = LabelEncoder()
    for column in request_df.columns:
        if request_df[column].dtype == 'object':
            request_df[column] = le.fit_transform(request_df[column].astype(str))

    scaler = MinMaxScaler()
    numeric_columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed',
                       'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am',
                       'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm']
    for column in numeric_columns:
        if request_df[column].dtype in [np.float64, np.int64]:
            request_df[column] = scaler.fit_transform(request_df[column].values.reshape(-1, 1))

    # request_df = request_df.drop(columns=['Date'])

    model = pickle.load(open(MODEL_PATH, 'rb'))
    prediction = model.predict(request_df)
    rain = "Tak" if prediction[0] == 1 else "Nie"

    print(prediction)

    return {"Rain": rain}
