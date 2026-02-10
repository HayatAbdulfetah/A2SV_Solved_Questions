class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            
            if s[i] in "{[(":
                res.append(s[i])
            elif res and (s[i] == ")" and res[-1] == "(" 
            or s[i] == "}" and res[-1] == "{" 
            or s[i] == "]" and res[-1] == "["):
                res.pop()
            else:
                return  False
        return len(res) == 0
