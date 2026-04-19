class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = []
        ans = []
        
        for num in reversed(nums):
            ans.append(bisect_left(sorted_list, num))
            insort(sorted_list, num)

        return ans[::-1]
