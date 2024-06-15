import requests
import streamlit as st
import pickle


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


def predict(data):
    response = requests.post("http://127.0.0.1:8008/predict", json=data)
    if response.status_code == 200:
        return response.json()
    st.error("Błąd podczas przewidywania pogody")
    return None


def main():
    st.set_page_config(page_title="Czy jutro będzie padać?")

    overview = st.container()
    left, right = st.columns(2)
    prediction = st.container()

    with overview:
        st.title("Czy jutro będzie padać?")

    with left:
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

    with right:
        st.write("Wybrane miasto: ", selected_city)

    if st.button("Przewiduj"):
        data = {
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
            "temp_3pm": temp_3pm
        }

        prediction = predict(data)
        if prediction:
            st.write(prediction)


if __name__ == '__main__':
    main()