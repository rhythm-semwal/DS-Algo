class Solution:
    """
    To solve this problem, we need to understand that the operations allowed don't change the frequency of characters,
    only their positions or representations. Therefore, two "close" strings must have the same set of characters and
    the same frequency of each character, although the characters themselves can be different.

    The crucial realization is that
    operation 1 allows us to reorder characters in any fashion, making the relative order of characters inconsequential.
    Operation 2 allows us to transform characters into each other, given that both characters exist in both strings.

    Condition 1
    The consequence of this is Both word1 and word2 must contain the same unique characters -
    they must have the same set of keys in their character counts (Counter).

    Condition 2
    Both word1 and word2 must have the same character frequencies, which implies,
    after sorting their frequency counts, these should match.
    If both the sorted values of the counts and the sets of unique characters match,
    we return true. Otherwise, we return false.
    """
    def closeStrings(self, word1: str, word2: str) -> bool:

        freq1, freq2 = [0] * 26, [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        # Both word1 and word2 must contain the same unique characters -
        # they must have the same set of keys in their character counts (Counter).
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True
