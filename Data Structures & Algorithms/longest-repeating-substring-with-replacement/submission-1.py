class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        seen = defaultdict(int)
        most_seen_c_frq = 0

        # 1. slide window add new chars
        l = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            # 2. new char just became most frq or its the same
            most_seen_c_frq = max(most_seen_c_frq, seen[s[r]])

            # 3. validate: w_len - most_seen_c should be <= k
            while (r - l + 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res    