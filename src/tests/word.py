"""
Test for matching case-insensitive word
"""

import re


def find_word(w):
    return re.compile(rf"\b({w})\b", flags=re.IGNORECASE).search


def main(response: str, case: list | str) -> bool:
    has_match = False
    if not isinstance(case, list):
        case = [case]
    for word in case:
        if find_word(word)(response):
            has_match = True
    return has_match
