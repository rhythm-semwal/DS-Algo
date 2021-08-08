from random import randint


class Snake:
    def __init__(self, start_point=None, end_point=None):
        self.start_point = start_point
        self.end_point = end_point

    def get_start_point(self):
        return self.start_point

    def get_end_point(self):
        return self.end_point

    def set_start_point(self, start_point):
        self.start_point = start_point

    def set_end_point(self, end_point):
        self.end_point = end_point

    class Ladder:
        def __init__(self, start_point=None, end_point=None):
            self.start_point = start_point
            self.end_point = end_point

        # Getters , Setters
        def get_start_point(self):
            return self.start_point

        def get_end_point(self):
            return self.end_point

        def set_start_point(self, start_point):
            self.start_point = start_point

        def set_end_point(self, end_point):
            self.end_point = end_point


class Dice:
    def __init__(self):
        self.__value = None

    def roll(self):
        self.__value = randint(1, 6)
        return self.__value


class Player:
    def __init__(self, name=None, position=None):
        self.name = name
        self.position = position
        self.is_winner = False

    # Getters , Setters
    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def set_name(self, name):
        self.name = name

    def set_position(self, position):
         self.position = position

    def move(self, dice_value, encounter=False):
        if not encounter:
            new_position = self.position + dice_value

        else:
            new_position = dice_value

        if new_position > 100:
            return

        elif new_position == 100:
            self.is_winner = True

        self.position = new_position


class Board:
    def __init__(self, size):
        self.board = [None for _ in range(size)]

    def populate_board(self, snakes, ladders):

        for snake in snakes:
            start_point = snake.get_start_point()
            self.board[start_point] = snake

        for ladder in ladders:
            start_point = ladder.get_start_point()
            self.board[start_point] = ladder

        return self.board


class Game:
    def __init__(self):
        self.winner = None
        self.board_size = 100

    def play(self):
        snakes = []
        ladders = []

        players = [Player("A", 1), Player("B", 2)]
        turns = 0

        board = Board(self.board_size).populate_board(snakes, ladders)
        dice = Dice()

        while self.winner is None:
            turns += 1

            for player in players:
                dice_value = dice.roll()
                player.move(dice_value)
                encounter = board[player.position]
                if encounter:
                    end_point = encounter.end_point
                    player.move(end_point, encounter=True)

                if player.is_winner:
                    self.winner = player
                    break

        print("\n--------------GAME OVER--------------")
        print(f"Player {self.winner.name} Has won the game after {turns} turns")
        print("--------------GAME OVER--------------\n")


if __name__ == "__main__":
    game = Game()
    game.play()
