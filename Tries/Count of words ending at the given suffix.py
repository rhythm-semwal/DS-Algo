class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False
        self.count = dict()


class Solution:
    def __init__(self):
        self.root = self.get_root_node()

    def get_root_node(self):
        return TrieNode()

    def insert(self, word):
        current = self.root
        for i in range(len(word)-1, -1, -1):
            ch = word[i]
            if ch not in current.children:
                new_node = TrieNode()
                current.children[ch] = new_node
                current.count[ch] = 1
            else:
                current.count[ch] += 1

            current = current.children[ch]

        current.isEndOfWord = True

    def solve(self, words, suffix):
        root = self.root

        for each in words:
            self.insert(each)

        current = root

        word_count = 0

        for i in range(len(suffix)-1,-1,-1):
            ch = suffix[i]
            if ch not in current.children:
                return word_count
            else:
                word_count = current.count[ch]

            current = current.children[ch]

        return word_count


words = ["GeeksForGeeks", "geeks", "computer",
         "science", "array"]
suffix = "ks"

print(Solution().solve(words, suffix))
