class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq_map = {}
        max_len = 0

        for n in nums:
            if n not in seq_map:

                # check 1 step back and 1 step ahed of n, default 0 return
                left_len = seq_map.get(n-1, 0) 
                right_len = seq_map.get(n+1, 0)

                cur_len = left_len + 1 + right_len
                max_len = max(max_len, cur_len)

                seq_map[n] = cur_len
                seq_map[n - left_len] = cur_len
                seq_map[n + right_len] = cur_len

        return max_len