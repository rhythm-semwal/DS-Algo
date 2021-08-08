from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.count = 0


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def construct_trie(self, words):
        root = self.root
        for chars in words:
            index = self.get_index(chars)

            if index not in root.children:
                root.children[index] = self.get_node()
                root.count = 1
            else:
                root.count += 1

            root = root.children[index]

        return root

    def solve(self, words):
        root = self.root
        for chars in words:
            index = self.get_index(chars)

    def prefix(self, A):
        for word in A:
            trie = self.construct_trie(word)

        # result = []
        #
        # node = trie.children
        # for words in A:
        #     ans = ""
        #     for chars in words:
        #         if node[chars] == 1:
        #             ans += chars
        #             break
        #         else:
        #             node = node[chars]
        #         ans += chars
        #
        #     result.append(ans)
        #
        # print(result)


A = ["zebra", "dog", "duck", "dove"]
Solution().prefix(A)
