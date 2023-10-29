class TrieNode:
    def __init__(self):
        self.children = dict()
        self.count = dict()
        self.isEndOfWord = False


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def __init__(self):
        self.root = self.get_root_node()

    def get_root_node(self):
        return TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch in current.children:
                current.count[ch] += 1
            else:
                new_node = TrieNode()
                current.children[ch] = new_node
                current.count[ch] = 1

            current = current.children[ch]

        current.isEndOfWord = True

    def check(self, word, m):
        n = len(word)
        if n < m:
            return False
        if n == m:
            return True

        word1, word2 = "", ""

        for i in range(m):
            word1 += word[i]
        for i in range(n-m, n):
            word2 += word[i]

        return word1 == word2

    def solve(self, A, B):
        m = len(B[0])

        for each in A:
            if self.check(each, m):
                self.insert(each)

        result = []
        for query in B:
            current = self.root
            count = 0
            for ch in query:
                if ch not in current.children:
                    count = 0
                else:
                    count = current.count[ch]
                    current = current.children[ch]

            result.append(count)

        return result
