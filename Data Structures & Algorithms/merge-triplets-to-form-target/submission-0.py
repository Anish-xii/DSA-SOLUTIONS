# for every n in targets, check those n in all the indivisual triplet []
# while skipping [] where any target 'i' position val is bigger

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        
        # use a  set to see all unic i'th pos is avalabel
        pos = set()

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            
            for i, n in enumerate(t):
                if n == target[i]:
                    pos.add(i)
        
        return len(pos) == 3