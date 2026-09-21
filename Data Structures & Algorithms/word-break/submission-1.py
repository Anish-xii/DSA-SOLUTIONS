# Bottom-up

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and (s[i:i+len(w)] == w):
                    if dp[i+len(w)]:
                        dp[i] = True
                        break  # from maching more w for 'i'
        
        return dp[0]

