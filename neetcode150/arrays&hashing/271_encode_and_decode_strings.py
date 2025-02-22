"""
271. Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Source: https://leetcode.com/problems/encode-and-decode-strings/
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ";;".join(strs) if len(strs) > 0 else "///"

    def decode(self, s: str) -> List[str]:
        return s.split(";;") if s != "///" else []
