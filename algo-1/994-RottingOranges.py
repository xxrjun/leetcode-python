class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count_minutes = 0

        q = collections.deque()

        # Put all rotten oranges' position into queue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append([i, j])

        # 4 directions [row, col]: right, left, up, down
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Be used to check when to count minutes
        last_q_len = len(q)
        cur_count = 0

        # bfs
        while q:
            row, col = q[0][0], q[0][1]
            q.popleft()

            # Check 4-directionally to a rotten orange
            for i in range(len(dir)):
                newRow = row + dir[i][0]
                newCol = col + dir[i][1]

                # Check bound
                if newRow < len(grid) and newRow >= 0 and newCol < len(grid[0]) and newCol >= 0:
                    if grid[newRow][newCol] == 1:
                        # A fresh orange becomes rotten
                        grid[newRow][newCol] = 2

                        # Put the new rotten orange into queue
                        q.append([newRow, newCol])

            cur_count += 1

            # Finished one round
            if cur_count == last_q_len:
                last_q_len = len(q)
                cur_count = 0
                count_minutes += 1

        # check whether still fresh orange exists
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        # Minus last count if count_minutes is > 0
        if count_minutes > 0:
            count_minutes -= 1

        return count_minutes
