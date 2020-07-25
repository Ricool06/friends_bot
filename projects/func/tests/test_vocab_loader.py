import json
from unittest.mock import MagicMock
import unittest
from unittest import mock

from src.func.vocab_loader import load_vocab


class VocabLoaderTests(unittest.TestCase):

    def test_load_default_path(self):
        fake_vocab = ['v', 'o', 'c', 'a', 'b']

        with mock.patch('builtins.open', mock.mock_open(
                read_data=json.dumps(fake_vocab))) as mocked_open:
            mocked_open: MagicMock
            vocab = load_vocab()

            self.assertEqual(vocab, fake_vocab)
            mocked_open.assert_called_once_with('resources/vocab.json', 'r')

    def test_load_specified_path(self):
        fake_vocab = ['v', 'o', 'c', 'a', 'b']
        expected_path = 'some/silly/path.json'

        with mock.patch('builtins.open', mock.mock_open(
                read_data=json.dumps(fake_vocab))) as mocked_open:
            mocked_open: MagicMock
            vocab = load_vocab(expected_path)

            self.assertEqual(vocab, fake_vocab)
            mocked_open.assert_called_once_with(expected_path, 'r')

    def test_load_non_list_json_throws(self):
        fake_vocab = {'v': 'o', 'c': 4, 'b': False}

        with mock.patch('builtins.open', mock.mock_open(
                read_data=json.dumps(fake_vocab))):

            self.assertRaises(TypeError, load_vocab)

    def test_load_non_char_list_json_throws(self):
        fake_vocab = ['v', 'o', 'c', 4, 'b']

        with mock.patch('builtins.open', mock.mock_open(
                read_data=json.dumps(fake_vocab))):

            self.assertRaises(TypeError, load_vocab)

    def test_load_non_single_char_list_json_throws(self):
        fake_vocab = ['v', 'o', 'c', 'aaaaaaa', 'b']

        with mock.patch('builtins.open', mock.mock_open(
                read_data=json.dumps(fake_vocab))):

            self.assertRaises(TypeError, load_vocab)

    def test_load_non_unique_char_list_json_throws(self):
        fake_vocab = ['v', 'o', 'c', 'a', 'a', 'b']

        with mock.patch('builtins.open', mock.mock_open(
                read_data=json.dumps(fake_vocab))):

            self.assertRaises(TypeError, load_vocab)
