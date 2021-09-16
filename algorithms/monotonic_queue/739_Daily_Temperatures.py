from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nr_temperatures = len(temperatures)
        next_high = [0] * nr_temperatures
        queue_stack = list()

        for i_temp, temp in enumerate(temperatures):
            while queue_stack and temperatures[queue_stack[-1]] < temp:
                prev_i_temp = queue_stack.pop()
                next_high[prev_i_temp] = i_temp - prev_i_temp
            queue_stack.append(i_temp)
        return next_high

sol = Solution()
cases = [
    {
        "input": [73,74,75,71,69,72,76,73],
        "expect": [1,1,4,2,1,1,0,0]
    },
    {
        "input": [30,40,50,60],
        "expect": [1,1,1,0]
    },
    {
        "input": [30,60,90],
        "expect": [1,1,0]
    },
]

for case in cases:
    result = sol.dailyTemperatures(case["input"])
    print(case["input"], result)
    assert result == case['expect']
