import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data_schema import WhetherPredictionResponse, WhetherPredictionRequest
from model import predict


app = FastAPI()


@app.post("/predict", response_model=WhetherPredictionResponse)
def get_prediction(request: WhetherPredictionRequest):
    print(request)
    prediction = predict(request)
    return JSONResponse(content={"Predict": prediction})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=12345)
