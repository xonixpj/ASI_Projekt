import streamlit as st
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


def main():

    menu = st.sidebar.radio("Menu", ["Przewidywanie pogody", "Zapisz dane do bazy"])

    if menu == "Przewidywanie pogody":
        st.title("Przewidywanie pogody")
        overview = st.container()
        left, mid, right = st.columns(3)

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

        with mid:
            st.write("Możesz wybrac model do przewidywania pogody")
            model_selected = st.selectbox("Wybierz model", ["Best overall", "Best F1", "Best Accuracy"], index=0)

        with right:
            st.write("Wybrane miasto: ", selected_city)

            data = {
                "model": model_selected,
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

            if st.button("Przewiduj"):
                prediction = send_predict(data)
                st.write(prediction)

    elif menu == "Zapisz dane do bazy":
        st.title("Zapisywanie danych do bazy")
        st.write("Tutaj możesz zapisać dane do bazy danych")


if __name__ == "__main__":
    main()
