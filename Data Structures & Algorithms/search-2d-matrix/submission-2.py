# logM + LogN
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find - row (logM) ---

        indx = -1
        l, r = 0, len(matrix)-1

        while l <= r:
            row = (l+r)//2
            if target > matrix[row][-1]:
                l = row + 1
            elif target < matrix[row][0]:
                r = row -1
            else:
                indx = row
                break
        
        if indx == -1: return False


        # find num (logN) --

        l, r = 0, len(matrix[0]) -1

        while l <= r:
            mid = (l+r)//2
            if target > matrix[indx][mid]:
                l = mid + 1
            elif target < matrix[indx][mid]:
                r = mid - 1
            else:
                return True
    
        return False