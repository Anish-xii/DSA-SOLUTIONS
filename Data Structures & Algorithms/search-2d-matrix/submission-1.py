# logM + LogN
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        index = float('inf')
        s, e = 0, len(matrix) - 1

        # logM
        while s <= e:
            row = (s+e)//2
            if matrix[row][0] > target: e = row -1
            elif matrix[row][-1] < target: s = row + 1
            else:
                index = row
                break        
        

        if index == float('inf'): return False

        l, r = 0, len(matrix[0])-1

        # logN
        while l <= r:
            m = l + ((r-l)//2)      
            if matrix[index][m] > target:
                r = m - 1
            elif matrix[index][m] < target:
                l = m + 1
            else:
                return True

        return False 