import pickle

MODEL_PATH = "ml_models/model.pkl"


def predict(request):
    model = pickle.load(open(MODEL_PATH, 'rb'))
    prediction = model.predict(request)
    #return prediction
    return "true"