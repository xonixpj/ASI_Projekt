import datetime
from time import strftime

import streamlit as st
import pandas as pd
import requests

cities = [
    "Albury", "BadgerysCreek", "Cobar", "CoffsHarbour", "Moree", "NorahHead", "NorfolkIsland",
    "Penrith", "Richmond", "Sydney", "SydneyAirport", "WaggaWagga", "Williamtown", "Wollongong",
    "Canberra", "Tuggeranong", "MountGinini", "Ballarat", "Bendigo", "Sale", "MelbourneAirport",
    "Melbourne", "Mildura", "Nhil", "Portland", "Watsonia", "Dartmoor", "Brisbane", "Cairns",
    "GoldCoast", "Townsville", "Adelaide", "MountGambier", "Nuriootpa", "Woomera", "Albany",
    "Witchcliffe", "PearceRAAF", "PerthAirport", "Perth", "SalmonGums", "Walpole", "Hobart",
    "Launceston", "AliceSprings", "Darwin", "Katherine", "Uluru"
]
default_city = "Sydney"


def send_predict(data):
    response = requests.post("http://fastapi:12345/predict", json=data)
    return response.text


def send_train():
    response = requests.post("http://fastapi:12345/train")
    return response.text


def send_save(data):
    response = requests.post("http://fastapi:12345/save", json=data)
    return response.text


def send_read():
    response = requests.get("http://fastapi:12345/read")
    return response.json()


