from typing import List
import random
import heapq
from queue import PriorityQueue
import time

class Solution:
    def minStoneSum(self, method, piles, k):
        if method == 'python_sort_sum':
            return self.minStoneSum_python_sort(piles, k)
        elif method == 'python_heap':
            return self.minStoneSum_python_heap(piles, k)
        elif method == 'heap_sum':
            return self.minStoneSum_heap(piles, k)
        elif method == 'priority_queue':
            return self.minStoneSum_priority_queue(piles, k)
        elif method == 'sorted_queue':
            return self.minStoneSum_sorted_queue(piles, k)


    # 8, 6, 4, 2, 0 => 3
    # 0, 4, 2 => 4 > 3
    # 3, 4, 3 => 2 < 3
    # 3, 2

    # 8, 6, 4, 2, 0 => 1
    # 0, 4, 2 => 4 > 1
    # 3, 4, 3 => 2 > 1
    # 4, 4, 4 => 0 < 1
    # 4, 3

    # 8, 6, 4, 2, 0 => 7
    # 0, 4, 2 => 4 < 7
    # 0, 1, 0 => 8 > 7
    # 1, 1, 1 => 6 < 7
    # 1, 0

    def minStoneSum_sorted_queue(self, piles, k):
        piles = sorted(piles, reverse = True)
        n = len(piles)
        for i in range(k):
            target = (piles[0] + 1) >> 1
            left, right = 1, n
            while left < right:
                mid = (left + right) // 2
                if piles[mid] == target:
                    break
                elif target > piles[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            j = 1
            while j < mid:
                piles[j-1] = piles[j]
                j += 1
            piles[mid - 1] = target
            #if target < piles[mid]:
            #    mid += 1
            #piles.insert(mid, target)
        return sum(piles)

    def minStoneSum_priority_queue(self, piles, k):
        my_queue = PriorityQueue()
        for ele in piles:
            my_queue.put((-ele, ele))
        for i in range(k):
            target = my_queue.get()[0] // 2
            my_queue.put((target, - target))

        summ = 0
        while not my_queue.empty():
            _, v = my_queue.get()
            summ += v
        return summ

    def minStoneSum_python_sort(self, piles, k):
        for i in range(k):
            piles = sorted(piles, reverse=True)
            piles[0] = (piles[0] + 1) >> 1
        return sum(piles)

    def minStoneSum_python_heap(self, piles, k):
        piles = [-ele for ele in piles]
        heapq.heapify(piles)
        for i in range(k):
            heapq.heappush(piles, heapq.heappop(piles) // 2)
        return -sum(piles)


    def minStoneSum_heap(self, piles: List[int], k: int) -> int:
        def heapify(arr, i, last_inner, n):
            if i <= last_inner:
                left, max_i = (i << 1) + 1, i; right = left + 1
                if arr[left] > arr[max_i]:
                    max_i = left
                if right < n and arr[right] > arr[max_i]:
                    max_i = right
                if max_i != i:
                    arr[max_i], arr[i] = arr[i], arr[max_i]
                    heapify(arr, max_i, last_inner, n)

        def build_heap(arr, last_inner, n):
            i = last_inner
            while i >= 0:
                heapify(arr, i, last_inner, n)
                i -= 1

        n = len(piles); last_inner = (n >> 1) - 1
        build_heap(piles, last_inner, n)
        for i in range(k):
            piles[0] = (piles[0] + 1) >> 1
            heapify(piles, 0, last_inner, n)
        return sum(piles)


sol = Solution()
cases = [
    {
        "piles": [5, 4, 9],
        "k": 2,
        "expect": 12
    },
    {
        "piles": [4,3,6,7],
        "k": 3,
        "expect": 12
    },
    {
        "piles": [1,6,3,5,8,4,7,2],
        "k": 5,
        "expect": 22
    },
    {
        "piles": [100000] * (10000 - 1) + [100001],
        "k": 1,
        "expect": 999950001
    },
    {
        "piles": [random.randint(1, 10000) for i in range(50000)],
        "k": 1,
    },

]

for method in ['python_sort_sum', 'python_heap', 'heap_sum', 'sorted_queue', 'priority_queue']:
    start = time.time()
    result = [sol.minStoneSum(method, list(case["piles"]), case["k"]) for case in cases[:]]
    print('{}: {} => {}'.format(method, time.time() - start, result))
