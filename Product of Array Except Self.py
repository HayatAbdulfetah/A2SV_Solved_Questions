class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        product = math.prod(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = 1
                results.append(math.prod(nums))
                nums[i] = 0
            else:
                results.append(product // nums[i])
        
        return results
