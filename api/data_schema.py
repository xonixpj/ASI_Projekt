from typing import Optional

from pydantic import BaseModel


class WhetherPredictionResponse(BaseModel):
    Predict: str


class WhetherPredictionRequest(BaseModel):
    model: str
    Date: str
    Location: str
    MinTemp: float
    MaxTemp: float
    Rainfall: float
    Evaporation: float
    Sunshine: float
    WindGustDir: str
    WindGustSpeed: int
    WindDir9am: str
    WindDir3pm: str
    WindSpeed9am: int
    WindSpeed3pm: int
    Humidity9am: int
    Humidity3pm: int
    Pressure9am: float
    Pressure3pm: float
    Cloud9am: int
    Cloud3pm: int
    Temp9am: float
    Temp3pm: float
    RainToday: str


class WhetherSaveDataRequest(BaseModel):
    date: str
    selected_city: str
    min_temp: float
    max_temp: float
    rainfall: float
    evaporation: float
    sunshine: float
    wind_gust_dir: str
    wind_gust_speed: int
    wind_dir_9am: str
    wind_dir_3pm: str
    wind_speed_9am: int
    wind_speed_3pm: int
    humidity_9am: int
    humidity_3pm: int
    pressure_9am: float
    pressure_3pm: float
    cloud_9am: int
    cloud_3pm: int
    temp_9am: float
    temp_3pm: float
    rain: str
    rain_tomorrow: str


class WhetherReadDataRequest(BaseModel):
    date: Optional[str]
    selected_city: Optional[str]
    min_temp: Optional[float]
    max_temp: Optional[float]
    rainfall: Optional[float]
    evaporation: Optional[float]
    sunshine: Optional[float]
    wind_gust_dir: Optional[str]
    wind_gust_speed: Optional[int]
    wind_dir_9am: Optional[str]
    wind_dir_3pm: Optional[str]
    wind_speed_9am: Optional[int]
    wind_speed_3pm: Optional[int]
    humidity_9am: Optional[int]
    humidity_3pm: Optional[int]
    pressure_9am: Optional[float]
    pressure_3pm: Optional[float]
    cloud_9am: Optional[int]
    cloud_3pm: Optional[int]
    temp_9am: Optional[float]
    temp_3pm: Optional[float]
    rain: Optional[str]
    rain_tomorrow: Optional[str]
