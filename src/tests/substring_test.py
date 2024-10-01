"""
Test for matching case-insensitive substring
"""

from tests import BaseTest


class SubstringTest(BaseTest):
    def validate(self, response: str) -> bool:
        has_match = False
        for substr in self.values:
            if self.case_sensitive:
                if substr in response:
                    has_match = True
                elif self.match_all:
                    return False
            elif substr.lower() in response.lower():
                has_match = True
            elif self.match_all:
                return False
        return has_match
