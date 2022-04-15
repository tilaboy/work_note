from typing import List
from collections import deque


class Solution:
    def swimInWater(self, grid: List[List[int]], method='pq') -> int:
        '''if and only if the elevation of both squares individually are at most t'''
        if method == 'bfs':
            return self.swimInWaterBfs(grid)
        if method == 'dfs':
            return self.swimInWaterDfs(grid)
        if method == 'union_find':
            return self.swimInWaterUF(grid)
        if method == 'pq':
            return self.swimInWaterPQ(grid)

    def swimInWaterPQ(self, grid):
        def heapify(i, arr):
            i_left = i * 2 + 1
            i_right = i_left + 1
            i_min = i
            if i_left < len(arr) and arr[i_min][0] > arr[i_left][0]:
                i_min = i_left
            if i_right < len(arr) and arr[i_min][0] > arr[i_right][0]:
                i_min = i_right
            if i_min != i:
                arr[i], arr[i_min] = arr[i_min], arr[i]
                heapify(i_min, arr)

        def heap_update(i, arr):
            pa = (i - 1) // 2
            if pa >=0 and arr[pa] > arr[i]:
                arr[pa], arr[i] = arr[i], arr[pa]
                heap_update(pa, arr)

        n = len(grid)
        visited = [[0] * n for _ in range(n)]
        pq = [(grid[0][0], 0, 0)]
        highest = 0
        while pq:
            pq[-1], pq[0] = pq[0], pq[-1]
            elevation, x, y = pq.pop()
            heapify(0, pq)
            if elevation > highest:
                highest = elevation
            if x == n-1 and y == n-1:
                break
            visited[x][y] = 1
            for dir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_x = x + dir[0]
                new_y = y + dir[1]
                if -1 < new_x < n and -1 < new_y < n and visited[new_x][new_y] == 0:
                    pq.append((grid[new_x][new_y], new_x, new_y))
                    heap_update(len(pq) - 1, pq)
        return highest






    def swimInWaterUF(self, grid):
        def find(x):
            nonlocal pa
            while x != pa[x]:
                x = pa[x]
            return x

        def union(x, y):
            nonlocal size
            nonlocal pa
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    pa[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    pa[root_x] = root_y
                    size[root_y] += size[root_x]

        n = len(grid)
        left, right = 0, n * n - 1
        lowest_swim = n * n
        while left <= right:
            mid = left + (right - left) // 2
            pa = [i for i in range(n*n)]
            size = [1 for _ in range(n*n)]
            for i in range(n):
                new_i = i + 1
                for j in range(n):
                    if grid[i][j] > mid:
                        continue
                    new_j = j + 1
                    if new_i < n and grid[new_i][j] <= mid:
                        union(i * n + j, new_i * n + j)
                    if new_j < n and grid[i][new_j] <= mid:
                        union(i * n + j, i * n + new_j)
            if find(0) == find(n * n - 1):
                right = mid - 1
                lowest_swim = mid
            else:
                left = mid + 1
        return lowest_swim



    def swimInWaterDfs(self, grid):
        def dfs(x, y, n, water_depth, visited):
            nonlocal grid
            visited[x][y] = 1
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for di in dirs:
                new_x = x + di[0]
                new_y = y + di[1]
                if n > new_x > -1 and n > new_y > -1:
                    if visited[new_x][new_y] == 0 and grid[new_x][new_y] <= water_depth:

                        dfs(new_x, new_y, n, water_depth, visited)

        n = len(grid)
        left, right = 0, n * n - 1
        lowest_swim = n * n
        while left <= right:
            mid = left + (right - left) // 2
            visited = [[0] * n for _ in range(n)]
            if grid[0][0] <= mid:
                dfs(0, 0, n, mid, visited)
            if visited[n - 1][n - 1]:
                right = mid - 1
                lowest_swim = mid
            else:
                left = mid + 1
        return lowest_swim

    def swimInWaterBfs(self, grid):
        def bfs(i, j, n, water_depth, visited):
            nonlocal grid
            nr_step = 0
            cur_step_eles = 0
            cell_queue_x = deque()
            cell_queue_y = deque()
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            if grid[0][0] <= water_depth:
                cell_queue_x.append(0)
                cell_queue_y.append(0)
                cur_step_eles = 1
            while cell_queue_x:
                x = cell_queue_x.popleft()
                y = cell_queue_y.popleft()
                visited[x][y] = 1
                cur_step_eles -= 1
                for di in dirs:
                    new_x = x + di[0]
                    new_y = y + di[1]
                    if n > new_x > -1 and n > new_y > -1:
                        if visited[new_x][new_y] == 0 and grid[new_x][new_y] <= water_depth:
                            cell_queue_x.append(new_x)
                            cell_queue_y.append(new_y)
                if cur_step_eles == 0:
                    nr_step += 1
                    cur_step_eles = len(cell_queue_x)

        n = len(grid)
        left, right = 0, n * n - 1
        lowest_swim = n * n
        while left <= right:
            mid = left + (right - left) // 2
            visited = [[0] * n for _ in range(n)]
            bfs(0, 0, n, mid, visited)
            if visited[n-1][n-1]:
                right = mid - 1
                lowest_swim = mid
            else:
                left = mid + 1
        return lowest_swim




sol = Solution()
cases = [
    {
        "input": [[0,2],[1,3]],
        "expect": 3
    },
    {
        "input": [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]],
        "expect": 16
    },
    {
        "input": [[3,2],[0,1]],
        "expect": 3
    }
]

for case in cases:
    result = sol.swimInWater(case["input"])
    print(case["input"], result)
    assert result == case['expect']
