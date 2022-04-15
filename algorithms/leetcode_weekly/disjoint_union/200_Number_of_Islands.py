from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]], method='bfs') -> int:
        if method == 'union_joint':
            return self.numIslandsUnionJoint(grid)
        if method == 'dfs':
            return self.numIslandsDfs(grid)
        if method == 'bfs':
            return self.numIslandsBfs(grid)

    def numIslandsUnionJoint(self, grid):
        def find(x):
            nonlocal pa
            while x != pa[x]:
                x = pa[x]
            return x

        def union_joint(x, y, nr_groups):
            nonlocal pa
            nonlocal size

            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return nr_groups
            else:
                if size[root_x] > size[root_y]:
                    pa[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    pa[root_x] = root_y
                    size[root_y] += root_x
                return nr_groups - 1

        m, n = len(grid), len(grid[0])
        nr_groups = m * n
        pa = [i for i in range(nr_groups)]
        size = [1] * nr_groups
        nr_land_cell = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    nr_land_cell += 1
                    for direction in [[1,0],[0,1]]:
                        new_i = i + direction[0]
                        new_j = j + direction[1]
                        if new_i < m and new_j < n and grid[new_i][new_j] == '1':
                            nr_groups = union_joint(i * n + j, new_i * n + new_j, nr_groups)
        return nr_groups - (n*m - nr_land_cell)


    def numIslandsDfs(self, grid):
        def dfs(i, j, m, n, visited):
            nonlocal grid
            visited[i][j] = 1
            for dir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if -1 < new_i < m and -1 < new_j < n:
                     if visited[new_i][new_j] == 0 and grid[new_i][new_j] == '1':
                         dfs(new_i, new_j, m, n, visited)

        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        nr_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    visited[i][j] = 1
                    continue
                if visited[i][j] == 1:
                    continue
                dfs(i, j, m, n, visited)
                nr_island += 1
        return nr_island

    def numIslandsBfs(self, grid):
        def bfs(x, y, m, n, visited):
            nonlocal grid
            cell_queue = deque([(x, y)])
            visited[x][y] = 1
            while cell_queue:
                pos = cell_queue.popleft()
                i, j = pos
                for dir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    new_i = i + dir[0]
                    new_j = j + dir[1]
                    if -1 < new_i < m and -1 < new_j < n:
                         if visited[new_i][new_j] == 0 and grid[new_i][new_j] == '1':
                             visited[new_i][new_j] = 1
                             cell_queue.append((new_i, new_j))

        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        nr_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    visited[i][j] = 1
                    continue
                if visited[i][j] == 1:
                    continue
                bfs(i, j, m, n, visited)
                nr_island += 1
        return nr_island


sol = Solution()
cases = [
    {
        "input": [
                      ["1","1","1","1","0"],
                      ["1","1","0","1","0"],
                      ["1","1","0","0","0"],
                      ["0","0","0","0","0"]
                  ],
        "expect": 1
    },
    {
        "input": [
                    ["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]
                 ],
        "expect": 3
    },
]

for case in cases:
    result = sol.numIslands(case["input"])
    print(case["input"], result)
    assert result == case['expect']
