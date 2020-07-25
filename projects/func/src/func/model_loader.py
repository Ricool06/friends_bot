from tensorflow import TensorShape
from tensorflow.keras.models import load_model, Sequential


def load_friends_model(
        path: str = 'resources/friends_practice_model.h5') -> Sequential:
    model = load_model(path, compile=False)
    model.build(TensorShape([1, None]))
    return model
