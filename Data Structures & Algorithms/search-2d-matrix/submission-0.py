# O(M + log N)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        index = -1

        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                index = i

        if index == -1: return False

        l, r = 0, len(matrix[0])-1

        while l <= r:
            m = l + ((r-l)//2)      
            if matrix[index][m] > target:
                r = m - 1
            elif matrix[index][m] < target:
                l = m + 1
            else:
                return True

        return False 