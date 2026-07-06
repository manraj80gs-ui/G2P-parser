"""
dictionary.py

Loads pronunciation.json and provides lookup functions.
"""

from pathlib import Path
import json
from typing import Dict, List, Optional


class PronunciationDictionary:

    def __init__(self, json_file=None):

        if json_file is None:

            root = Path(__file__).resolve().parent.parent
            json_file = root / "data" / "pronunciation.json"

        self.json_file = Path(json_file)
        self._dictionary: Dict[str, List[List[str]]] = {}

        self.load()

    def load(self):

        if not self.json_file.exists():
            raise FileNotFoundError(
                "pronunciation.json not found.\n"
                "Run preprocess.py first."
            )

        with open(self.json_file, "r", encoding="utf-8") as f:

            self._dictionary = json.load(f)

    def lookup(self, word: str) -> Optional[List[str]]:

        word = word.upper()

        result = self._dictionary.get(word)

        if result is None:
            return None

        phones = []

        for syllable in result:
            phones.extend(syllable)

        return phones

    def lookup_syllables(self, word: str):

        return self._dictionary.get(word.upper())

    def contains(self, word: str):

        return word.upper() in self._dictionary

    def words(self):

        return self._dictionary.keys()

    def size(self):

        return len(self._dictionary)
