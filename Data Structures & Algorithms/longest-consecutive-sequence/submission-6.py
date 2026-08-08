class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        max_seq = 0

        for n in seen:
            if n-1 not in seen:
                l_seq = 1
                while n + l_seq in seen:
                    l_seq += 1
                
                max_seq = max(max_seq, l_seq)
        
        return max_seq