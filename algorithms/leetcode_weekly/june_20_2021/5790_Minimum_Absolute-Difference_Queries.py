from typing import List
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #index_x_nums = {num_i:num for num_i, num in enumerate(nums)}
        #sorted_index = {num_i:num for num_i, num in sorted(index_x_nums.items(), key=lambda x:x[1])}
        result = [-1] * len(queries)
        index_x_queries = {i_query:query for i_query, query in enumerate(queries)}
        sorted_queries = [(i_query, query) for i_query, query in sorted(index_x_queries.items(), key=lambda x: x[1][1] - x[1][0])]
        mem_sets = list()

        for i_query, query in sorted_queries:
            start, end = query
            for mem_start, mem_end, mem_set in mem_sets[::-1]:
                if start == mem_start and end == mem_end:
                    cur_mem_set = mem_set
                    break
                elif start <= mem_start and end >= mem_end:
                    cur_mem_set = set.union(set(nums[start:mem_start]), mem_set, set(nums[mem_end+1:end+1]))
                    mem_sets.append((start, end, cur_mem_set))
                    break
            else:
                cur_mem_set = set(nums[start:end+1])
                mem_sets.append((start, end, cur_mem_set))
            if len(cur_mem_set) == 1:
                result[i_query] = -1
            else:
                queried_array = sorted(list(cur_mem_set))
                min_diff = 101
                for i in range(len(queried_array) - 1):
                    diff = queried_array[i+1] - queried_array[i]
                    if diff == 1:
                        result[i_query] = 1
                        break
                    elif diff < min_diff:
                        min_diff = diff
                if result[i_query] == -1:
                    result[i_query] = min_diff
        return result

sol = Solution()
cases = [
    {
        "nums": [4,5,2,2,7,10],
        "queries": [[2,3],[0,2],[0,5],[3,5]],
        "expect": [-1,1,1,3]
    },
    {
        "nums": [1,3,4,8],
        "queries": [[0,1],[1,2],[2,3],[0,3]],
        "expect": [2,1,4,1]
    },
    {
        "nums": [4,6,2,2,7],
        "queries": [[0,3],[2,4],[0,4],[0,4],[0,3]],
        "expect": [2,5, 1,1,2]
    },

]

for case in cases:
    predict = sol.minDifference(case["nums"], case["queries"])
    print(case["nums"], case["queries"], predict)
    assert predict == case['expect']
