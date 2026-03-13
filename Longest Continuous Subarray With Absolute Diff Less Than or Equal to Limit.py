class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_d = deque()
        min_d = deque()
        ans = 0

        for i in range(len(nums)):

            while max_d and nums[i] > max_d[-1]:
                max_d.pop()
            max_d.append(nums[i])

            while min_d and nums[i] < min_d[-1]:
                min_d.pop()
            min_d.append(nums[i])

            while max_d[0] - min_d[0] > limit:
                if nums[left] == max_d[0]:
                    max_d.popleft()
                if nums[left] == min_d[0]:
                    min_d.popleft()
                left += 1

            ans = max(ans, i - left + 1)

        return ans
