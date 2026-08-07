class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                indx = ord(c) - ord('a')
                key[indx] += 1
            
            key = tuple(key)
            if key not in seen:
                seen[key] = []
            
            seen[key].append(s)
        
        return list(seen.values())