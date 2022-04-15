from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]], method='dfs') -> List[int]:
        if method == 'dfs':
            return self.hitBricks_dfs(grid, hits)
        if method == 'union':
            return self.hitBricks_union(grid, hits)

    def hitBricks_dfs(self, grid: List[List[int]], hits: List[List[int]]):
        def dfs(i, j, m, n):
            nonlocal grid
            ret = 1
            grid[i][j] = 2
            for direction in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
                new_i, new_j = i + direction[0], j + direction[1]
                if new_i < 0 or new_i >= m  or new_j < 0 or new_j >= n:
                    continue
                if grid[new_i][new_j] == 1:
                    ret += dfs(new_i, new_j, m, n)
            return ret

        def connected(i, j, m, n):
            nonlocal grid
            if i == 0:
                return True
            for direction in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
                new_i, new_j = i + direction[0], j + direction[1]
                if new_i < 0 or new_i >= m  or new_j < 0 or new_j >= n:
                    continue
                if grid[new_i][new_j] == 2:
                    return True
            return False


        m, n = len(grid), len(grid[0])
        for x, y in hits:
            grid[x][y] -= 1
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j, m, n)

        nr_hits = len(hits)
        ret = [0] * nr_hits
        i_hit = nr_hits - 1
        for x, y in hits[::-1]:
            grid[x][y] += 1
            if grid[x][y] == 1 and connected(x, y, m, n):
                ret[i_hit] = dfs(x, y, m, n) - 1
            i_hit -= 1
        return ret



    def hitBricks_union(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def find_root(x):
            nonlocal pa
            root = x
            while root != pa[root]:
                root = pa[root]

            while pa[x] != root:
                next_x = pa[x]
                pa[x] = root
                x = next_x
            return root

        def union_find(x, y):
            nonlocal size, pa
            root_x, root_y = find_root(x), find_root(y)
            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    pa[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    pa[root_x] = root_y
                    size[root_y] += size[root_x]

        def union_around(i, j, m, n):
            nonlocal grid
            for direction in [[0, -1],[0, 1],[-1, 0],[1, 0]]:
                new_i, new_j = i + direction[0], j + direction[1]
                if new_i < 0 or new_i >= m  or new_j < 0 or new_j >= n:
                    continue
                if grid[new_i][new_j] == 1:
                    union_find(i * n + j, new_i * n + new_j)
            if i == 0:
                union_find(j, m * n)

        m, n = len(grid), len(grid[0])
        nr_groups = n * m + 1

        results = list()
        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = 2

        pa = [i for i in range(nr_groups)]
        size = [1] * nr_groups
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    union_around(i, j, m, n)
        nr_bricks = size[find_root(nr_groups - 1)]

        for x, y in hits[::-1]:
            if grid[x][y] == 2:
                grid[x][y] = 1
                union_around(x, y, m, n)
            nr_bricks_new = size[find_root(nr_groups - 1)]
            results.append(max(nr_bricks_new - nr_bricks - 1, 0))
            nr_bricks = nr_bricks_new
        return results[::-1]




sol = Solution()
cases = [
    {
        "grid": [[1,0,0,0],[1,1,1,0]],
        "hits": [[1,0]],
        "expect": [2]
    },
    {
        "grid": [[1,0,0,0],[1,1,0,0]],
        "hits": [[1,1],[1,0]],
        "expect": [0,0]
    },
    {
        "grid": [[1],[1],[1],[1],[1]],
        "hits": [[3,0],[4,0],[1,0],[2,0],[0,0]],
        "expect": [1,0,1,0,0]
    }
]

for case in cases:
    result = sol.hitBricks(case["grid"], case["hits"])
    print(case["grid"], case["hits"], result, "\n")
    assert result == case['expect']
