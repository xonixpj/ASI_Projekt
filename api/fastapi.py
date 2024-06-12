import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data_schema import WhetherPredictionResponse, WhetherPredictionRequest
from libs.model import predict


app = FastAPI()


@app.post("/predict", response_model=WhetherPredictionResponse)
def get_prediction(request: WhetherPredictionRequest):
    prediction = predict(request)
    return JSONResponse(content={"Predict": prediction})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8008)
