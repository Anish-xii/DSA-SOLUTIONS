class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq_set = set(nums)
        max_len = 0

        for n in seq_set:
            if (n-1) not in seq_set:
                l = 1
                while (n + l) in seq_set:
                    l += 1
                
                max_len =  max(max_len, l)   

        return max_len