class Solution:
    def cellsInRange(self, s: str):
        result = []
        row, column = s.split(':')
        row_variable, row_number = row[0], int(row[1])
        column_variable, column_number = column[0], int(column[1])

        for name in range(ord(row_variable), ord(column_variable)+1):
            for num in range(row_number, column_number+1):
                result.append(chr(name)+str(num))

        return result


s = "A1:L2"
print(Solution().cellsInRange(s))
