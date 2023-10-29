class TrieNode:
    def __init__(self):
        self.children = dict()
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
            if ch not in current.children:
                new_node = TrieNode()
                current.children[ch] = new_node
            current = current.children[ch]
        current.isEndOfWord = True

    def check(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return 0
            current = current.children[ch]
        if current.isEndOfWord:
            return 1
        return 0

    def solve(self, A, B):
        for each in A:
            self.insert(each)
        result = []
        for word in B:
            result.append(self.check(word))

        print(result)


# A = [ "hat", "cat", "rat" ]
# B = [ "cat", "ball" ]
# A = [ "tape", "bcci" ]
# B = [ "table", "cci" ]
A = [ "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg" ]
B = [ "a", "b", "ab", "abcd" ]
Solution().solve(A, B)
