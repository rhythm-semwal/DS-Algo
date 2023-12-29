# https://www.geeksforgeeks.org/problems/buildings-receiving-sunlight3032/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
class Solution1:
    def getBuildingsWithAView(self, buildings):
        # TC = O(N)
        # SC = O(N)

        result = [0]
        stack = [buildings[0]]

        for i in range(1, len(buildings)):
            if buildings[i] < stack[-1]:
                stack.append(buildings[i])
            else:
                while stack and buildings[i] >= stack[-1]:
                    stack.pop()

                if not stack:
                    result.append(i)
                    stack.append(buildings[i])
        return result


class Solution2:
    def getBuildingsWithAView(self, buildings):
        i, count = 1, 1
        current_building = buildings[0]

        while i < len(buildings):
            if current_building <= buildings[i]:
                count += 1
                current_building = buildings[i]
            i += 1

        return count


input = [7, 4, 9, 8, 8, 2, 9]
input = [6, 2, 8, 4, 11, 13]
input = [4, 7, 6, 5, 5, 7, 1, 8, 6]
# input = [11, 12, 13, 14, 15]
print(Solution2().getBuildingsWithAView(input))

