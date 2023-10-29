class TrieNode:
    def __init__(self):
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    # Trie data structure class
    def __init__(self):
        self.root =TrieNode()


def insert(root, key):
    '''
    root: root of trie tree
    key:  key to be inserted
    '''
    # code here
    node = root

    for ch in key:
        index = ord(ch) - ord('a')

        if node.children[index] is None:
            node.children[index] = TrieNode()

        node = node.children[index]

    node.isEndOfWord = True


def search(root, key):
    '''
    root:       root of trie tree
    key:        key to be searched
    Returns:    true if key presents in trie, else false
    '''
    # code here
    node = root

    for ch in key:
        index = ord(ch) - ord('a')
        if node.children[index] is None:
            return False
        node = node.children[index]

    if node.isEndOfWord:
        return True
    return False
