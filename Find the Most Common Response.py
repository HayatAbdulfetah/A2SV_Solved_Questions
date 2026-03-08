class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        hashh = {}

        for lst in responses:
            for response in set(lst):
                if response not in hashh:
                    hashh[response] = 1
                else:
                    hashh[response] += 1

        max_count = max(hashh.values())

        equal_values = [key for key, value in hashh.items() if value == max_count]
        
        return min(equal_values)
