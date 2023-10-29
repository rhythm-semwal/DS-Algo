from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}

    def insert(self, word):
        letters = self.children

        for ch in word:
            if ch not in letters:
                letters[ch] = {"freq": 1}
            else:
                letters[ch]["freq"] += 1

            letters = letters[ch]
        letters["*"] = True

    def generate_prefix(self, word):
        result = []
        letters = self.children

        for ch in word:
            result.append(ch)
            if letters[ch]["freq"] == 1:
                break
            else:
                letters = letters[ch]

        return "".join(result)


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        t = TrieNode()
        for each in A:
            t.insert(each)

        ans = []
        for each in A:
            ans.append(t.generate_prefix(each))

        print(ans)


A = ["zebra", "dog", "duck", "dove"]
Solution().prefix(A)
