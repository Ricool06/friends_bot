from os import environ
from tweepy import API, OAuthHandler
from functools import lru_cache


@lru_cache(maxsize=1)
def get_twitter_client():
    auth = OAuthHandler(environ['consumer_key'], environ['consumer_secret'])
    auth.set_access_token(environ['token'], environ['secret'])
    return API(auth)
