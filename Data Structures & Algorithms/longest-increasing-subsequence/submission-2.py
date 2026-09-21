# "Patience-sort":  (for every new card,placing each card either on top of an 
# existing pile (if it's smaller than the pile's current top card) 
# or starting a new pile (if it's larger than every pile's top card))

# Non-optimised: o(n2)

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        piles = []

        for n in nums:

            n_placed = False
            for p in piles:
                if p[-1] >= n:
                    p.append(n)
                    n_placed = True
                    break
            if not n_placed:
                piles.append([n])
        
        return len(piles)

        