class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        max_char_count = 0
        seen = defaultdict(int)

        l = 0
        for r in range(len(s)):
            char = s[r]
            
            seen[char] += 1
            max_char_count = max(max_char_count, seen[char])

            while (r-l+1) - max_char_count > k:
                seen[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res