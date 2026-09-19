class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1  # 2nd-last, last (always 1)

        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        
        return one