from typing import List

def trap_brutal(height): # TLE
    nr_height = len(height)
    score = 0
    for i in range(1, nr_height - 1):
        left_max = right_max = 0
        for j in range(0, i):
            left_max = max(left_max, height[j])
        for j in range(i+1, nr_height):
            right_max = max(right_max, height[j])
        score += max(0, min(left_max, right_max) - height[i])
    return score


def trap_dp(height): # 64ms, 33 MB
    def right_max_helper(i, n, height, seen):
        if i == n:
            return 0
        if seen[i] is None:
            seen[i] = max(height[i], right_max_helper(i+1, n, height, seen))
        return seen[i]
    def left_max_helper(i, height, seen):
        if i == -1:
            return 0
        if seen[i] is None:
            seen[i] = max(height[i], left_max_helper(i - 1, height, seen))
        return seen[i]

    nr_height = len(height)
    seen_right_max = [None] * nr_height
    seen_left_max = [None] * nr_height

    score = 0
    for i in range(1, nr_height - 1):
        right_max = right_max_helper(i + 1, nr_height, height, seen_right_max)
        left_max = left_max_helper(i - 1, height, seen_left_max)
        score += max(min(right_max, left_max) - height[i], 0)
    return score


def trap_dp_optimized(height): # 44ms, 16MB
    nr_height = len(height)
    right_max = [0] * nr_height
    left_max = [0] * nr_height
    score = 0
    for i in range(1, nr_height):
        left_max[i] = max(left_max[i - 1], height[i - 1])
    for i in range(nr_height - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i + 1])
    for i in range(1, nr_height - 1):
        score += max(min(right_max[i], left_max[i]) - height[i], 0)
    return score

def trap_dp_and_pointer(height): # 44ms 16MB
    nr_height = len(height)
    left_max, right_max = 0, 0
    left, right = 0, nr_height
    score = 0
    right_max = [0] * nr_height
    for i in range(nr_height - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i + 1])

    left_max = 0
    for i in range(1, nr_height -1):
        left_max = max(left_max, height[i - 1])
        level = min(left_max, right_max[i])
        score += max(level - height[i], 0)
    return score

def trap_db_pointer(height): # 36 ms, 16MB
    nr_height = len(height)
    left, right = 0, nr_height - 1
    left_max, right_max = 0, 0
    score = 0
    #print('input:', height)
    #print(left, left_max, right, right_max, score)

    while left < right:
        # note here is height[left], height[right]
        # not max_left, max_right
        # one can think it as a maximum search process
        # if right is large, keep moving left
        # if left is large, keep moving right
        # in the end, it always meet at the highest point
        if height[left] < height[right]:
            if height[left] < left_max:
                score += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if height[right] < right_max:
                score += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
        #print(left, left_max, right, right_max, score)
    return score


def trap_horizontal(height): # TLE
    max_height = max(height)
    min_height = min(height)
    nr_height = len(height)
    score = 0
    first_min_height = 0
    last_min_height = nr_height - 1
    for height_level in range(min_height + 1, max_height + 1):
        found_first = found_last = False
        for i in range(first_min_height, nr_height):
            if height[i] >= height_level:
                first_min_height = i
                found_first = True
                break
        for i in range(last_min_height, -1, -1):
            if height[i] >= height_level:
                last_min_height = i
                found_last = True
                break
        if found_first is None or found_last is None:
            break
        for i in range(first_min_height + 1, last_min_height):
            score += 1 if height[i] < height_level else 0
    return score

def trap_mq_optimized(height): # 36ms, 16MB
    nr_height = len(height)
    mq = list()
    score = 0
    for i_height, cur_height in enumerate(height):
        while mq and cur_height > height[mq[-1]]:
            last_level = height[mq.pop()]
            if mq:
                height_level = min(cur_height, height[mq[-1]])
                score += (i_height - mq[-1] - 1) * (height_level - last_level)
        mq.append(i_height)
    return score


def trap_mq(height): # 36ms, 17MB
    nr_height = len(height)
    next_large = [nr_height] * nr_height
    prev_large = [-1] * nr_height
    mq = []
    for i_cur in range(nr_height):
        while mq and height[i_cur] > height[mq[-1]]:
            i_prev = mq.pop()
            next_large[i_prev] = i_cur
        mq.append(i_cur)
    mq = []
    for i_cur in range(nr_height - 1, -1, -1):
        while mq and height[i_cur] > height[mq[-1]]:
            i_prev = mq.pop()
            prev_large[i_prev] = i_cur
        mq.append(i_cur)
    total_score = 0
    prev = None
    for i_cur in range(nr_height):
        left = prev_large[i_cur]
        right = next_large[i_cur]
        if right == nr_height or left == -1:
            if prev:
                level = min(height[prev[0]], height[prev[1]])
                total_score += (prev[1] - prev[0] - 1) *level - sum(height[prev[0] + 1: prev[1]])
                prev = None
        else:
            if prev is None:
                prev = [left, right]
            else:
                prev[0] = min(prev[0], left)
                prev[1] = max(prev[1], right)
    return total_score


class Solution:
    def trap(self, height: List[int], method) -> int:
        return method(height)


sol = Solution()
cases = [
    {
        "input": [9,6,8,6,8,5,7,6,9],
        "expect": 17
    },
    {
        "input": [8,6,8,6,4,6,8,6,4,6,8,6,8],
        "expect": 20
    },
    {
        "input": [9,6,8,8,5,6,3],
        "expect": 3
    },
    {
        "input": [5,4,1,2],
        "expect": 1
    },
    {
        "input": [4,2,3],
        "expect": 1
    },

    {
        "input": [0,1,0,2,1,0,1,3,2,1,2,1],
        "expect": 6
    },
    {
        "input": [4,2,0,3,2,5],
        "expect": 9
    },
]


for method in [trap_mq, trap_brutal, trap_horizontal, trap_dp, trap_dp_optimized, trap_mq_optimized, trap_dp_and_pointer, trap_db_pointer]:
    result = [sol.trap(case["input"], method) for case in cases]
    expected = [case["expect"] for case in cases]
    print(method.__name__, [ f'{pred} <=> {expect}' for expect, pred in zip(expected, result)])
    assert result == expected
