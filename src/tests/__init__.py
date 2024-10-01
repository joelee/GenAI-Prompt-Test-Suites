from .base_test import BaseTest  # noqa: F401
from .regex_test import RegexTest  # noqa: F401
from .substring_test import SubstringTest  # noqa: F401
from .word_test import WordTest  # noqa: F401


def import_test(name):
    class_name = f"{name.title()}Test"
    try:
        return globals()[class_name]
    except KeyError as e:
        raise ImportError(f"Cannot import {class_name}") from e
