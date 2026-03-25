class Solution:
    def lastRemaining(self, n: int) -> int:
        current  =  1
        step = 1

        remaining = n
        left_to_right = True

        while remaining > 1:

            if left_to_right or remaining % 2 == 1:

                current+=step

            step*=2
            remaining//=2

            left_to_right = not left_to_right
        
        return current
