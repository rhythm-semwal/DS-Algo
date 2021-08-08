class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        row, col = len(board), len(board[0])

        for r in range(row):
            for c in range(col):
                if self.search_word(board, word, 0, r, c):
                    return True

        return False

    def search_word(self, board, word, i, r, c):

        # base case
        if i >= len(word):
            return True

        # base case
        if c < 0 or c >= len(board[0]) or r < 0 or r >= len(board):
            return False

        if board[r][c] != word[i]:
            return False

        board[r][c] = '*'

        if (self.search_word(board, word, i + 1, r - 1, c) or
                self.search_word(board, word, i + 1, r, c - 1) or
                self.search_word(board, word, i + 1, r, c + 1) or
                self.search_word(board, word, i + 1, r + 1, c)):
            return True

        board[r][c] = word[i]
        return False