class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countStr1 = Counter(ransomNote)
        countStr2 = Counter(magazine)

        for char in countStr1:
            if countStr1[char] > countStr2[char]:
                return False
        
        return True
