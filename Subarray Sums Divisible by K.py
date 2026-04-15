class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_prefixes = [0]*k
        mod_prefixes[0] = 1
        curr_sum = 0
        total = 0

        for num in nums:
            curr_sum+=num
            target_mod = curr_sum%k
            if target_mod<k:
                total+=mod_prefixes[target_mod]
            mod_prefixes[curr_sum%k]+=1

        return total
