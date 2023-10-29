class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []
        diff1 = set(nums1) - set(nums2)
        result.append(diff1)
        diff2 = set(nums2) - set(nums1)
        result.append(diff2)
        return result
      
    def findDifference1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]

        hash_map1 = set(nums1)

        hash_map2 = set(nums2)

        for i in hash_map2:
            if i not in hash_map1:
                result[1].append(i)
        for i in hash_map1:
            if i not in hash_map2:
                result[0].append(i)

        return result
