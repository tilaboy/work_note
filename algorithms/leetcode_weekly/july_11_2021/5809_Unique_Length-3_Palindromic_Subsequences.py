from typing import List

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        tri_strings = dict()
        len_s = len(s)
        i = 1
        left = dict()
        right = dict()
        while i < len_s - 1:
            cur_char = s[i]
            if i == 1:
                left = {s[0]: 1}
                for j in range(2, len_s):
                    right[s[j]] = right.get(s[j], 0) + 1
            else:
                left_char = s[i-1]
                left[left_char] = left.get(left_char, 0) + 1
                if right[cur_char] == 1:
                    right.pop(cur_char)
                else:
                    right[cur_char] = right[cur_char] - 1
            print(i, left, right)

            for left_char in left:
                if left_char in right:
                    tri_string = left_char + cur_char + left_char
                    if tri_string not in tri_strings:
                        tri_strings[tri_string] = 1
            i += 1
        print(tri_strings)
        return len(tri_strings)


sol = Solution()
cases = [
    {
        "input": "aabca",
        "expect": 3
    },
    {
        "input": "abc",
        "expect": 0
    },
    {
        "input": "aba",
        "expect": 1
    },
    {
        "input": "aaa",
        "expect": 1
    },
    {
        "input": "bbcbaba",
        "expect": 4
    },
]

for case in cases:
    result = sol.countPalindromicSubsequence(case["input"])
    print(case["input"], result)
    assert result == case['expect']
