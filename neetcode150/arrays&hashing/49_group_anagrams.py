"""
49. Group Anagrams
Given an array of strings `strs`, group the `anagrams` together. You can return the answer in any order.

Source: https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            val = "".join(sorted(i))
            result[val] = result.get(val, [])
            result[val].append(i)

        return list(result.values())
