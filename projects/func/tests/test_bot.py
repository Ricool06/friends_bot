from unittest import TestCase, mock
from unittest.mock import DEFAULT, MagicMock, Mock
from tweepy import API
from tweepy.models import Status

from func.bot import handler


@mock.patch.multiple(
    'func.bot',
    load_vocab=DEFAULT,
    load_friends_model=DEFAULT,
    generate_quote=DEFAULT,
    get_twitter_client=DEFAULT
)
class BotTests(TestCase):

    def test_bot(
            self,
            load_vocab: MagicMock,
            load_friends_model: MagicMock,
            generate_quote: MagicMock,
            get_twitter_client: MagicMock):
        load_vocab.return_value = ['v', 'o', 'c', 'a', 'b']
        load_friends_model.return_value = MagicMock()
        generate_quote.return_value = 'Joey: How you doin\'?'
        mock_api = Mock(spec=API)
        get_twitter_client.return_value = mock_api

        mock_status = Mock(spec=Status)
        mock_api.update_status.return_value = mock_status

        result = handler({}, None)

        self.assertEqual(result, mock_status)
        load_vocab.assert_called_once()
        load_friends_model.assert_called_once()
        generate_quote.assert_called_once()
        get_twitter_client.assert_called_once()
        generate_quote_args = generate_quote.call_args_list[0][0]

        self.assertEqual(
            generate_quote_args[0],
            load_friends_model.return_value)
        self.assertIn(
            generate_quote_args[1],
            ['JOEY', 'ROSS', 'RACHEL', 'CHANDLER', 'MONICA', 'PHOEBE'])
        self.assertEqual(generate_quote_args[2], load_vocab.return_value)

        mock_api.update_status.assert_called_once_with(
            generate_quote.return_value)
