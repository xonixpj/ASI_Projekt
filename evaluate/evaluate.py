from sklearn.metrics import f1_score, recall_score


def evaluate_model(model, X_test, y_test):
    # Predykcja na danych testowych
    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5)  # Konwertuj wyniki na klasy binarne (0 lub 1)

    # Ocena modelu na danych testowych
    _, accuracy = model.evaluate(X_test, y_test, verbose=0)


    # Oblicz dodatkowe metryki
    f1 = f1_score(y_test, y_pred, average='micro')  # Zmiana ustawienia na 'micro'
    recall = recall_score(y_test, y_pred, average='micro')  # Zmiana ustawienia na 'micro'

    return accuracy, f1, recall
