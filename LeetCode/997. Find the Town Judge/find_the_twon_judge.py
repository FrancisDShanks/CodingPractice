class Solution(object):
    def findJudge(self, N, trust):
        # just calculate the in-degree and out-degree
        # inital all degree[i] as 0
        # if i has one in-degree edge, degree[i] - 1
        # if i has one out-degree edge, degree[i] + 1
        # the judge, if exists, should be the only one whose degree is N-1
        if N == 1:
            return 1
        degree = [0] * (N+1)
        for a, b in trust:
            degree[a] -= 1
            degree[b] += 1
        if degree.count(N-1) != 1:
            return -1
        j = degree.index(N-1)
        return j
