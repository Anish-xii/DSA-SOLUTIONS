class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t: return ""

        t_count = Counter(t)

        # only get the indexes and chars we need in same order of 's'
        filtered_s = [(i, char) for i, char in enumerate(s) if char in t_count]

        have, need = 0, len(t_count)

        window = defaultdict(int)
        res, res_l = [-1, -1], float("inf") # substr (start, fin)

        l = 0

        for r in range(len(filtered_s)):
            
            c = filtered_s[r][1] # (i, c)
            window[c] += 1
            
            # if we have the same amount of a char we need
            if t_count[c] == window[c]: have += 1

            # if we have all char we need
            while need == have:

                start_i = filtered_s[l][0]
                end_i = filtered_s[r][0]

                w_len = end_i - start_i + 1
                
                # save new res
                if w_len < res_l:
                    res = [start_i, end_i]
                    res_l = w_len
                
                # prepare for next stage
                # (contract l window (clear c data (find c)))
                left_c = filtered_s[l][1]
                window[left_c] -= 1  
                l += 1 

                # check if we broke the valid window
                if window[left_c] < t_count[left_c]:
                    have -= 1


        res_l, res_r = res            
        return s[res_l:res_r+1] if res_l != float("inf") else ""
