class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = []
        count = Counter(nums)
        for num in count:
            if count[num] > len(nums) //3:
                answer.append(num)       
        return answer
