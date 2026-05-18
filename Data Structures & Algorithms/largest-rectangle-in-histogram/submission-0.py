class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0
        stk = []

        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][0] > h:
                height, index = stk.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                start = index
            stk.append((h, start))

        for h, i in stk:
            max_area = max(max_area, h * (len(heights)-i))

        return max_area