class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows = len(mat)
        cols = len(mat[0])

        for i in range(4):
            for r in range(rows):
                for c in range(r+1, cols):
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
            
            for i in mat:
                i.reverse()
            if mat == target:
                return True
            
        return False
