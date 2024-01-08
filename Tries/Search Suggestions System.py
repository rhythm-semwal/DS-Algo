from typing import List


class Solution1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = {}

        for p in products:
            t = trie
            for index, ch in enumerate(p):
                is_end = index == len(p)-1
                if ch not in t:
                    t[ch] = {
                        'trie': {},
                        'is_end': is_end,
                        'data': [p]
                    }
                else:
                    t[ch]['data'].append(p)

                if is_end:
                    t[ch]['is_end'] = is_end

                t = t[ch]['trie']

        result = [[] for _ in range(len(searchWord))]

        for index, ch in enumerate(searchWord):
            if ch in trie:
                result[index] = trie[ch]['data'][:3]
                trie = trie[ch]['trie']
            else:
                break

        return result


class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        result = []

        for index, ch in enumerate(searchWord):
            count = 0
            current = []
            search_key = searchWord[:index + 1]

            for p in products:
                if search_key == p[:index + 1]:
                    count += 1
                    current.append(p)

                if count == 3:
                    break

            result.append(current)

        return result


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


class Solution3:
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


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        temp_list = [[] for _ in range(len(searchWord))]

        for word in products:
            for index, value in enumerate(searchWord):
                # len(word) > index this conditions is there to check for string index out of range error
                if len(word) > index and word[index] == value:
                    temp_list[index].append(word)
                else:
                    break

        result = []
        for each in temp_list:
            result.append(each[:3])

        return result


if __name__ == '__main__':
    # products = ["havana"]
    # searchWord = "tatiana"
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(Solution().suggestedProducts(products, searchWord))
