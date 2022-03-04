# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


def recursiveSearch(root, word, index):
    if index >= len(word):
        return root.endOfWord
    c = word[index]
    index += 1
    if c == '.':
        for node in root.children.values():
            if recursiveSearch(node, word, index):
                return True
        return False
    elif c not in root.children:
        return False
    else:
        return recursiveSearch(root.children[c], word, index)


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        return recursiveSearch(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
