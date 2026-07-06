"""
parser.py

Public API for English G2P.
"""

import re
from typing import List, Optional

from .dictionary import PronunciationDictionary

_dictionary = PronunciationDictionary()


def normalize(word: str):

    word = word.upper()

    word = re.sub(r"[^A-Z0-9()'-]", "", word)

    return word


def wordparse(word: str) -> Optional[List[str]]:

    word = normalize(word)

    return _dictionary.lookup(word)


def wordstruct(word):

    word = normalize(word)

    return _dictionary.lookup_syllables(word)


def sentenceparse(sentence: str):

    words = re.findall(r"[A-Za-z0-9()'-]+", sentence)

    return [wordparse(word) for word in words]


def exists(word):

    word = normalize(word)

    return _dictionary.contains(word)


def dictionary_size():

    return _dictionary.size()
