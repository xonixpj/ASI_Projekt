"""
This is a boilerplate pipeline 'model_evaluation'
generated using Kedro 0.19.4
"""
from sklearn.metrics import f1_score, recall_score
from tensorflow.python.keras.engine.sequential import Sequential


def evaluate_model(model: Sequential, X_test, y_test):
    # Predykcja na danych testowych
    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5)  # Konwertuj wyniki na klasy binarne (0 lub 1)

    # Ocena modelu na danych testowych
    _, accuracy = model.evaluate(X_test, y_test, verbose=0)


    # Oblicz dodatkowe metryki
    f1 = f1_score(y_test, y_pred, average='micro')  # Zmiana ustawienia na 'micro'
    recall = recall_score(y_test, y_pred, average='micro')  # Zmiana ustawienia na 'micro'

    return accuracy, f1, recall