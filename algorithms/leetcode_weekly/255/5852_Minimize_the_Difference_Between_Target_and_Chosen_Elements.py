from typing import List

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:

        def dp(i, m, n, target, seen):
            nonlocal sorted_mat
            if (i, target) in seen:
                return seen[(i, target)]
            if i == m:
                return abs(target)
            else:
                if target < 0:
                    seen[(i, target)] = dp(i + 1, m, n, target - sorted_mat[i][0], seen)
                else:
                    min_diff = 5000
                    for j in range(n):
                        diff = dp(i + 1, m, n, target - sorted_mat[i][j], seen)
                        if diff == 0:
                            return diff
                        if diff < min_diff:
                            min_diff = diff
                    seen[(i, target)] = min_diff
            return seen[(i, target)]

        # dynamic prog
        sorted_mat = [sorted(arr) for arr in mat]
        m, n = len(mat), len(mat[0])
        seen = dict()
        min_score = dp(0, m, n, target, seen)
        return min_score



sol = Solution()
cases = [
    {
        "mat": [[1,2,9,8,7]],
        "target": 6,
        "expect": 1
    },
    {
        "mat": [[1],[2],[3]],
        "target": 100,
        "expect": 94
    },
    {
        "mat": [[1,2,3],[4,5,6],[7,8,9]],
        "target": 13,
        "expect": 0
    },
    {
        "mat": [[65],[45],[45],[69],[55],[60],[29],[25],[16],[5],[62],[16],[29],[19],[34],[2],[24],[32],[66],[62],[60],[46],[42],[37],[51],[4],[41],[4],[66],[20],[9],[4],[66],[6],[56],[10],[51],[44],[7],[8],[5],[44],[28],[7],[10],[7],[24],[62],[19],[14],[45],[68],[9],[14],[51],[28],[8],[57],[59],[6],[54],[8],[19],[16],[63],[45],[33],[15],[33],[67]],
        "target": 800,
        "expect": 1510
    }
]

for case in cases:
    result = sol.minimizeTheDifference(case["mat"], case["target"])
    print(case["mat"], case["target"], result)
    assert result == case['expect']
