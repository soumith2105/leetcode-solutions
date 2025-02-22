"""
238. Product of Array Except Self
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Source: https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        isZero = False
        zeroCount = 0
        product = 1
        result = []

        for i in nums:
            if i == 0:
                isZero = True
                zeroCount += 1
            else:
                product *= i

        if isZero:
            result = [0] * len(nums)
            if zeroCount == 1:
                result[nums.index(0)] = product

        else:
            result = [int(product / val) for val in nums]

        return result
