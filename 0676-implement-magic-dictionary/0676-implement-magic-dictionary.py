class MagicDictionary:

    def __init__(self):
        self.dict = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict.add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            for j in range(26):
                target = searchWord[:i] + chr(ord('a') + j) + searchWord[i + 1:]
                if target == searchWord:
                    continue
                
                if target in self.dict:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)