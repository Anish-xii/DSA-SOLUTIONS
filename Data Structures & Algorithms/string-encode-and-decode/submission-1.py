class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # word_len + sign + word
            res += str(len(s)) + "$" + s 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # begining of str

        while i < len(s): # staying inside str
            
            j = i
            # find the start of word: sign
            while s[j] != "$": 
                j += 1
            
            word_len = int(s[i:j])
            i = j + 1   # start of word
            j = i + word_len # end of word + 1

            res.append(s[i:j]) # i-inclusive j-exclusive
            i = j # reset
        
        return res    