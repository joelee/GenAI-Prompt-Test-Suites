"""
Test for matching RegEx
"""

import re

from tests import BaseTest


class RegexTest(BaseTest):
    def validate(self, response: str) -> bool:
        has_match = False

        for regex in self.values:
            if re.search(regex, response, flags=self.regex_flags):
                has_match = True
            elif self.match_all:
                return False
        return has_match
