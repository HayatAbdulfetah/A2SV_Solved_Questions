class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
        # count = Counter(nums)
        # for num in count:
        #     if count[num] > 1:
        #         return True
        # return False
