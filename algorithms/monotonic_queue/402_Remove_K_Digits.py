from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = list(map(int, num))
        mono_queue = list()
        j = 0
        while j < len(nums):
            while k and mono_queue and nums[j] < mono_queue[-1]:
                mono_queue.pop()
                k -= 1
            mono_queue.append(nums[j])
            j += 1

        new_nums = mono_queue + nums[j:]
        for _ in range(k):
            new_nums.pop()
        #print(mono_queue, nums[j:], new_nums)
        result = 0
        for ele in new_nums:
            result = result * 10 + ele
        return str(result)

    def removeKdigits_2(self, num: str, k: int) -> str:
        mono_queue = list()
        remains = len(num) - k
        for digit in num:
            while k and mono_queue and digit < mono_queue[-1]:
                mono_queue.pop()
                k -= 1
            mono_queue.append(digit)

        return ''.join(mono_queue[:remains]).lstrip('0') or '0'



sol = Solution()
cases = [
    {
        "num": "1432219",
        "k": 3,
        "expect": "1219"
    },
    {
        "num": "10200",
        "k": 1,
        "expect": "200"
    },
    {
        "num": "10",
        "k": 2,
        "expect": "0"
    },
    {
        "num": "123454321",
        "k": 3,
        "expect": "123321"
    },

    {
        "num": "123456789",
        "k": 3,
        "expect": "123456"
    },
    {
        "num": "987654321",
        "k": 3,
        "expect": "654321"
    },
    {
        "num": "42536117",
        "k": 0,
        "expect": "42536117"
    },
    {
        "num": "42536117",
        "k": 1,
        "expect": "2536117"
    },
    {
        "num": "42536117",
        "k": 2,
        "expect": "236117"
    },
    {
        "num": "42536117",
        "k": 3,
        "expect": "23117"
    },
    {
        "num": "42536117",
        "k": 4,
        "expect": "2117"
    },
    {
        "num": "42536117",
        "k": 5,
        "expect": "117"
    },
    {
        "num": "42536117",
        "k": 6,
        "expect": "11"
    },

]

for case in cases:
    result = sol.removeKdigits_2(case["num"], case['k'])
    print(case["num"], result)
    assert result == case['expect']
