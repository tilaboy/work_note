import sys
from typing import List
import time
import collections
from examples import get_cases

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        return self.lcs_sa(n, paths)

    def lcs_sa(self, n, paths) -> int:
        def suffix_array_std(arr):
            len_s = len(arr)
            p, c = [0] * len_s,  [0] * len_s
            dist, k = 0, 0
            while dist < len_s:
                work_arr = list(arr) if k == 0 else [
                    (c[i], c[(i+dist) % len_s])
                    for i in range(len_s)
                ]
                p = sorted(range(len_s), key=work_arr.__getitem__)
                c[p[0]] = 0
                for i in range(1, len_s):
                    if work_arr[p[i]] != work_arr[p[i-1]]:
                        c[p[i]] = c[p[i-1]] + 1
                    else:
                        c[p[i]] = c[p[i-1]]
                if c[p[i]] == len_s - 1:
                    break
                k += 1
                dist = 1 << (k - 1)
            return p

        def suffix_array_radix_improve(arr):
            len_s = len(arr)
            dist, k, c = 0, 0, [0] * len_s

            cur_p = pre_p = 0
            while dist < len_s:
                if k == 0:
                    p = sorted(range(len_s), key=arr.__getitem__)
                    for i in range(1, len_s):
                        cur_p = p[i]
                        pre_p = p[i-1]
                        c[cur_p] = c[pre_p] + 1 if arr[cur_p] != arr[pre_p] else c[pre_p]
                else:
                    count, pos, p_new, c_new = [0] * len_s, [0] * len_s, [0] * len_s, [0] * len_s
                    for i in range(len_s):
                        count[c[i]] += 1
                    for i in range(1, len_s):
                        pos[i] = pos[i-1] + count[i-1]
                    for i in p:
                        new_i = (i-dist) % len_s
                        score = c[new_i]
                        p_new[pos[score]] = new_i
                        pos[score] += 1
                    p = p_new
                    for i in range(1, len_s):
                        cur_p = p[i]
                        pre_p = p[i-1]
                        cur = (c[cur_p], c[(cur_p + dist) % len_s])
                        prev = (c[pre_p], c[(pre_p + dist) % len_s])
                        c_new[cur_p] = c_new[pre_p] + 1 if cur != prev else c_new[pre_p]
                    c = c_new
                if c[cur_p] == len_s - 1:
                    break
                k += 1
                dist = 1 << (k - 1)
            return p

        def lcp(sa, arr):
            len_s = len(arr)
            lcp_arr, rank_t = [0] * len_s, [0] * len_s
            for rank, index in enumerate(sa):
                rank_t[index] = rank
            k = 1
            for cur in range(0, len_s):
                if rank_t[cur] == 0:
                    continue
                prev, k = sa[rank_t[cur] - 1], max(k - 1, 0)
                while max(prev, cur) + k < len_s and arr[prev + k] == arr[cur + k]:
                    k += 1
                lcp_arr[rank_t[cur]] = k
            return lcp_arr

        def longest_k_lcs(lcp_arr, i_paths, sa, m):
            left, right, op = m, m, 'expand'
            paths_in_window = {i:0 for i in range(1, m + 1)}
            nr_paths_in_window = 0
            score_count = dict()
            lcp_in_window, max_lcp = None, 0

            while right < len(lcp_arr):
                if op == 'expand':
                    i_path = i_paths[sa[right]]
                    if paths_in_window[i_path] == 0:
                        nr_paths_in_window += 1
                    paths_in_window[i_path] += 1
                    if right > left:
                        score_count[lcp_arr[right]] = score_count.get(lcp_arr[right] , 0) + 1
                        if lcp_in_window is None:
                            lcp_in_window = lcp_arr[right]
                        elif lcp_arr[right] < lcp_in_window:
                            lcp_in_window = lcp_arr[right]
                else:
                    prev_left = left - 1
                    i_path = i_paths[sa[prev_left]]
                    if paths_in_window[i_path] == 1:
                        nr_paths_in_window -= 1
                    paths_in_window[i_path] -= 1
                    score_count[lcp_arr[left]] -= 1
                    if score_count[lcp_arr[left]] == 0:
                        score_count.pop(lcp_arr[left])
                    if lcp_in_window not in score_count:
                        if score_count:
                            lcp_in_window = min(score_count.keys())
                        else:
                            lcp_in_window = None
                #print(left, right, op, lcp_arr[left : right + 1], score_count, paths_in_window, nr_paths_in_window, lcp_in_window, max_lcp)
                if nr_paths_in_window == m:
                    # can also use a hash to count each lcp score, but a bit slower with python
                    #lcp_in_window = min(lcp_arr[left+1:right+1])

                    if lcp_in_window > max_lcp:
                        max_lcp = lcp_in_window
                    left += 1
                    op = 'shrink'
                else:
                    right += 1
                    op = 'expand'
            return max_lcp

        i = -1
        arr, i_paths, nr_paths = list(), list(), len(paths)
        for path in paths:
            arr.extend(path)
            arr.append(i)
            i_paths.extend([-i] * len(path))
            i_paths.append(i)
            i -= 1
        sa = suffix_array_radix_improve(arr)
        lcp_arr = lcp(sa, arr)
        #for i in range(len(arr)):
        #    print('{:3d} {:5d} {:5d} {:5d} {:5d} {:5d} {:5d}'.format(i, arr[i], i_paths[i], sa[i], arr[sa[i]], i_paths[sa[i]], lcp_arr[i]) )
        result = longest_k_lcs(lcp_arr, i_paths, sa, nr_paths)
        #print('lcs', result)
        return result

    def lcs_rolling_hash(self, n, paths) -> int:
        def rolling_hash_path(path, w_size, base, p):
            pos, rh, f_power = 0, 0, pow(base, w_size, p)
            while pos < w_size:
                rh = ((rh * base) + path[pos]) % p
                pos += 1
            seen = collections.defaultdict(list)
            seen[rh].append((0, pos))
            while pos < len(path):
                start = pos - w_size
                rh = ((rh * base - path[start] * f_power ) % p + path[pos]) % p
                start, pos, recorded = start + 1, pos + 1, False

                if rh in seen:
                    for p_begin, p_end in seen[rh]:
                        if path[start:pos] == path[p_begin:p_end]:
                            recorded = True
                if not recorded:
                    seen[rh].append((start, pos))
            return seen

        def find_rolling_hash(paths, w_size, n, p):
            path_hash = rolling_hash_path(paths[0], w_size, n, p)
            for cur_path in paths[1:]:
                new_seen = rolling_hash_path(cur_path, w_size, n, p)
                overlaped = dict()
                for hash_key in path_hash:
                    if hash_key in new_seen:
                        seqs = [cur_path[start:end] for start, end in new_seen[hash_key]]
                        overlaped[hash_key] = [
                            (start, end)
                            for start, end in path_hash[hash_key]
                            if paths[0][start:end] in seqs
                        ]
                        if not overlaped[hash_key]:
                            overlaped.pop(hash_key)
                if not overlaped:
                    return False
                else:
                    path_hash = overlaped
            return True if path_hash else False

        min_len = min([len(path) for path in paths])
        left, right, lcs = 0, min_len, 0
        while left <= right:
            mid = left + (right - left)// 2
            if find_rolling_hash(paths, mid, n, 2 ** 32 - 1):
                lcs, left = mid, mid + 1
            else:
                right = mid - 1
        return lcs


sol = Solution()
cases = get_cases()
K = 8
expects = [case['expect'] for case in cases[:K]]
start = time.perf_counter_ns()
#print(sol.longestCommonSubpath(5, [[0,1,2,3,4], [2,3,4], [4,0,1,2,3]]))
solutions = [sol.longestCommonSubpath(case["n"], case["input"]) for case in cases[:K]]
print("durantion: {}".format((time.perf_counter_ns() - start)/1e9))
assert solutions == expects
