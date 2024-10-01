"""
Abstract base class for all AI clients.
"""

import re
from abc import ABC, abstractmethod


class BaseTest(ABC):
    def __init__(self, case: dict):
        self._case = case

    @abstractmethod
    def validate(self, response: str) -> bool:
        pass

    @property
    def case(self) -> dict:
        return self._case

    @property
    def type(self) -> str:
        return self.case.get("type")

    @property
    def name(self) -> str:
        return self.type

    @property
    def values(self) -> list:
        v = self.case.get("values")
        if not isinstance(v, list | tuple):
            # Convert v to list if it is not already a list
            v = [v]
        return v

    @property
    def match_all(self) -> bool:
        # Default only match one value,
        # if match_all is set to True, then match all values
        return self.case.get("match_all", False)

    @property
    def case_sensitive(self) -> bool:
        return self.case.get("case_sensitive", False)

    @property
    def multiline(self) -> bool:
        return self.case.get("multiline", False)

    @property
    def dotall(self) -> bool:
        return self.case.get("dotall", False)

    @property
    def regex_flags(self) -> int:
        flags = re.NOFLAG
        if not self.case_sensitive:
            flags = re.IGNORECASE
        if self.multiline:
            flags |= re.MULTILINE
        if self.dotall:
            flags |= re.DOTALL
        return flags
