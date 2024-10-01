"""
Test for matching word
"""

import re

from tests import BaseTest


class WordTest(BaseTest):
    def validate(self, response: str) -> bool:
        has_match = False
        for word in self.values:
            if self.find_word(word)(response):
                has_match = True
            elif self.match_all:
                return False
        return has_match

    def find_word(self, word: str):
        return re.compile(rf"\b({word})\b", flags=self.regex_flags).search
