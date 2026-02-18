class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sum_even = sum([i for i in nums if i %2 == 0])

        for val,index in queries:
            if not nums[index] % 2:
                sum_even -= nums[index]

            nums[index] += val

            if not nums[index] %2:
                sum_even += nums[index]

            answer.append(sum_even)
            
        return answer
