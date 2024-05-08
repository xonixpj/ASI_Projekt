"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.4
"""
from sklearn.metrics import f1_score, recall_score
from tensorflow.python.keras.engine.sequential import Sequential


def evaluate_model(predictor, test_data):
    results = predictor.evaluate(test_data)
    return results