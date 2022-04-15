from typing import List
# https://leetcode.com/problems/unique-paths-ii/


def upwo_recur(og, i, j, seen):

    if (i, j) in seen:
        return seen[(i, j)]

    if i == len(og) - 1:
        seen[(i, j)] = 1 - int(1 in og[i][j:])
        return seen[(i, j)]
    if j == len(og[0]) - 1:
        seen[(i, j)] = 1 - int(1 in [row[-1] for row in og[i:]])
        return seen[(i, j)]

    if og[i][j + 1] == 1 and og[i + 1][j] == 1:
        seen[(i, j)] = 0
    elif og[i][j + 1] == 1:
        seen[(i, j)] = upwo_recur(og, i + 1, j, seen)
    elif og[i + 1][j] == 1:
        seen[(i, j)] = upwo_recur(og, i, j + 1, seen)
    else:
        seen[(i, j)] = upwo_recur(og, i + 1, j, seen) + upwo_recur(og, i, j + 1, seen)
    return seen[(i, j)]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        return upwo_recur(obstacleGrid, 0, 0, {}) if obstacleGrid[0][0] == 0 else 0

sol = Solution()
cases = [
    {
        "input": [[0,0,0],[0,1,0],[0,0,0]],
        "expect": 2
    },
    {
        "input": [[0,1],[0,0]],
        "expect": 1
    },
    {
        "input": [[0],[1]],
        "expect": 0
    }
]

for case in cases:
    result = sol.uniquePathsWithObstacles(case["input"])
    print(case["input"], result)
    assert result == case['expect']
