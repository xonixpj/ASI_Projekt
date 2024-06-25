from pydantic import BaseModel


class WhetherPredictionResponse(BaseModel):
    Predict: str


class WhetherPredictionRequest(BaseModel):
    model: str
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
