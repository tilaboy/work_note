from typing import List

def lra_mq(heights):
    nr_heights = len(heights)
    mq = list()
    forward_min = [nr_heights] * nr_heights
    for i_height, height in enumerate(heights):
        while mq and height < heights[mq[-1]]:
            last_i_mq_height = mq.pop()
            forward_min[last_i_mq_height] = i_height
        mq.append(i_height)

    mq = list()
    backward_min = [-1] * nr_heights
    for i_height in range(nr_heights - 1, -1, -1):
        height = heights[i_height]
        while mq and height < heights[mq[-1]]:
            last_i_mq_height = mq.pop()
            backward_min[last_i_mq_height] = i_height
        mq.append(i_height)

    #print(forward_min)
    #print(backward_min)
    #print([height * (forward_min[i_height] - backward_min[i_height] - 1) for i_height, height in enumerate(heights)])
    return max([height * (forward_min[i_height] - backward_min[i_height] - 1) for i_height, height in enumerate(heights)])



def lra_dp(heights, i, j, seen):
    if (i, j) in seen:
        return seen[(i, j)]
    if i == j:
        seen[(i, j)] = (heights[i], heights[i])
    else:
        lra_left, min_left = lra_dp(heights, i + 1, j, seen)
        lra_right, min_right = lra_dp(heights, i, j - 1, seen)
        min_height = min(min_right, min_left)
        max_span = min(heights[i], min_left) * (j - i + 1)
        seen[(i, j)] = (max(lra_left, lra_right, max_span), min_height)
    return seen[(i, j)]


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #lra, min_value = lra_dp(heights, 0, len(heights) - 1, dict())
        #return lra
        return lra_mq(heights)

sol = Solution()
cases = [
    {
        "heights": [2,1,5,6,2,3],
        "expect": 10
    },
    {
        "heights": [4,2,5,6,2,3],
        "expect": 12
    },
    {
        "heights": [4,3,2,5,8,6,7,2,3],
        "expect": 20
    },
    {
        "heights": [2,4],
        "expect": 4
    },
    {
        "heights": [6,7,5,2,4,5,9,3],
        "expect": 16
    }
]

for case in cases:
    result = sol.largestRectangleArea(case["heights"])
    print(case["heights"], result)
    assert result == case['expect']
