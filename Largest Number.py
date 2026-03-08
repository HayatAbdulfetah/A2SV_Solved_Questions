class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert numbers to strings for concatenation comparisons
        nums = [str(i) for i in nums]
    
        nums.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(nums)

        if result[0] == "0":
            return "0"
        else:
            return result
