class WordDictionary:

    def __init__(self):
        self.trie = {}


    # nested {k:{k:v}}
    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'


    def search(self, word: str) -> bool:
        def dfs(d, i):
            if i == len(word):
                return '.' in d
            
            c = word[i]
        
            if c != '.':
                if c in d:
                    return dfs(d[c], i+1)
                return False
            else:
                for key in d:
                    if key != '.' and dfs(d[key], i+1):
                        return True
                return False
        
        return dfs(self.trie, 0)