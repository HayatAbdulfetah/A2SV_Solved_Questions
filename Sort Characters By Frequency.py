class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        ans = sorted(count.items(), key = lambda x : x[1],reverse = True)

        return ''.join(key*values for key, values in ans)
