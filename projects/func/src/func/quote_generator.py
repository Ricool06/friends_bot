from typing import List
from tensorflow.keras.models import Sequential
from tensorflow import expand_dims, squeeze
from tensorflow.random import categorical
import numpy as np


def generate_quote(
        model: Sequential,
        seed: str,
        vocab: List[str],
        length=100,
        temp=1.0) -> str:
    '''
    model: Trained Model to Generate Text
    seed: Intial seed text in string form
    vocab: The set of characters to use, in List[str] form
    length: Full length of generated text, including seed
    temp: randomness value

    Basic idea behind this function is to take in some seed text, format it so
    that it is in the correct shape for our network, then loop the sequence as
    we keep adding our own predicted characters. Similar to RNN
    time series problems.
    '''

    char_to_ind = {c: i for i, c in enumerate(vocab)}
    ind_to_char = np.array(vocab)
    input_eval = [char_to_ind[c] for c in seed]

    input_eval = expand_dims(input_eval, 0)

    generated_chars = []

    for i in range(length - len(seed)):

        predictions = model(input_eval)
        predictions = squeeze(predictions, 0)
        predictions = predictions / temp

        predicted_id = categorical(predictions, num_samples=1)[-1, 0].numpy()

        input_eval = expand_dims([predicted_id], 0)

        generated_chars.append(ind_to_char[predicted_id])

    return (seed + ''.join(generated_chars))
