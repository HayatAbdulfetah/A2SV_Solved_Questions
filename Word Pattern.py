class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        hash_map = {}
        unique = set()

        if len(pattern) != len(s):
            return False

        for i in range(len(s)):
            if pattern[i] not in hash_map:
                if s[i] in unique:
                    return False
                hash_map[pattern[i]] = s[i]
                unique.add(s[i])
            else:
                if hash_map[pattern[i]] != s[i]:
                    return False
        return True
