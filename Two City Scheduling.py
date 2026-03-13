class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        difference = []
        result = 0
        for c1, c2 in costs:
            difference.append([c1-c2, c1, c2])

        difference.sort()
        n = len(difference)

        for i in range(n):
            if i < n//2:
                result += difference[i][1]
            else:
                result += difference[i][2]

        return result
