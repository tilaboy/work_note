from typing import List


# https://leetcode.com/problems/distinct-subsequences/

def direct_helper(cur_str, str_len, i, s_arr, t, len_s, len_t):
    if str_len == len_t and cur_str == t:
        return 1
    if str_len > len_t or i == len_s or len_s - i < len_t - str_len:
        return 0
    return direct_helper(cur_str, str_len, i+1, s_arr, t, len_s, len_t) + \
    direct_helper(cur_str + s_arr[i], str_len + 1, i+1, s_arr, t, len_s, len_t)


def numDisDirect(s, t):
    t_dict = {c:1 for c in t}
    s_arr = [c for c in s if c in t_dict]
    len_s, len_t = len(s_arr), len(t)
    if len_s < len_t:
        return 0
    return direct_helper('', 0, 0, s_arr, t, len_s, len_t)


def numDisRecur(s, t, i, j, seen):
    if j == len(t):
        return 1
    if i == len(s):
        return 0

    if (i, j) in seen:
        return seen[(i, j)]

    if (i+1, j) not in seen:
        seen[(i+1, j)]=  numDisRecur(s, t, i+1, j, seen)

    if s[i] == t[j]:
        if (i+1, j+1) not in seen:
            seen[(i+1, j+1)]=  numDisRecur(s, t, i+1, j+1, seen)
        return seen[(i+1, j)] + seen[(i+1, j+1)]
    else:
        return seen[(i+1, j)]


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return numDisRecur(s,t, 0, 0, {})


sol = Solution()
cases = [
    {
        "s": "rabbbit",
        "t": "rabbit",
        "expect": 3
    },
    {
        "s": "babgbag",
        "t": "bag",
        "expect": 5
    },
]

for case in cases:
    result = sol.numDistinct(case["s"], case["t"])
    print(case["s"], case["t"], result)
    assert result == case['expect']
