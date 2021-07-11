class Solution:
    def largestOddNumber(self, num: str) -> str:
        ldn = ""
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                ldn = num[:i+1]
                break
        return ldn

sol = Solution()
assert sol.largestOddNumber("420") == ""
assert sol.largestOddNumber("421") == "421"
assert sol.largestOddNumber("5") == "5"
assert sol.largestOddNumber("4210") == "421"
