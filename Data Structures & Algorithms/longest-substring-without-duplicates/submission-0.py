class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1

        max_l = 0
        l = 0
        seen_set = set()

        for r in range(n):
            
            # if r alredy exist in set, find and remove
            while s[r] in seen_set:
                seen_set.remove(s[l])
                l += 1

            max_l = max(max_l, r-l+1)    
            seen_set.add(s[r])

        return max_l 