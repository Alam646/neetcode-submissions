class TrieNode:
    def __init__(self):
        self.letters = {}
        self.endofWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    

    def insert(self, word: str) -> None:
        temp = self.root


        for x in word:
            if x not in temp.letters:
                temp.letters[x] = TrieNode()
            
            temp = temp.letters[x]
        
        temp.endofWord = True



    def search(self, word: str) -> bool:
        temp = self.root
        
        for x in word:
            if x not in temp.letters:
                return False

            temp = temp.letters[x]
        
        return temp.endofWord
               

    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for x in prefix:
            if x not in temp.letters:
                return False
            
            temp = temp.letters[x]
        
        return True
        
        