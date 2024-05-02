"""
This is a boilerplate pipeline 'model_training'
generated using Kedro 0.19.4
"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def train_model(X_train, y_train) -> Sequential:
    model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
    xD = model
    return xD
