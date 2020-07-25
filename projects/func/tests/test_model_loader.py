from unittest.mock import MagicMock
from tensorflow.keras.models import Sequential
import unittest
from unittest import mock
from tensorflow.python.framework.tensor_shape import TensorShape
from src.func.model_loader import load_friends_model


@mock.patch('src.func.model_loader.load_model')
class ModelLoaderTests(unittest.TestCase):

    def test_load_default_path(self, mock_load: MagicMock):
        fake_model = Sequential()
        mock_load.return_value = fake_model

        model = load_friends_model()

        self.assertEqual(model, fake_model)
        mock_load.assert_called_once_with(
            'resources/friends_model.h5', compile=False)

    def test_load_specified_path(self, mock_load: MagicMock):
        fake_model = Sequential()
        mock_load.return_value = fake_model

        model = load_friends_model('some/silly/path')

        self.assertEqual(model, fake_model)
        mock_load.assert_called_once_with(
            'some/silly/path', compile=False)

    def test_build_with_tensorshape(self, mock_load: MagicMock):
        fake_model = MagicMock()
        mock_load.return_value = fake_model
        fake_model.build = MagicMock()

        load_friends_model('some/silly/path')

        tensor_shape: TensorShape = fake_model.build.call_args_list[0][0][0]
        self.assertEqual(tensor_shape.as_list(), [1, None])
