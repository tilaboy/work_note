from typing import List

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        reduced_s = list()
        s_index = list()
        for i_char, char in enumerate(s):
            if char in p:
                reduced_s.append(char)
                s_index.append(i_char)
        s = reduced_s
        len_s = len(s)
        len_p = len(p)
        mem = [[None] * (len_s + 1) for i in range(len_p + 1)]

        for i in range(len_p + 1):
            mem[i][-1] = []
        for j in range(len_s + 1):
            mem[-1][j] = []

        for i in range(len_p -1, -1, -1):
            cur_p = p[i]
            min_len = len_p - i
            for j in range(len_s -1, -1, -1):
                if s[j] == cur_p:
                    # mem[i-1][j]
                    # mem[i][j-1]
                    if mem[i+1][j]:
                        mem[i][j] = [[j] + ele for ele in mem[i+1][j]]
                    else:
                        mem[i][j] = [[j]]

                    mem[i][j] = [ele for ele in mem[i][j] + mem[i][j+1] if len(ele) == min_len]
                else:
                    mem[i][j] = mem[i][j+1]

        all_subseq = [[s_index[i_char] for i_char in ele] for ele in mem[0][0]]
        for ele_i, ele in enumerate(removable):
            all_subseq = [arr for arr in all_subseq if ele not in arr]
            if not all_subseq:
                return ele_i
        return ele_i + 1

sol = Solution()
cases = [
    {
        's': "abcacbcdbd",
        'p': "abc",
        'removable': [3,1,0]
    },
    {
        's': "abcacb",
        'p': "ab",
        'removable': [3,1,2]
    },
    {
        's': "abcbddddd",
        'p': "abcd",
        'removable': [3,2,1,4,5,6]
    },
    {
        's': "abcbddddd",
        'p': "abcd",
        'removable': [3,0,1,4,5,6]
    },
    {
        's': "abcab",
        'p': "abc",
        'removable': [0,1,2,3,4]
    },
]
for case in cases:
    result = sol.maximumRemovals(case['s'], case['p'], case['removable'])
    print(case, result)
