# logM + LogN
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        l, r = 0, (row * col) -1 # position in flat array

        while l <= r:
            mid = (l+r)//2
            i, j = (mid // col), (mid % col) # mid pos in 2d array
            mid_num = matrix[i][j]
            
            if mid_num == target:
                return True
            elif mid_num < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False