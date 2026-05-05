class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False

        # 1. uniq key s1
        s1_count = defaultdict(int)
        for s in s1: s1_count[s] += 1

        # 2. uniq key window
        w_count = defaultdict(int)
        l = 0

        for r in range(len(s2)):
            w_count[s2[r]] += 1

            # 3. srink down window from left when its out of bounce
            if (r - l + 1) > len(s1):    
                w_count[s2[l]] -= 1
                if w_count[s2[l]] == 0:
                    del w_count[s2[l]]
                l += 1

            # 4. check the current unq keys, while in curr loop
            if (r - l + 1) == len(s1):
                if w_count == s1_count:
                    return True

        return False