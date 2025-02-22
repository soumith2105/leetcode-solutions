"""
347. Top K Frequent Elements
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

Source: https://leetcode.com/problems/top-k-frequent-elements/
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}

        for i in nums:
            result[i] = result.get(i, 0)
            result[i] += 1

        result = sorted(
            [[value, key] for key, value in result.items()],
            reverse=True,
            key=lambda x: x[0],
        )[:k]

        return [key[1] for key in result]
