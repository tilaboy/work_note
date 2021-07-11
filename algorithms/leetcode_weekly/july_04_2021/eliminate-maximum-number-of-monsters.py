from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        def ceil(d, s):
            if d%s == 0:
                return d // s
            else:
                return d // s + 1

        arrive_time = sorted([ ceil(d, s) for d, s in zip(dist, speed)])
        print(arrive_time)
        count = 0
        for i in range(0, len(arrive_time)):
            count += 1
            if arrive_time[i] >= count:
                pass
            else:
                return arrive_time[i]
        else:
            return count




sol = Solution()
cases = [
    {
        "dist": [1,3,4],
        "speed": [1,1,1],
        "expect": 3
    },
    {
        "dist": [1,1,2,3],
        "speed": [1,1,1,1],
        "expect": 1
    },
    {
        "dist": [3,2,4],
        "speed": [5,3,2],
        "expect": 1
    },
    {
        "dist": [3,5,7,4,5],
        "speed": [2,3,6,3,2],
        "expect": 2
    }
]

for case in cases:
    result = sol.eliminateMaximum(case["dist"], case["speed"])
    print(case["dist"], case["speed"], result)
    assert result == case['expect']
