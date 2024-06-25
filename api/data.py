import sqlite3
from data_schema import WhetherSaveDataRequest, WhetherReadDataRequest


def save_data(data: WhetherSaveDataRequest):
    conn = sqlite3.connect('../asi-kedro/weatherAUS.db')

    cursor = conn.cursor()

    cursor.execute("INSERT INTO weather (Date,Location,MinTemp,MaxTemp,Rainfall,Evaporation,Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,Temp9am,Temp3pm,RainToday,RainTomorrow) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (data.date, data.selected_city, data.min_temp, data.max_temp, data.rainfall, data.evaporation, data.sunshine, data.wind_gust_dir, data.wind_gust_speed, data.wind_dir_9am, data.wind_dir_3pm, data.wind_speed_9am, data.wind_speed_3pm, data.humidity_9am, data.humidity_3pm, data.pressure_9am, data.pressure_3pm, data.cloud_9am, data.cloud_3pm, data.temp_9am, data.temp_3pm, data.rain, data.rain_tomorrow))

    conn.commit()

    conn.close()

    return "Data saved successfully"


def read_data():
    conn = sqlite3.connect('../asi-kedro/weatherAUS.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM weather")

    data = cursor.fetchall()

    data_list = []

    for row in data:
        data = WhetherReadDataRequest(
            date=row[0] if row[0] is not None else None,
            selected_city=row[1] if row[1] is not None else None,
            min_temp=row[2] if row[2] is not None else None,
            max_temp=row[3] if row[3] is not None else None,
            rainfall=row[4] if row[4] is not None else None,
            evaporation=row[5] if row[5] is not None else None,
            sunshine=row[6] if row[6] is not None else None,
            wind_gust_dir=row[7] if row[7] is not None else None,
            wind_gust_speed=row[8] if row[8] is not None else None,
            wind_dir_9am=row[9] if row[9] is not None else None,
            wind_dir_3pm=row[10] if row[10] is not None else None,
            wind_speed_9am=row[11] if row[11] is not None else None,
            wind_speed_3pm=row[12] if row[12] is not None else None,
            humidity_9am=row[13] if row[13] is not None else None,
            humidity_3pm=row[14] if row[14] is not None else None,
            pressure_9am=row[15] if row[15] is not None else None,
            pressure_3pm=row[16] if row[16] is not None else None,
            cloud_9am=row[17] if row[17] is not None else None,
            cloud_3pm=row[18] if row[18] is not None else None,
            temp_9am=row[19] if row[19] is not None else None,
            temp_3pm=row[20] if row[20] is not None else None,
            rain=row[21] if row[21] is not None else None,
            rain_tomorrow=row[22] if row[22] is not None else None,
        )
        data_list.append(data)

    conn.close()

    return data_list
