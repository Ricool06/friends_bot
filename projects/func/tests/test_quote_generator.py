from unittest.mock import MagicMock
import tensorflow
from tensorflow import expand_dims, Tensor

from func.quote_generator import generate_quote


class QuoteGeneratorTests(tensorflow.test.TestCase):

    def test_generate_quote(self):
        seed = 'joey'
        expected_length = 140

        char_to_ind = {c: i for i, c in enumerate(seed)}
        expected_call_count = expected_length - len(seed)
        vocab = list(seed)

        expected_first_input_tensor = expand_dims(
            [char_to_ind[c] for c in seed], 0)
        expected_subsequent_input_tensor = expand_dims(
            [char_to_ind['j']], 0)

        model = MagicMock(return_value=expand_dims(
            [[85.0, 1.1, -2.1, 3.2]], 0))

        quote = generate_quote(
            model,
            seed,
            vocab,
            length=expected_length)

        first_input_tensor: Tensor = model.call_args_list[0][0][0]
        self.assertAllEqual(first_input_tensor, expected_first_input_tensor)
        self.assertEqual(len(quote), expected_length)

        self.assertEqual(model.call_count, expected_call_count)

        for args in model.call_args_list[1:]:
            self.assertAllEqual(args[0][0], expected_subsequent_input_tensor)
