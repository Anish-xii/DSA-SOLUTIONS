# For every char that match: we go to next char of both str and solve the sub str from there
# For every char that dont mach, ither:
#   1. exclude that char of str-1 and scan rest of str-2
#   2. exclude taht char of str-2 and scan rest of str-1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # rows -> text1, cols -> text2

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # whwn char mach
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                # when donnt mach
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) # bottom/right
        
        return dp[0][0]