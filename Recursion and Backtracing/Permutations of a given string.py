class Solution:

    def permutations(self, word, left, right, result):
        if left == right:
            print("".join(word))

        for i in range(left, right+1):
            word[i], word[left] = word[left], word[i]
            self.permutations(word, left+1, right, result)
            word[i], word[left] = word[left], word[i]


if __name__ == "__main__":
    a = 'abc'
    left = 0
    right = len(a)-1
    result = []
    Solution().permutations(list(a), 0, right, result)
