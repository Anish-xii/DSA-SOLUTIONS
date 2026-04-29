class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq_map = defaultdict(int)
        max_len = 0

        for n in nums:
            if not seq_map[n]:

                seq_map[n] = seq_map[n-1] + 1 + seq_map[n+1] 
                seq_map[n - seq_map[n-1]] = seq_map[n]
                seq_map[n + seq_map[n+1]] = seq_map[n]
                max_len = max(max_len, seq_map[n])

        return max_len