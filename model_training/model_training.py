import tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def train_model(X, y):
    model = Sequential([
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

    return model
