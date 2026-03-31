class Solution:
    def splitString(self, s: str) -> bool:
        # i = 0,  = s[::j+1]
        def back_track(idx, curr):
            if idx ==len(s):
                for i in range(1,len(curr)):
                    if curr[i-1] -curr[i] != 1:
                        return False

                return len(curr) >=2

            for j in range(idx, len(s)):
                val = int(s[idx:j+1])
                curr.append(val)
                if back_track(j+1,curr):
                    return True
                curr.pop()
            return False
        return back_track(0,[])

        # at first no combination will work till [0,5,0,0,4,3]then goes on to check [05,0043], [05,0,04] 
