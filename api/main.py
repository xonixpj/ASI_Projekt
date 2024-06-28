import uvicorn
import subprocess
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data_schema import WhetherPredictionResponse, WhetherPredictionRequest, WhetherSaveDataRequest, WhetherReadDataRequest
from model import predict
from data import read_data, save_data


app = FastAPI()


@app.post("/predict", response_model=WhetherPredictionResponse)
def get_prediction(request: WhetherPredictionRequest):
    print(request)
    prediction = predict(request)
    return JSONResponse(content={"Predict": prediction})


@app.post("/train")
def train():
    result = subprocess.run(["kedro", "run"], stdout=subprocess.PIPE)
    if result.returncode != 0:
        return JSONResponse(content="Model training failed")
    return JSONResponse(content="Model trained successfully")


@app.post("/save")
def save(request: WhetherSaveDataRequest):
    save_data(request)
    return JSONResponse(content="Data saved successfully")


@app.get("/read")
def read():
    data = read_data()
    return data


if __name__ == "__main__":
    print("xD")
    uvicorn.run(app, host="0.0.0.0", port=12345)
