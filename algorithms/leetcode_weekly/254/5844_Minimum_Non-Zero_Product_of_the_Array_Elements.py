from typing import List

'''
1

01
10
11

001
010
011
100
101
110
111

0001
0011
0101
0111
1001
1011
1101
0010
0100
0110
1000
1010
1100
1110
1111


fast power:
 2^10
 4^5
 8^2 * 8^2 * 4
'''

class Solution:
    def minNonZeroProduct(self, p: int):
        def fast_power(a, p, modular):
            if p == 1:
                return a
            elif p % 2 == 0:
                return fast_power((a*a) % modular, p // 2, modular) % modular
            else:
                return fast_power((a*a) % modular, p // 2, modular) * a % modular
        if p == 1:
            return 1
        else:
            modular = 10 ** 9 + 7
            largest = ( 1 << p ) - 1
            return largest * fast_power(largest - 1, largest //2, modular) % modular

sol = Solution()
cases = [
    {
        "input": 1,
        "expect": 1
    },
    {
        "input": 2,
        "expect": 6
    },
    {
        "input": 3,
        "expect": 1512
    },
    {
        "input": 4,
        "expect": 581202553
    },
]

for case in cases:
    result = sol.minNonZeroProduct(case["input"])
    print(case["input"], result)
    assert result == case['expect']
