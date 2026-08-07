class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_count, t_count = [0]*26, [0]*26

        for i in range(len(s)):
            s_order = ord(s[i]) - ord('a')
            t_order = ord(t[i]) - ord('a')
            s_count[s_order] += 1
            t_count[t_order] += 1
        
        return s_count == t_count