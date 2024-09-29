"""
Test for matching RegEx
"""

import re


def main(response: str, case: list | str) -> bool:
    has_match = False
    if not isinstance(case, list):
        case = [case]
    for regex in case:
        if re.search(regex, response):
            has_match = True
            print(f"MATCH: {regex}")
        else:
            print(f"NO MATCH: {regex}")
    return has_match
