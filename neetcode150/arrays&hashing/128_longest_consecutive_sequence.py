"""
128. Longest Consecutive Sequence
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

Source: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))

        res = 1
        max_val = 0
        prev = nums[0]
        for i in nums[1:]:
            if prev + 1 == i:
                res += 1
            else:
                max_val = max(res, max_val)
                res = 1

            prev = i

        max_val = max(res, max_val)

        return max_val
