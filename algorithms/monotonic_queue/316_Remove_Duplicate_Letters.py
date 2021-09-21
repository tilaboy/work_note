from typing import List

def rdl_brutal(s):
    char_mapping = dict()
    uniq_chars = set([ch for ch in s])
    for i_ch, ch in enumerate(s):
        if ch in char_mapping:
            char_mapping[ch].append(i_ch)
        else:
            char_mapping[ch] = [i_ch]
    prev_possible_sol = [[]]
    for ch in uniq_chars:
        possible_sol = list()
        for i_ch in char_mapping[ch]:
            possible_sol.extend([sol + [[i_ch, ch]] for sol in prev_possible_sol])
        prev_possible_sol = possible_sol
    possible_sol = [[ch for i_ch, ch in sorted(sol)] for sol in possible_sol]
    return min(possible_sol)


def rdl_mq(s):
    len_s = len(s)
    mq = list()
    s_count = dict()
    for ch in s:
        s_count[ch] = s_count.get(ch, 0) + 1
    for i in range(len_s):
        if s[i] in mq:
            s_count[s[i]] -= 1
            continue
        while mq and s[i] < mq[-1]:
            if s_count[mq[-1]] == 0:
                break
            mq.pop()
        mq.append(s[i])
        s_count[s[i]] -= 1
    return ''.join(mq)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return rdl_mq(s)

sol = Solution()
cases = [
    {
        "input": "cbacdcbc",
        "expect": "acdb"
    },
    {
        "input": "bcabc",
        "expect": "abc"
    },
]

for case in cases:
    result = sol.removeDuplicateLetters(case["input"])
    print(case["input"], result)
    assert result == case['expect']
