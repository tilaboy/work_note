from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int], method: str='union_find') -> int:
        if method == 'sort':
            return self.longestConsecutivePythonSort(nums)
        if method == 'heap_sort':
            return self.longestConsecutiveHeapSort(nums)
        elif method == 'union_find':
            return self.longestConsecutiveUnionFind(nums)

    def longestConsecutiveUnionFind(self, nums):
        def find_root(x):
            nonlocal parents
            while x != parents[x]:
                x = parents[x]
            return x

        def union_join(x, y):
            nonlocal size
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x != root_y:
                if size[root_x] > size[root_y]:
                    parents[root_y] = root_x
                    size[root_x] += size[root_y]
                else:
                    parents[root_x] = root_y
                    size[root_y] += size[root_x]

        num_table = dict()
        id = 0
        for num in nums:
            if num not in num_table:
                num_table[num] = id
                id += 1
        nr_uniq_num = len(num_table)
        parents = [ele for ele in range(nr_uniq_num)]
        size = [1] * nr_uniq_num
        i = 0
        for value in num_table:
            if (value - 1) in num_table:
                union_join(num_table[value], num_table[value - 1])
            if (value + 1) in num_table:
                union_join(num_table[value], num_table[value + 1])
            i += 1
        return max(size) if size else 0



    def longestConsecutivePythonSort(self, nums):
        if not nums:
            return 0
        sorted_nums = sorted(nums)
        i, longest_seq, seq_len = 1, 1, 1
        while i < len(sorted_nums):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                seq_len += 1
            elif sorted_nums[i] == sorted_nums[i-1]:
                pass
            else:
                if seq_len > longest_seq:
                    longest_seq = seq_len
                seq_len = 1
            print(i, sorted_nums[i], seq_len, longest_seq)
            i += 1
        if seq_len > longest_seq:
            longest_seq = seq_len
        return longest_seq


    def longestConsecutiveHeapSort(self, nums):
        def heapify(arr, i, nr_ele):
            left = 2 * i + 1
            max_i = i
            if left < nr_ele and arr[left] > arr[i]:
                max_i = left
            if left + 1 < nr_ele and arr[left + 1] > arr[max_i]:
                max_i = left + 1
            if max_i != i:
                arr[i], arr[max_i] = arr[max_i], arr[i]
                heapify(arr, max_i, nr_ele)

        def build_heap(arr, nr_ele):
            i_node = nr_ele // 2 - 1
            while i_node >= 0:
                heapify(arr, i_node, nr_ele)
                i_node -= 1


        nr_ele = len(nums)
        if nr_ele == 0:
            return 0
        build_heap(nums, nr_ele)
        seq_len, longest_seq = 1, 1
        while nr_ele > 1:
            nr_ele -= 1
            nums[0], nums[nr_ele] = nums[nr_ele], nums[0]
            heapify(nums, 0, nr_ele)
            if nums[0] == nums[nr_ele]:
                pass
            elif nums[0] + 1 == nums[nr_ele]:
                seq_len += 1
            else:
                if seq_len > longest_seq:
                    longest_seq = seq_len
                seq_len = 1
        if seq_len > longest_seq:
            longest_seq = seq_len
        return longest_seq

sol = Solution()
cases = [
    {
        "input": [100,4,200,1,3,2],
        "expect": 4
    },
    {
        "input": [0,3,7,2,5,8,4,6,0,1],
        "expect": 9
    },
    {
        "input": [],
        "expect": 0
    },
    {
        "input": [2,0],
        "expect": 1
    },
    {
        "input": [1,2,0,1],
        "expect": 3
    },
    {
        "input": [4,6,7,3,9,5,2,10,1,7,4,11,0,8,6,2,0,1],
        "expect": 12
    },
]

for case in cases:
    result = sol.longestConsecutive(case["input"], 'union_find')
    print(case["input"], result)
    assert result == case['expect']
