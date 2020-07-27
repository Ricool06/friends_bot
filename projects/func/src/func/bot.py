from typing import Dict
import random

from tweepy.models import Status
from func.get_twitter_client import get_twitter_client

from src.func.vocab_loader import load_vocab
from src.func.model_loader import load_friends_model
from src.func.quote_generator import generate_quote


def handler(event: Dict, context) -> Status:
    vocab = load_vocab()
    model = load_friends_model()
    seed = random.choice(
        ['JOEY', 'ROSS', 'RACHEL', 'CHANDLER', 'MONICA', 'PHOEBE'])
    quote = generate_quote(
        model,
        seed,
        vocab)
    api = get_twitter_client()

    return api.update_status(quote)
