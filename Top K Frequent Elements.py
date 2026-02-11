class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        sorted_count = sorted(count.items(), key= lambda x:x[1],reverse = True)
        for i in range(k):
            res.append(sorted_count[i][0])
        #x = [sorted_count[i][0] for i in range(k)]

        return res
