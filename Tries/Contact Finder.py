class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False
        self.count = dict()

class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def __init__(self):
        self.root = self.get_root_node()

    def get_root_node(self):
        return TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                new_node = TrieNode()
                current.children[ch] = new_node
                current.count[ch] = 1
            else:
                current.count[ch] += 1

            current = current.children[ch]

        current.isEndOfWord = True

    def search(self, word):
        current = self.root
        count = 0
        for ch in word:
            if ch not in current.children:
                return 0
            else:
                count = current.count[ch]

            current = current.children[ch]

        return count

    def solve(self, A, B):
        result = []
        for i in range(len(B)):
            if A[i] == 0:
                self.insert(B[i])
            else:
                result.append(self.search(B[i]))

        print(result)


# A = [0, 0, 1, 1]
# B = ["hack", "hacker", "hac", "hak"]

A = [0, 1]
B = ["abcde", "abc"]
Solution().solve(A, B)
