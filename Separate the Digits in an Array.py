class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer= []
        for num in nums:
            for digits in str(num):
                answer.append(int(digits))

        return answer
