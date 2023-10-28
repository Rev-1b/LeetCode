class Node:
    def __init__(self, children=None):
        self.children = children if children is not None else {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            curr = curr.children.setdefault(letter, Node())
        curr.is_word = True

    def search(self, word: str) -> bool:
        def do_magic(node: Node, index: int) -> bool:
            if index == len(word):
                return node.is_word
            if word[index] == '.':
                for child in node.children.values():
                    res = do_magic(child, index + 1)
                    if res:
                        return True
            if word[index] in node.children:
                return do_magic(node.children[word[index]], index + 1)
            return False

        return do_magic(self.root, 0)


if __name__ == '__main__':
    task = WordDictionary()
    task.addWord("bad")
    task.addWord("dad")
    task.addWord("mad")
    print(task.search("pad"))
    print(task.search("bad"))
    print(task.search(".ad"))
    print(task.search("b.."))
