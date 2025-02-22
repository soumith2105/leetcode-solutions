"""
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Source: https://leetcode.com/problems/valid-sudoku/
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def getcol(ind):
            res = [val[ind] for val in board if val[ind] != "."]
            return len(res) == len(set(res))

        def getrow(ind):
            res = [val for val in board[ind] if val != "."]
            return len(res) == len(set(res))

        def get9x9(ind1, ind2):
            res = []
            for i in board[ind1 : ind1 + 3]:
                res += [j for j in i[ind2 : ind2 + 3] if j != "."]

            return len(res) == len(set(res))

        for i in range(0, 9):
            if not getcol(i) or not getrow(i):
                return False

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                if not get9x9(i, j):
                    return False

        return True
