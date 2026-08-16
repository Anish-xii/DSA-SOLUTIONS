class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t or len(s) < len(t): return ''

        cnt = Counter(t)
        windo = {}

        have, need = 0, len(cnt)
        res, res_len = [-1,-1], float('inf')

        l = 0
        
        for r in range(len(s)):
            c = s[r]
            windo[c] = windo.get(c, 0) + 1
            
            if c in cnt and windo[c] == cnt[c]:
                have += 1
            
            while have == need:
                c_len = r-l+1
                
                if c_len < res_len:
                    res = [l, r]
                    res_len = c_len
                
                windo[s[l]] -= 1
                if s[l] in cnt and windo[s[l]] < cnt[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""

# how many chars wee need vs what we have. going through the arr count char freq if a char is in t and we have the needed freq for that char we +1 have.
# when we have all the have, we srink from left and update windo, if what we removed is a candidate and we now lack needed freq for a char -= have.
