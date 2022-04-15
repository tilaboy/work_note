from typing import List

def get_start(mat, m, value):
    for i in range(m):
        if value in mat[i]:
            return (i, mat[i].index(value))

def uq_recur(grid, i, j, m, n, rest):
    if i < 0 or j < 0 or i == m or j == n:
        return 0
    if grid[i][j] < 0:
        return 0

    if grid[i][j] == 2:
        if rest == 0:
            return 1
        else:
            return 0
    else:
        nr_path = 0
        rest -= 1
        temp_rock = grid[i][j]
        grid[i][j] = -1
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            new_i = i + dx
            new_j = j + dy
            nr_path += uq_recur(grid, new_i, new_j, m, n, rest)

        grid[i][j] = temp_rock
        return nr_path


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # 1 start, 2 end, -1 stone, 0 path
        m, n = len(grid), len(grid[0])
        i, j = get_start(grid, m, 1)
        # why not -5, need to include start point, path = start_point + all empty cells
        rest = m * n + sum(sum(row) for row in grid) - 4
        print(m, n, rest)
        return uq_recur(grid, i, j, m, n, rest)

sol = Solution()
cases = [
    {
        "input": [[1,0,0,0],[0,0,0,0],[0,0,2,-1]],
        "expect": 2
    },
    {
        "input": [[1,0,0,0],[0,0,0,0],[0,0,0,2]],
        "expect": 4
    },
    {
        "input": [[0,1],[2,0]],
        "expect": 0
    }
]

for case in cases:
    result = sol.uniquePathsIII(case["input"])
    print(case["input"], result)
    assert result == case['expect']
