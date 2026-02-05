class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        newList = []
        for i in count:
            if count[i] == 2:
                newList.append(i)
        
        return newList
