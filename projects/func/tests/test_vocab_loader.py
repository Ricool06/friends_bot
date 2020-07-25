from unittest.mock import MagicMock
import unittest
from unittest import mock

from src.func.vocab_loader import load_vocab


@mock.patch('src.func.vocab_loader.load')
class VocabLoaderTests(unittest.TestCase):

    def test_load_default_path(self, mock_load: MagicMock):
        fake_vocab = ['v', 'o', 'c', 'a', 'b']
        mock_load.return_value = fake_vocab

        vocab = load_vocab()

        self.assertEqual(vocab, fake_vocab)
        mock_load.assert_called_once_with('resources/vocab.json')

    def test_load_specified_path(self, mock_load: MagicMock):
        fake_vocab = ['v', 'o', 'c', 'a', 'b']
        mock_load.return_value = fake_vocab
        expected_path = 'some/silly/path.json'

        vocab = load_vocab(expected_path)

        self.assertEqual(vocab, fake_vocab)
        mock_load.assert_called_once_with(expected_path)

    def test_load_non_list_json_throws(self, mock_load: MagicMock):
        fake_vocab = {'v': 'o', 'c': 4, 'b': False}
        mock_load.return_value = fake_vocab

        self.assertRaises(TypeError, load_vocab)

    def test_load_non_char_list_json_throws(self, mock_load: MagicMock):
        fake_vocab = ['v', 'o', 'c', 4, 'b']
        mock_load.return_value = fake_vocab

        self.assertRaises(TypeError, load_vocab)

    def test_load_non_single_char_list_json_throws(self, mock_load: MagicMock):
        fake_vocab = ['v', 'o', 'c', 'aaaaaaa', 'b']
        mock_load.return_value = fake_vocab

        self.assertRaises(TypeError, load_vocab)

    def test_load_non_unique_char_list_json_throws(self, mock_load: MagicMock):
        fake_vocab = ['v', 'o', 'c', 'a', 'a', 'b']
        mock_load.return_value = fake_vocab

        self.assertRaises(TypeError, load_vocab)
