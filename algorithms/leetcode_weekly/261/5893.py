from typing import List

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        total_nr_ch = 0
        len_s = len(s)
        for ch in s:
            if ch == letter:
                total_nr_ch += 1
        total_to_remove = len_s - k
        nr_letter_to_remove = total_nr_ch - repetition
        nr_letter_in_mq = 0
        mq = list()

        for i_ch, ch in enumerate(s):
            while mq and total_to_remove and ch < s[mq[-1]] :
                if s[mq[-1]] == letter:
                    if nr_letter_to_remove == 0:
                        break
                    else:
                        nr_letter_in_mq -= 1
                        nr_letter_to_remove -= 1
                mq.pop()
                total_to_remove -= 1
            while mq and ch == letter and len(mq) - nr_letter_in_mq + repetition > k:
                mq.pop()
            if ch == letter:
                nr_letter_in_mq += 1
            mq.append(i_ch)
        chars = [s[i_ch] for i_ch in mq[:k]]
        return ''.join(chars)

sol = Solution()
cases = [
    {
        "s": "bb",
        "k": 2,
        "letter": "b",
        "repetition": 2,
        "expect": "bb"
    },
    {
        "s": "leetcode",
        "k": 4,
        "letter": "e",
        "repetition": 2,
        "expect": "ecde"
    },
    {
        "s": "leet",
        "k": 3,
        "letter": "e",
        "repetition": 1,
        "expect": "eet"
    },
    {
        "s": "aaabbbcccddd",
        "k": 3,
        "letter": "b",
        "repetition": 2,
        "expect": "abb"
    },
    {
        "s": "bezzzzzszvvwxxxz",
        "k": 7,
        "letter": "z",
        "repetition": 5,
        "expect": "bezzzzz"
    }
]

for case in cases:
    result = sol.smallestSubsequence(case["s"], case["k"], case["letter"], case["repetition"])
    print(result)
    assert result == case['expect']
