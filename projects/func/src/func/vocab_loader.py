from json import load
from typing import Any, List


def load_vocab(path: str = 'resources/vocab.json') -> List[str]:
    with open(path, 'r') as json_file:
        json = load(json_file)

        if not _is_valid_vocab(json):
            raise TypeError(
                f'Expected a set of single chars, got: {json}')

        return json


def _is_valid_vocab(json: Any):
    return (type(json) is list
            and all(type(e) is str for e in json)
            and all(len(e) == 1 for e in json)
            and len(set(json)) == len(json))
