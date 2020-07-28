from unittest import TestCase
from unittest import mock
from unittest.mock import DEFAULT, MagicMock

from func.get_twitter_client import get_twitter_client


mock_environ = {
    'consumer_key': 'consumer_key_value',
    'consumer_secret': 'consumer_secret_value',
    'token': 'token_value',
    'secret': 'secret_value'
}


@mock.patch.multiple(
    'func.get_twitter_client',
    API=DEFAULT,
    OAuthHandler=DEFAULT,
    environ=mock_environ,
)
class GetTwitterClientTests(TestCase):

    def test_get_twitter_client(
            self,
            API: MagicMock,
            OAuthHandler: MagicMock):
        client = get_twitter_client()

        self.assertEqual(client, API.return_value)
        API.assert_called_once_with(OAuthHandler.return_value)
        OAuthHandler.assert_called_once_with(
            mock_environ['consumer_key'], mock_environ['consumer_secret'])
        OAuthHandler.return_value.set_access_token.assert_called_once_with(
            mock_environ['token'], mock_environ['secret'])

    def test_get_twitter_client_caches(
            self,
            API: MagicMock,
            OAuthHandler: MagicMock):
        API.side_effect = [MagicMock(), MagicMock()]

        client = get_twitter_client()
        second_client = get_twitter_client()

        self.assertIs(client, second_client)
