class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        for i in image:
            i.reverse()
        
        for r in range(rows):
            for c in range(cols):
                if image[r][c] == 0:
                    image[r][c] = 1
                else:
                    image[r][c] = 0

        return image
