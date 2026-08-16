class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_sub = 0
        count = [0] * 26 # 26 capital char
        l = 0

        for r in range(len(s)):
            
            char = s[r]
            count[ord(char) - ord('A')] += 1

            # sub_len - most repeating char = chars to convert
            # if > what we are allowed, move l
            while (r-l+1) - max(count) > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            sub_len = r-l+1
            max_sub = max(max_sub, sub_len)
        
        return max_sub