from typing import List

def lvp_stack(s):
    stack = list()
    count, longest = 0, 0
    for par in s:
        if par == '(':
            stack.append(0)
        else:
            if not stack:
                # not matched, move to next
                longest = max(count, longest)
                count = 0
            else:
                score = stack.pop()
                if stack:
                    stack[-1] += score + 2
                if not stack:
                    count += score + 2
                    longest = max(count, longest)
    #print(stack, count, longest)
    max_in_stack = max(stack) if stack else 0
    longest = max(count, longest, max_in_stack)
    return longest


def lvp_stack_standard(s):
    stack = [-1]
    len_s = len(s)
    longest = 0
    for i_char in range(len_s):
        ch = s[i_char]
        if ch == '(':
            stack.append(i_char)
        else:
            poped = stack.pop()
            if stack:
                longest = max(i_char - stack[-1], longest)
            else:
                stack.append(i_char)
    return longest


def lvp_dp(s):
    len_s = len(s)
    dp = [0] * len_s
    for i_char in range(1, len_s):
        ch = s[i_char]
        if ch == ')':
            if s[i_char - 1] == '(':
                dp[i_char] = dp[i_char - 2] + 2 if i_char > 1 else 2
            else:
                prev_match_index = i_char - dp[i_char - 1] - 1
                if prev_match_index > -1 and s[prev_match_index] == '(':
                    before_block = dp[prev_match_index - 1] if prev_match_index > 0 else 0
                    dp[i_char] = dp[i_char - 1] + 2 + before_block
                else:
                    dp[i_char] = 0
    return max(dp) if dp else 0


def lvp_pop_and_sort(s):
    # all elements not in the seq and left in queue
    stack = list()
    all_valid = list()
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                poped = stack.pop()
                if s[poped] == '(':
                    all_valid.append(poped)
                    all_valid.append(i)

    sorted_all_valid = sorted(all_valid)
    i_begin = i_end = longest = 0
    for i in range(len(sorted_all_valid) - 1):
        if sorted_all_valid[i_end + 1] != sorted_all_valid[i_end] + 1:
            longest = max(longest, i_end - i_begin + 1)
            i_begin = i_end + 1
        i_end += 1
    longest = max(longest, i_end - i_begin + 1 if i_end > i_begin else 0)
    return longest


def lvp_double_pointers(s):
    left, right = 0, 0
    longest = 0
    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            left += 1
        else:
            right += 1
            if right == left:
                longest = max(left  + right, longest)
            elif right > left:
                right = 0
                left = 0

    left, right = 0, 0
    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch == ')':
            right += 1
        else:
            left += 1
            if right == left:
                longest = max(left + right, longest)
            elif left > right:
                right = 0
                left = 0
    return longest







class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return lvp_double_pointers(s)
sol = Solution()
cases = [
    {
        "input": "(()",
        "expect": 2
    },
    {
        "input": ")()())",
        "expect": 4
    },
    {
        "input": "((()(((()",
        "expect": 2
    },
    {
        "input": "()(())",
        "expect": 6
    }
]

for case in cases:
    result = sol.longestValidParentheses(case["input"])
    print(case["input"], result)
    assert result == case['expect']
