class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        indix = {}
        for i, num in enumerate(sorted_nums):
            if num not in indix:
                indix[num] = i
                
        result = []
        for num in nums:
            result.append(indix[num])

        return result
