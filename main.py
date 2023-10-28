from collections import deque


class Node:
    def __init__(self, char: str, children=None, last_char=False):
        self.char = char
        self.children = children if children is not None else {}
        self.last_char = last_char

    def __str__(self):
        return f'Chars="{self.char}"'


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            curr = curr.children.setdefault(letter, Node(letter))
        curr.last_char = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.last_char

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return not curr.last_char


if __name__ == '__main__':
    # task = Solution()
    # print(task.ladderLength(beginWord, endWord, wordList))

    trie = Trie()
    trie.insert("a")
    print(trie.search("a"))
    print(trie.startsWith("a"))
