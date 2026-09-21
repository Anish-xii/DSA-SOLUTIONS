# Top-down

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {len(s): True}

        def dfs(i):
            if i in memo: 
                return memo[i]
            
            for w in wordDict:
                # if we found a valid pare [i:i+len(w)] recurse the rest of arr [i+len(w): ]
                if (i + len(w) <= len(s)) and (s[i:i+len(w)] == w):
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            # if we dont found a valid pare for all words for any given point
            memo[i] = False
            return False
        

        return dfs(0)

        