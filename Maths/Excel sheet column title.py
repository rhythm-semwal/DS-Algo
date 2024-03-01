class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ''
        """
        Here we are doing -1 because it's ) indexed
        Detailed Explanation: 
        https://leetcode.com/problems/excel-sheet-column-title/editorial/?envType=daily-question&envId=2024-01-17
        """

        while columnNumber > 0:
            answer = chr(ord('A') + (columnNumber - 1) % 26) + answer
            columnNumber = (columnNumber - 1) // 26

        return answer


columnNumber = 28
print(Solution().convertToTitle(columnNumber))
