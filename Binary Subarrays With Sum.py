class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {0: 1}
        prefix = 0
        count = 0

        for num in nums:

            prefix += num
            key = prefix 
            complement = key - goal 

            if complement in seen:
                count += seen[complement]

            seen[key] = seen.get(key,0) + 1

        return count
