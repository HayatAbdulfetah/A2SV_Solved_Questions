class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        l = 0 
        longest = 0

        if len(nums) == 1:
            return 1

        for r in range(len(nums)-1):
            if nums[r] == nums[r+1]:
                l+=1
                longest = max(longest, r-l+2)
                continue

            if nums[r]+1 != nums[r+1]:
                l=r+1

            longest = max(longest, r-l+2)

        return longest

              
