class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        seen = set()

        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1 
            seen.add(s[r])
            max_sub = max(max_sub, r-l+1)

        return max_sub

