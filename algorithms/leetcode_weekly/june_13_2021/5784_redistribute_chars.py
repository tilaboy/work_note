from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        nr_words = len(words)
        char_count = dict()
        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1

        for char, count in char_count.items():
            if count % nr_words != 0:
                return False
        else:
            return True



sol = Solution()
cases = [["abc","aabc","bc"], ["ab","a"]]
for case in cases:
    result = sol.makeEqual(case)
    print(case, result)
