from unittest.mock import MagicMock
import unittest
from unittest import mock
from func.model_loader import load_friends_model


@mock.patch('func.model_loader.pipeline')
class ModelLoaderTests(unittest.TestCase):

    def test_load_default_path(self, mock_pipeline: MagicMock):
        fake_model = MagicMock()
        mock_pipeline.return_value = fake_model

        model = load_friends_model()

        self.assertEqual(model, fake_model)
        mock_pipeline.assert_called_once_with(
            'text-generation', model='resources/')

    def test_load_specified_path(self, mock_pipeline: MagicMock):
        fake_model = MagicMock()
        mock_pipeline.return_value = fake_model

        model = load_friends_model('some/silly/path')

        self.assertEqual(model, fake_model)
        mock_pipeline.assert_called_once_with(
            'text-generation', model='some/silly/path')


