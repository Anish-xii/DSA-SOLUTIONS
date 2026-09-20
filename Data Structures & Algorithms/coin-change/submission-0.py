# Top-down

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        memo = {}

        # how many ways u can make the "v" from v-0 and memo
        def dfs(v):
            if v == 0: return 0
            if v in memo: return memo[v]

            res = float('inf')
            for c in coins:
                if (v - c) >= 0:
                    res = min(res, 1+dfs(v-c))

            memo[v] = res
            return res
        

        min_coin = dfs(amount)
        return -1 if min_coin >= float('inf') else min_coin