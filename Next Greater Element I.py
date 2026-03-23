class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = []
        for i in nums1:
            idx = nums2.index(i)
            f = 0
            for j in range(idx+1, n):
                if nums2[j] > i:
                    f = 1
                    res.append(nums2[j])
                    break
            if not f:
                res.append(-1)
        return res
