# "Patience-sort":  (for every new card,placing each card either on top of an 
# existing pile (if it's smaller than the pile's current top card) 
# or starting a new pile (if it's larger than every pile's top card))

# Optimised: nlogn (binary-s)

# 1. insted of saving the whole dec, save only the top card
# 2. from priority left-right "find/search" the val >= num and replace it

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        piles = []

        for n in nums:
            l, r = 0, len(piles)

            while l < r:
                mid = (l+r)//2
                if piles[mid] < n:
                    l = mid + 1
                else:
                    r = mid
            
            # if we exided piles (which has indx len(piles)-1)
            # start a new pile
            if l == len(piles):
                piles.append(n)
            else:
                piles[l] = n
                
        
        return len(piles)

        