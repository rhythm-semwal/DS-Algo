class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False
        self.count = dict()

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def __init__(self):
        self.root = self.get_root_node()

    def get_root_node(self):
        return TrieNode()

    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
                current.count[ch] = 1
            else:
                current.count[ch] += 1

            current = current.children[ch]

        current.isEndOfWord = True

    def search(self, word, node, index, count):
        if count > 1:
            return False
        if index == len(word):
            return True

        if word[index] not in node.children:
            count += 1
            self.search(word, node.children[word[index+1]], index+1, count)
        else:
            self.search(word, node.children[word[index]], index + 1, count)

    def solve(self, A, B):
        for each in A:
            self.insert(each)

        for word in B:
            current = self.root
            if self.search(word, current, 0, 0):
                print("here")


A = ["hello", "world"]
B = ["hella", "pello", "pella"]
Solution().solve(A, B)





