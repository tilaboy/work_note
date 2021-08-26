from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]], method='union') -> None:
        if method == 'dfs':
            self.solve_dfs(board)
        elif method == 'bfs':
            self.solve_bfs(board)
        elif method == 'union':
            self.solve_union_find(board)

    def solve_union_find(self, board):
        def find_root(x):
            nonlocal pa
            root = x
            while root != pa[root]:
                root = pa[root]

            while x != root:
                next_x = pa[x]
                pa[x] = root
                x = next_x
            return root

        def union_find(x, y):
            nonlocal pa
            nonlocal size
            root_x, root_y = find_root(x), find_root(y)

            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    pa[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    pa[root_x] = root_y
                    size[root_y] += size[root_x]

        def map_arr(x, y):
            nonlocal n
            return x * n + y

        m, n = len(board), len(board[0])
        arr_size = m * n + 1
        pa = [i for i in range(arr_size)]
        size = [1] * arr_size

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'X':
                    continue
                if i < m - 1 and board[i + 1][j] == 'O':
                    union_find(map_arr(i, j), map_arr(i + 1, j))
                if j < n - 1 and board[i][j + 1] == 'O':
                    union_find(map_arr(i, j), map_arr(i, j + 1))
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    union_find(map_arr(i, j), arr_size - 1)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and find_root(map_arr(i,j)) != find_root(arr_size - 1):
                    board[i][j] = 'X'


    def solve_dfs(self, board):
        def dfs(i, j, m, n, visited):
            nonlocal board
            visited[i][j] = 1
            possible_cells = list()
            if i > 0 and board[i - 1][j] == 'O':
                possible_cells.append((i - 1, j))
            if i < m - 1 and board[i + 1][j] == 'O':
                possible_cells.append((i + 1, j))
            if j > 0 and board[i][j - 1] == 'O':
                possible_cells.append((i, j - 1))
            if j < n - 1 and board[i][j + 1] == 'O':
                possible_cells.append((i, j + 1))
            for x, y in possible_cells:
                if visited[x][y] == 0:
                    dfs(x, y, m, n, visited)

        m, n = len(board), len(board[0])
        boundaries = [(0, j)     for j in range(n - 1)] + \
                     [(i, n - 1) for i in range(m - 1)] + \
                     [(m - 1, j) for j in range(1, n)] + \
                     [(i, 0) for i in range(1, m)]
        visited = [[0] * n for _ in range(m)]
        for cell_x, cell_y in boundaries:
            if board[cell_x][cell_y] == "O" and not visited[cell_x][cell_y]:
                dfs(cell_x, cell_y, m, n, visited)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'


    def solve_bfs(self, board):
        m, n = len(board), len(board[0])
        boundaries = [(0, j)     for j in range(n - 1)] + \
                     [(i, n - 1) for i in range(m - 1)] + \
                     [(m - 1, j) for j in range(1, n)] + \
                     [(i, 0) for i in range(1, m)]
        visited = [[0] * n for _ in range(m)]
        for cell_x, cell_y in boundaries:
            if board[cell_x][cell_y] == "O" and not visited[cell_x][cell_y]:
                q = deque([(cell_x, cell_y)])
                while q:
                    i, j = q.popleft()
                    visited[i][j] = 1
                    possible_cells = list()
                    if i > 0 and board[i - 1][j] == 'O':
                        possible_cells.append((i - 1, j))
                    if i < m - 1 and board[i + 1][j] == 'O':
                        possible_cells.append((i + 1, j))
                    if j > 0 and board[i][j - 1] == 'O':
                        possible_cells.append((i, j - 1))
                    if j < n - 1 and board[i][j + 1] == 'O':
                        possible_cells.append((i, j + 1))
                    for cell in possible_cells:
                        if visited[cell[0]][cell[1]] == 0:
                            q.append(cell)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'


sol = Solution()
cases = [
    {
        "input": [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        "expect": [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    },
    {
        "input": [["X"]],
        "expect": [["X"]]
    },
    {
        "input": [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]],
        "expect": [["X","O","X","O","X","O"],["O","X","X","X","X","X"],["X","X","X","X","X","O"],["O","X","O","X","O","X"]]
    },
    {
        "input": [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]],
        "expect": [["X","O","X","X"],["O","X","X","X"],["X","X","X","O"],["O","X","X","X"],["X","X","X","O"],["O","X","O","X"]],
    }
]

for case in cases:
    input_board = [list(row) for row in case["input"]]
    sol.solve(input_board)
    print(case["input"], input_board)
    assert input_board == case['expect']
