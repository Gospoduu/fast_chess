from .Figures import Figures

class Board:
    @staticmethod
    def arrangement_of_figures(board): # Расстановка фигур
        board = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]
        return board

    def __init__(self):
        self.board = self.arrangement_of_figures()

    def move(self, old_position, new_positions):
        self.board[new_positions[0]][new_positions[1]] = self.board[old_position[0]][old_position[1]]
                   