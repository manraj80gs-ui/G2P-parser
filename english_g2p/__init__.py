"""
English Grapheme-to-Phoneme Parser
"""

from .parser import (
    wordparse,
    wordstruct,
    sentenceparse,
    exists,
    dictionary_size,
)

__version__ = "0.2.0"

__all__ = [
    "wordparse",
    "wordstruct",
    "sentenceparse",
    "exists",
    "dictionary_size",
]
