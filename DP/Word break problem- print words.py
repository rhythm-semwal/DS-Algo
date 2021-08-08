class Solution:
    def break_string(self, s, word):
        i = 0

        while i < len(s):
            j = 0

            while j < len(word):
                if word[j] == s[i]:
                    if j == len(word)-1:
                        print(word, end=" ")
                        break
                    else:
                        i += 1
                        j += 1

                else:
                    if i == len(s)-1:
                        break
                    else:
                        j = 0
                        i += 1

            break

    def word_break(self, A, B):
        for word in B:
            self.break_string(str(A), word)

A = "myinterviewtrainer",
B = ["trainer", "my", "interview"]
Solution().word_break(A, B)