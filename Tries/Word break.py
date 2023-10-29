class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False


class Solution:
    def __init__(self):
        self.root = self.get_root_node()

    def get_root_node(self):
        return TrieNode()

    def insert(self, word):
        current = self.root

        for each in word:
            if each in current.children:
                continue
            else:
                new_node = TrieNode()
                current.children[each] = new_node
                # current.children[each] = 1

            current = current.children[each]

        current.isEndOfWord = True

    def search(self, word):
        current = self.root

        for each in word:
            if each not in current.children:
                return False

            current = current.children[each]

        if current.isEndOfWord:
            return True
        return False

    def word_break(self, word):
        if len(word) == 0:
            return True

        for i in range(1, len(word)+1):
            if self.search(word[:i]) and self.word_break(word[i:]):
                return True
        return False


    def solve(self, A, B):
        for each in B:
            self.insert(each)

        print(1 if self.word_break(A) else 0)


A = "iamace"
B = ["i", "am", "ace"]
Solution().solve(A, B)

