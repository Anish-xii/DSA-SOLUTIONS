class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        count_1 = [0] * 26
        count_2 = [0] * 26

        # if s1 is bigger -> no pr=ermutation
        if n1 > n2: return False

        # count the s1 and make the s2 window
        for i in range(n1):
            count_1[ord(s1[i]) - ord('a')] += 1
            count_2[ord(s2[i]) - ord('a')] += 1
        
        if count_1 == count_2: return True

        # SLIDE THE WINDOW & compare
        for i in range(n1, n2):
            
            count_2[ord(s2[i]) - ord('a')] += 1  # add to the r
            count_2[ord(s2[i-n1]) - ord('a')] -= 1  # cut from the l

            if count_1 == count_2: return True

        return False