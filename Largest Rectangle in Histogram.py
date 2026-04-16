class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                
                max_area = max(max_area, h * w)
            
            stack.append(i)
        
        n = len(heights)
        while stack:
            h = heights[stack.pop()]
            
            if stack:
                w = n - stack[-1] - 1
            else:
                w = n
            
            max_area = max(max_area, h * w)
        
        return max_area
