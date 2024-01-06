from typing import List


class Solution:
    """
    Notice that if a spell and potion pair is successful, then the spell and all stronger potions will be successful too.
    Thus, for each spell, we need to find the potion with the least strength that will form a successful pair.
    We can efficiently do this by sorting the potions based on strength and using binary search.
    """
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        TC = O(N * log(M)), where N is the length of the spells list, and M is the length of the potions list
        """
        result = []
        potions.sort()

        for i in spells:
            low, high = 0, len(potions) - 1
            index = len(potions)

            while low <= high:
                mid = (low + high) // 2

                if i * potions[mid] >= success:
                    high = mid - 1
                    index = mid
                else:
                    low = mid + 1
            result.append(len(potions) - index)

        return result