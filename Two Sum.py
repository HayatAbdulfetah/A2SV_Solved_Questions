class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        for i in range(1, len(nums)):
            if nums[i] + nums[left] == target:
                    return [left , i]
            else:
                left += 1
                if left < i and nums[i] + nums[left] == target:
                    return [left, i]
            

        return []
