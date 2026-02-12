class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newStr = [''] *len(s)
      
        for i in range(len(s)):
            newStr[indices[i]] = s[i]
          
        return ''.join(newStr)
