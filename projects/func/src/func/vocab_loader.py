from json import load
from typing import Any, List


def load_vocab(path: str = 'resources/vocab.json') -> List[str]:
    json = load(path)

    if not __is_valid_vocab(json):
        raise TypeError(
            f'Expected a set of single chars, got: {json}')

    return json


def __is_valid_vocab(json: Any):
    return (type(json) is list
            and all(type(e) is str for e in json)
            and all(len(e) == 1 for e in json)
            and len(set(json)) == len(json))
