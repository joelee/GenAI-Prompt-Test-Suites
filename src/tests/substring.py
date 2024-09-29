"""
Test for matching case-insensitive substring
"""


def main(response: str, case: list | str) -> bool:
    has_match = False
    if not isinstance(case, list):
        case = [case]
    for substr in case:
        if substr.lower() in response.lower():
            has_match = True
    return has_match
