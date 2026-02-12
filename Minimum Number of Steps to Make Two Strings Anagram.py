class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        steps = 0

        for i in s_count:
            if s_count[i] > t_count[i]:
                steps += s_count[i] - t_count[i]

        return steps
