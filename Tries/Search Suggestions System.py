from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.word = []


class TrieNode:
    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        temp = self.root
        for ch in word:
            temp.word.append(word)
            temp = temp.children.setdefault(ch, Trie())
        temp.word.append(word)

    def search(self, word):
        temp = self.root

        for ch in word:
            if ch in temp.children:
                temp = temp.children[ch]
            else:
                return []
        return temp.word


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        node = TrieNode()

        for word in products:
            node.insert(word)

        result = []

        for idx, value in enumerate(searchWord):
            l = node.search(searchWord[:idx + 1])
            if len(l) > 3:
                result.append(l[:3])
            else:
                result.append(l)

        return result


if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mousep"
    print(Solution().suggestedProducts(products, searchWord))


# ["mobile","moneypot","monitor","mouse","mousepad"]