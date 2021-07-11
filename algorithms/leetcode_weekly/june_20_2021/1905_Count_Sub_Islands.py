from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid, i_row, i_col):
            nonlocal nr_groups, visited, grid_labels, m, n
            visited[i_row][i_col] = True
            grid_labels[i_row][i_col] = nr_groups
            for (j_row, j_col) in get_neighbours(i_row, i_col):
                if visited[j_row][j_col] == False and grid[j_row][j_col] == 1:
                    dfs(grid, j_row, j_col)

        def find_subgraph(grid):
            nonlocal nr_groups, visited, m, n
            for i_row in range(m):
                for i_col in range(n):
                    if visited[i_row][i_col] == False and grid[i_row][i_col] == 1:
                        nr_groups += 1
                        dfs(grid, i_row, i_col)
                        
            groups = {i_group + 1:list() for i_group in range(nr_groups)}
            for i_row in range(m):
                for i_col in range(n):
                    label = grid_labels[i_row][i_col]
                    if label != 0:
                        groups[label].append((i_row, i_col))
            return list(groups.values())


        def get_neighbours(row, col):
            nonlocal m, n
            neighbours = list()
            if row > 0:
                neighbours.append((row-1, col))
            if col > 0:
                neighbours.append((row, col-1))
            if row < m - 1:
                neighbours.append((row+1, col))
            if col < n - 1:
                neighbours.append((row, col+1))
            return neighbours


        m, n = len(grid2), len(grid2[0])
        nr_groups = 0
        visited = [[0] * n for _ in range(m)]
        grid_labels = [[0] * n for _ in range(m)]

        sub_grids = find_subgraph(grid2)
        nr_sub_islands = 0
        for sub_grid in sub_grids:
            if all([grid1[row][col] == 1 for row, col in sub_grid]):
                nr_sub_islands += 1
        return nr_sub_islands

sol = Solution()
cases = [
    {
        "grid1": [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
        "grid2": [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]],
        "expect": 3
    },
    {
        "grid1": [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
        "grid2": [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]],
        "expect": 2
    },
    {
        "grid1": [[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]],
        "grid2": [[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]],
        "expect": 0
    }
]

for case in cases:
    result = sol.countSubIslands(case["grid1"], case["grid2"])
    assert result == case['expect']
