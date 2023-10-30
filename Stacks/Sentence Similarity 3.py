class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2, sentence1

        stack1 = sentence1.split(" ")
        stack2 = sentence2.split(" ")

        while stack1[0] == stack2[0]:
            stack1.pop(0)
            stack2.pop(0)

            if not stack2:
                return True

        if not stack2:
            return True

        while stack1[-1] == stack2[-1]:
            stack1.pop()
            stack2.pop()

            if not stack2:
                return True

        if not stack2:
            return True

        return False


sentence1 = "My name is Haley"
sentence2 = "My Haley"

# sentence1 = "of"
# sentence2 = "A lot of words"

sentence1 = "Eating right now"
sentence2 = "Eating"

sentence1 = "CwFfRo regR"
sentence2 = "CwFfRo H regR"
print(Solution().areSentencesSimilar(sentence1, sentence2))
