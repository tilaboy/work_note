from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        len_s, i, nr_words, i_word = len(s), 0, len(words), 0
        while i < len_s:
            if i_word == nr_words:
                return False
            len_word = len(words[i_word])
            if words[i_word] == s[i: i+len_word]:
                i = i+len_word
                i_word += 1
            else:
                return False
        return True


sol = Solution()
cases = [
    {
        "s": "iloveleetcode",
        "words": ["i","love","leetcode","apples"],
        "expect": True
    },
    {
        "s": "iloveleetcode",
        "words": ["i","love", "leet"],
        "expect": False
    },
    {
        "s": "iloveleetcode",
        "words": ["apples","i","love","leetcode"],
        "expect": False
    },
]

for case in cases:
    result = sol.isPrefixString(case["s"], case["words"])
    print(case, result)
    assert result == case['expect']
