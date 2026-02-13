class Solution:
    def findValidPair(self, s: str) -> str:

        if len(s) <= 2:
            return ""

        l = 0
        r = 1
        count = Counter(s)

        while r < len(s):
            if s[l] != s[r] and count[s[l]] == int(s[l]) and count[s[r]] == int(s[r]):
                return s[l]+s[r]

            l += 1
            r += 1

        return ""
