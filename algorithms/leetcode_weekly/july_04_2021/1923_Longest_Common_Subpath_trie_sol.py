from typing import List
import time
from examples import get_cases

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def find_shortest_path(paths):
            i_shortest = -1
            len_shortest = 10000
            for i in range(len(paths)):
                len_path = len(paths[i])
                if len_path < len_shortest:
                    i_shortest = i
                    len_shortest = len_path
            return i_shortest, len_shortest

        def add_path_to_trie(trie, sub_arr):
            len_arr = len(sub_arr)
            i = 0
            while i < len_arr:
                city = sub_arr[i]
                if city not in trie:
                    trie[city] = dict()
                trie = trie[city]
                i += 1

        def construct_trie(path_arr):
            trie = dict()
            all_sub = list()
            for i in range(len(path_arr)):
                add_path_to_trie(trie, path_arr[i:])
            return trie

        def construct_prefix(path_arr):
            prefix = list()
            for i in range(len(path_arr)):
                prefix.append(path[i:])
            return prefix

        def filter_at_pos(trie, path_arr, i, len_path, new_trie):
            while i < len_path and path_arr[i] in trie:
                city = path_arr[i]
                if city not in new_trie:
                    new_trie[city] = dict()
                new_trie = new_trie[city]
                trie = trie[city]
                i += 1

        def filter_trie(trie, path_arr):
            len_path = len(path_arr)
            i_city = 0
            new_trie = dict()
            while i_city < len_path:
                filter_at_pos(trie, path_arr, i_city, len_path, new_trie)
                i_city += 1
            return new_trie

        def get_trie_longest_path(trie, path_len):
            nonlocal trie_longest_path
            for city in trie:
                if path_len + 1 > trie_longest_path:
                    trie_longest_path = path_len + 1
                get_trie_longest_path(trie[city], path_len + 1)

        i_shortest, len_shortest = find_shortest_path(paths)
        if i_shortest == -1 or len_shortest == 0:
            return 0

        #const_start = time.perf_counter_ns()
        trie = construct_trie(paths[i_shortest])
        #qprint(paths[i_shortest], "=>",trie)
        #const_end = time.perf_counter_ns()
        #print("construct in {} sec".format((const_end - const_start)/1e9))
        for i in range(len(paths)):
            if i == i_shortest:
                continue
            else:
                trie = filter_trie(trie, paths[i])
            #print("after", paths[i], "=>", trie)
        #print("lookup in {} sec".format((time.perf_counter_ns() - const_end)/1e9))

        trie_longest_path = 0
        get_trie_longest_path(trie, 0)
        return trie_longest_path

K = 6
cases = get_cases()
sol = Solution()
start = time.perf_counter_ns()
for case in cases[:K]:
    result = sol.longestCommonSubpath(case["n"], case["input"])
    print(case["n"], case["input"], result)
    assert result == case['expect']
print("durantion: {}".format((time.perf_counter_ns() - start)/1e9))
