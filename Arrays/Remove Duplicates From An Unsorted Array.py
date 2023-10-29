# https://afteracademy.com/blog/remove-duplicates-from-an-unsorted-array/
class Solution:
    def removeDuplicates(self, arr) -> int:
        hash_set = set(arr)

        return list(hash_set)
