import re

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = [[] for i in range(0, 501)]

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        length = len(word)
        self.l[length].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        length = len(word)
        for x in self.l[length]:
            if(re.fullmatch(word, x)):
                return True
            else:
                continue
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)