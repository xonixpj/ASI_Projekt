import numpy as np
import tensorflow as tf
from sklearn.model_selection import KFold

from data_processing.data_processing import process_data
from evaluate.evaluate import evaluate_model
from model_training.model_training import train_model

physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

X, y = process_data()

n_splits = 10
kf = KFold(n_splits=n_splits)
fold_accuracy = []
fold_f1 = []
fold_recall = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    model = train_model(X_train, y_train)
    accuracy, f1, recall = evaluate_model(model, X_test, y_test)

    fold_accuracy.append(accuracy)
    fold_f1.append(f1)
    fold_recall.append(recall)

mean_accuracy = np.mean(fold_accuracy)
std_accuracy = np.std(fold_accuracy)
mean_f1 = np.mean(fold_f1)
std_f1 = np.std(fold_f1)
mean_recall = np.mean(fold_recall)
std_recall = np.std(fold_recall)

print(f'Średnia dokładność: {mean_accuracy} ± {std_accuracy}')
print(f'Średnie F1-score: {mean_f1} ± {std_f1}')
print(f'Średnia czułość: {mean_recall} ± {std_recall}')