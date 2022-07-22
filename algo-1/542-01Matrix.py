# 542. 01 Matrix

import collections
from pickletools import dis
import sys


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 0:
            return mat

        # Initialize distance matrix we should return
        distMatrix = [[0] * len(mat[0]) for i in range(len(mat))]

        q = collections.deque()
        maxValue = sys.maxsize

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    # put all 0's position to the queue
                    q.append([i, j])
                else:
                    # Fill a big number in distance matrix if it's a non-zero element in mat
                    distMatrix[i][j] = sys.maxsize

        # Four directions [row, col], [up, down, left, right]
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Update distance using BFS
        while q:
            row, col = q[0][0], q[0][1]
            q.popleft()

            # Check 4 directions:
            for i in range(len(dir)):
                newRow = row + dir[i][0]
                newCol = col + dir[i][1]

                # Check bound
                if newRow >= 0 and newRow < len(mat) and newCol >= 0 and newCol < len(mat[0]):
                    # Check if it's a shorter distance
                    if distMatrix[row][col] + 1 < distMatrix[newRow][newCol]:
                        # Update distance
                        distMatrix[newRow][newCol] = distMatrix[row][col] + 1

                        # Put the position into queue to calculate other neighbors' distance
                        q.append([newRow, newCol])

        return distMatrix
