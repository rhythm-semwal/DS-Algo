# http://www.newthinktank.com/2012/12/object-oriented-design-2/

from random import randint


class Coin:
    def __init__(self):
        self.__coin_option = ""
        self.coin_value = {0:"Heads", 1:"tails"}

    def get_coin_value(self):
        self.__coin_option = self.coin_value[randint(0, 1)]

    def get_coin_option(self):
        return self.__coin_option


class Player:
    def __init__(self, name):
        self.__name = name
        self.__coin_option = ""
        self.coin_value = {0: "Heads", 1: "tails"}

    def set_coin_option(self, opponent_coin):
        self.__coin_option = "tails" if opponent_coin == "Heads" else "Heads"

    def get_coin_option(self):
        return self.__coin_option

    def get_random_coin_option(self):
        random_num = randint(0, 1)
        self.__coin_option = self.coin_value[random_num]
        return self.coin_value[random_num]

    def did_player_win(self, coin_side):
        if self.__coin_option == coin_side:
            print("player won")
        else:
            print("player lost")


class Game:
    def __init__(self, player1, player2):
        self.players_list = []
        self.players_list.append(Player(player1))
        self.players_list.append(Player(player2))
        self.coin = Coin()

    def start_game(self):
        random_index = randint(0, 1)
        players_picked = self.players_list[random_index].get_random_coin_option()
        opponent = 0 if random_index == 1 else 1
        self.players_list[opponent].set_coin_option(players_picked)

        self.coin.get_coin_value()
        winning_flip = self.coin.get_coin_option()

        self.players_list[0].did_player_win(winning_flip)
        self.players_list[1].did_player_win(winning_flip)


if __name__ == "__main__":
    game = Game("Rhythm", "Semwal")
    game.start_game()