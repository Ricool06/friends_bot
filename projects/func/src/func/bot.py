from typing import Dict
import random

from tweepy.models import Status
from func.get_twitter_client import get_twitter_client

from func.model_loader import load_friends_model


def handler(event: Dict, context) -> Status:
    model = load_friends_model()
    seed = random.choice(
        ['JOEY', 'ROSS', 'RACHEL', 'CHANDLER', 'MONICA', 'PHOEBE'])
    quote = model(seed, max_length=80)[0]['generated_text']
    api = get_twitter_client()

    return api.update_status(quote)


if __name__ == '__main__':
    handler({}, None)
