# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
class Solution1:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
        
        return letters[0]

# use binary search
class Solution2:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
      if target >= letters[-1] or target < letters[0]:
          return letters[0]

      low, high = 0, len(letters)-1

      while low < high:
          mid = (low+high)//2

          if letters[mid] > target:
              high = mid
          else:
              low = mid+1

      return letters[low]
