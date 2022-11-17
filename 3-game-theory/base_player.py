from player import Player

class MyPlayer(Player):
    def __init__(self, name):
        print(name)
        super().__init__(name)

    def choose_next_move(self, board, letter) -> (int, int):
        return (0,0)