def main():

    menu = st.sidebar.radio("Menu", ["Przewidywanie pogody", "Zapisz dane do bazy", "Dane", "Trenuj model"])

    if menu == "Przewidywanie pogody":
        st.title("Przewidywanie pogody")
        overview = st.container()
        left, mid, right = st.columns(3)

        with overview:
            st.title("Czy jutro będzie padać?")

        with left:
            date_input = st.date_input("Data", value=datetime.date.today())
            selected_city = st.selectbox("Wybierz miasto", cities, index=cities.index(default_city))
            min_temp = st.number_input("MinTemp", value=0.0)
            max_temp = st.number_input("MaxTemp", value=0.0)
            rainfall = st.number_input("Rainfall", value=0.0)
            evaporation = st.number_input("Evaporation", value=0.0)
            sunshine = st.number_input("Sunshine", value=0.0)
            wind_gust_dir = st.selectbox("WindGustDir",
                                     options=["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW",
                                              "W", "WNW", "NW", "NNW"])
            wind_gust_speed = st.number_input("WindGustSpeed", value=0)
            wind_dir_9am = st.selectbox("WindDir9am",
                                    options=["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW",
                                             "W", "WNW", "NW", "NNW"])
            wind_dir_3pm = st.selectbox("WindDir3pm",
                                    options=["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW",
                                             "W", "WNW", "NW", "NNW"])
            wind_speed_9am = st.number_input("WindSpeed9am", value=0)
            wind_speed_3pm = st.number_input("WindSpeed3pm", value=0)
            humidity_9am = st.number_input("Humidity9am", value=0)
            humidity_3pm = st.number_input("Humidity3pm", value=0)
            pressure_9am = st.number_input("Pressure9am", value=0.0)
            pressure_3pm = st.number_input("Pressure3pm", value=0.0)
            cloud_9am = st.slider("Cloud9am", min_value=-1, max_value=8, value=0)
            cloud_3pm = st.slider("Cloud3pm", min_value=-1, max_value=8, value=0)
            temp_9am = st.number_input("Temp9am", value=0.0)
            temp_3pm = st.number_input("Temp3pm", value=0.0)
            rain_today = st.selectbox("RainToday", options=["Yes", "No"], index=1)

        with mid:
            st.write("Możesz wybrac model do przewidywania pogody")
            model_selected = st.selectbox("Wybierz model", ["Best overall", "Best F1", "Best Accuracy"], index=0)

        with right:
            st.write("Wybrane miasto: ", selected_city)

            data = {
                "model": model_selected,
                "Date": date_input.strftime("%Y-%m-%d"),
                "Location": selected_city,
                "MinTemp": min_temp,
                "MaxTemp": max_temp,
                "Rainfall": rainfall,
                "Evaporation": evaporation,
                "Sunshine": sunshine,
                "WindGustDir": wind_gust_dir,
                "WindGustSpeed": wind_gust_speed,
                "WindDir9am": wind_dir_9am,
                "WindDir3pm": wind_dir_3pm,
                "WindSpeed9am": wind_speed_9am,
                "WindSpeed3pm": wind_speed_3pm,
                "Humidity9am": humidity_9am,
                "Humidity3pm": humidity_3pm,
                "Pressure9am": pressure_9am,
                "Pressure3pm": pressure_3pm,
                "Cloud9am": cloud_9am,
                "Cloud3pm": cloud_3pm,
                "Temp9am": temp_9am,
                "Temp3pm": temp_3pm,
                "RainToday": rain_today
            }

            if st.button("Przewiduj"):
                prediction = send_predict(data)
                st.write(prediction)

    elif menu == "Zapisz dane do bazy":
        st.title("Zapisywanie danych do bazy")
        st.write("Tutaj możesz zapisać dane do bazy danych")

        overview = st.container()
        left, right = st.columns(2)

        with left:
            date = st.date_input("Date")
            selected_city = st.selectbox("Wybierz miasto", cities, index=cities.index(default_city))
            min_temp = st.number_input("MinTemp", value=0.0)
            max_temp = st.number_input("MaxTemp", value=0.0)
            rainfall = st.number_input("Rainfall", value=0.0)
            evaporation = st.number_input("Evaporation", value=0.0)
            sunshine = st.number_input("Sunshine", value=0.0)
            wind_gust_dir = st.selectbox("WindGustDir",
                                         options=["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW",
                                                  "WSW",
                                                  "W", "WNW", "NW", "NNW"])
            wind_gust_speed = st.number_input("WindGustSpeed", value=0)
            wind_dir_9am = st.selectbox("WindDir9am",
                                        options=["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW",
                                                 "WSW",
                                                 "W", "WNW", "NW", "NNW"])
            wind_dir_3pm = st.selectbox("WindDir3pm",
                                        options=["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW",
                                                 "WSW",
                                                 "W", "WNW", "NW", "NNW"])
            wind_speed_9am = st.number_input("WindSpeed9am", value=0)
            wind_speed_3pm = st.number_input("WindSpeed3pm", value=0)
            humidity_9am = st.number_input("Humidity9am", value=0)
            humidity_3pm = st.number_input("Humidity3pm", value=0)
            pressure_9am = st.number_input("Pressure9am", value=0.0)
            pressure_3pm = st.number_input("Pressure3pm", value=0.0)
            cloud_9am = st.slider("Cloud9am", min_value=-1, max_value=8, value=0)
            cloud_3pm = st.slider("Cloud3pm", min_value=-1, max_value=8, value=0)
            temp_9am = st.number_input("Temp9am", value=0.0)
            temp_3pm = st.number_input("Temp3pm", value=0.0)
            rain = st.radio("Rain", ["Yes", "No"], index=1)
            rain_tomorrow = st.radio("RainTomorrow", ["Yes", "No"], index=1)

        with right:

            data = {
                "date": strftime("%Y-%m-%d"),
                "selected_city": selected_city,
                "min_temp": min_temp,
                "max_temp": max_temp,
                "rainfall": rainfall,
                "evaporation": evaporation,
                "sunshine": sunshine,
                "wind_gust_dir": wind_gust_dir,
                "wind_gust_speed": wind_gust_speed,
                "wind_dir_9am": wind_dir_9am,
                "wind_dir_3pm": wind_dir_3pm,
                "wind_speed_9am": wind_speed_9am,
                "wind_speed_3pm": wind_speed_3pm,
                "humidity_9am": humidity_9am,
                "humidity_3pm": humidity_3pm,
                "pressure_9am": pressure_9am,
                "pressure_3pm": pressure_3pm,
                "cloud_9am": cloud_9am,
                "cloud_3pm": cloud_3pm,
                "temp_9am": temp_9am,
                "temp_3pm": temp_3pm,
                "rain": rain,
                "rain_tomorrow": rain_tomorrow
            }

            if st.button("Zapisz"):
                result = send_save(data)
                st.write(result)

            # if st.button("Wczytaj dane"):
            #     response = requests.get("http://fastapi:12345/read")
            #     st.write(response.text)

    elif menu == "Trenuj model":
        st.title("Trenowanie modelu")
        st.write("Tutaj możesz trenować model")
        if st.button("Trenuj"):
            result = send_train()
            st.write(result)

    elif menu == "Dane":
        st.title("Dane")
        st.write("Tutaj możesz zobaczyć dane")

        response = send_read()
        df = pd.DataFrame(response)
        st.dataframe(df)


if __name__ == "__main__":
    main()
