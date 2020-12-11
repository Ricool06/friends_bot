from unittest import TestCase, mock
from unittest.mock import ANY, DEFAULT, MagicMock, Mock
from tweepy import API
from tweepy.models import Status
from func.bot import handler


@mock.patch.multiple(
    'func.bot',
    load_friends_model=DEFAULT,
    get_twitter_client=DEFAULT
)
class BotTests(TestCase):

    def test_bot(
            self,
            load_friends_model: MagicMock,
            get_twitter_client: MagicMock):
        mock_model = MagicMock()
        tweet_content = 'JOEY: How you doin\'?'
        mock_model.return_value = [{'generated_text': tweet_content}]
        load_friends_model.return_value = mock_model
        mock_api = Mock(spec=API)
        get_twitter_client.return_value = mock_api

        mock_status = Mock(spec=Status)
        mock_api.update_status.return_value = mock_status

        result = handler({}, None)

        self.assertEqual(result, mock_status)
        load_friends_model.assert_called_once()
        get_twitter_client.assert_called_once()

        model_call_args = mock_model.call_args_list[0][0]
        self.assertIn(
            model_call_args[0],
            ['JOEY', 'ROSS', 'RACHEL', 'CHANDLER', 'MONICA', 'PHOEBE'])
        mock_model.assert_called_once_with(ANY, max_length=80)

        mock_api.update_status.assert_called_once_with(
            tweet_content)
