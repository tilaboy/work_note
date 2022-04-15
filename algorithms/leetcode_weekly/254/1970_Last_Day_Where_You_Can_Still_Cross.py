from typing import List

class UnionSets:
    def __init__(self, elements):
        self.nr_sets = len(elements)
        self.par = [ele for ele in range(self.nr_sets)]
        self.size = [1] * self.nr_sets

    def __repr__(self):
        return f'{self.par} => {self.size}'

    def find(self, x):
        root = x
        while root != self.par[root]:
            root = self.par[root]

        while x != root:
            next_x = self.par[x]
            self.par[x] = root
            x = next_x
        return root

    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x == r_y:
            return

        if self.size[r_x] > self.size[r_y]:
            self.par[r_y] = r_x
            self.size[r_x] = self.size[r_x] + self.size[r_y]
        else:
            self.par[r_x] = r_y
            self.size[r_y] = self.size[r_x] + self.size[r_y]
        self.nr_sets -= 1


class Solution:
    def latestDayToCrossUnionFind(self, row: int, col: int, cells: List[List[int]]) -> int:
        cells = [(cell[0] - 1, cell[1] - 1) for cell in cells]
        terr = [[0] * col for _ in range(row)]
        size_uds = row * col + 2
        uds = UnionSets([i for i in range(size_uds)])
        nr_land = 0
        for i, j in cells[::-1]:
            terr[i][j] = 1
            nr_land += 1
            if i > 0 and terr[i-1][j] == 1:
                uds.union(i * col + j + 1, (i - 1) * col +j +1)
            if i < row - 1 and terr[i+1][j] == 1:
                uds.union(i * col + j + 1, (i + 1) * col +j +1)
            if j > 0 and terr[i][j - 1] == 1:
                uds.union(i * col + j + 1, i * col + j)
            if j < col - 1 and terr[i][j + 1] == 1:
                uds.union(i * col + j + 1, i * col + j + 2)

            if i == 0:
                uds.union(j + 1, 0)
            if i == row - 1:
                uds.union(i * col + j + 1, size_uds - 1)
            if uds.find(0) == uds.find(size_uds - 1):
                break
        return len(cells) - nr_land






    def latestDayToCrossBinarySearch(self, row: int, col: int, cells: List[List[int]]) -> int:
        def reachable(row, col, cells_to_last_move):
            reached = False
            visited = [[0]* col for i in range(row)]
            for x, y in cells_to_last_move:
                visited[x][y] = 1
            for i in range(col):
                if visited[0][i] != 1:
                    if dfs(row, col, 0, i, visited):
                        reached = True
                        break
            return reached

        def dfs(row, col, x, y, visited):
            visited[x][y] = 1
            if x == row - 1:
                return True
            possible_directions = list()
            if x > 0 and visited[x - 1][y] == 0:
                possible_directions.append((x-1, y))
            if x < row - 1 and visited[x + 1][y] == 0:
                possible_directions.append((x+1, y))
            if y > 0 and visited[x][y - 1] == 0:
                possible_directions.append((x, y- 1))
            if y < col - 1 and visited[x][y + 1] == 0:
                possible_directions.append((x, y + 1))
            #print(x, y, 'visited:', visited, 'next to check:', possible_directions)
            return any([dfs(row, col, x, y, visited) for x, y in possible_directions])

        left, right = 0, len(cells) - 1
        conv_cells = [(cell[0] - 1, cell[1] - 1) for cell in cells]
        best = 0
        while left <= right:
            mid = left + (right - left) // 2
            if reachable(row, col, conv_cells[:mid+1]):
                left = best = mid + 1
            else:
                right = mid - 1
        return best

sol = Solution()
cases = [
    {
        "input": [2,2,[[1,1],[2,1],[1,2],[2,2]]],
        "expect": 2
    },
    {
        "input": [2,2,[[1,1],[1,2],[2,1],[2,2]]],
        "expect": 1
    },
    {
        "input": [3,3,[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]],
        "expect": 3
    },
    {
        "input": [6,2,[[4,2],[6,2],[2,1],[4,1],[6,1],[3,1],[2,2],[3,2],[1,1],[5,1],[5,2],[1,2]]],
        "expect": 3
    }
]

for case in cases:
    result = sol.latestDayToCrossUnionFind(case["input"][0], case["input"][1], case["input"][2])
    print(case["input"], result)
    assert result == case['expect']
