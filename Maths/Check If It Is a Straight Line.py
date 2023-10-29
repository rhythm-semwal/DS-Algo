'''
Qs. https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        The slope for a line through any 2 points (x0, y0) and (x1, y1) is (y1 - y0) / (x1 - x0); Therefore, for any given 3 points (denote the 3rd point as (x, y)), if they are in a straight line, the slopes of the lines from the 3rd point to the 2nd point and the 2nd point to the 1st point must be equal:

        (y - y1) / (x - x1) = (y1 - y0) / (x1 - x0)
        In order to avoid being divided by 0, use multiplication form:

        (x1 - x0) * (y - y1) = (x - x1) * (y1 - y0) =>
        dx * (y - y1) = dy * (x - x1), where dx = x1 - x0 and dy = y1 - y0
        """
        i, j = 0, 1

        while j < len(coordinates):
            xp1 = coordinates[i][0]
            yp1 = coordinates[i][1]
            xp2 = coordinates[j][0]
            yp2 = coordinates[j][1]

            if xp1 != xp2-1:
                return False
            if yp1 != yp2-1:
                return False

            i += 1
            j += 1
        return True
