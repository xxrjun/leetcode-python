# 542. 01 Matrix

from ast import MatchValue
import collections
import sys


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 0:
            return mat

        distmat = [[0] * len(mat[0]) for i in range(len(mat))]

        q = collections.deque()
        maxValue = sys.maxsize

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    q.append([i, j])
                else:
                    distmat[i][j] = maxValue

        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            row, col = q[0][0], q[0][1]
            q.popleft()

            for i in range(len(dir)):
                newRow = row + dir[i][0]
                newCol = col + dir[i][1]

                if newRow < len(mat) and newRow >= 0 and newCol < len(mat[0]) and newCol >= 0:

                    if distmat[row][col] + 1 < distmat[newRow][newCol]:
                        distmat[newRow][newCol] = distmat[row][col] + 1
                        q.append([newRow, newCol])

        return distmat
