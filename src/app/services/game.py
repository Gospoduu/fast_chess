from uuid import UUID, uuid4
from typing import Tuple

from src.app.services.move_validator import MoveValidator
from src.infra.schemas.models import Figure

class Game:
    def __init__(self):
        self.id: UUID = uuid4()
        self.player1: UUID = uuid4()
        self.player2: UUID = uuid4()
        self.board: list[list[int]] = []
        self.validator: MoveValidator = MoveValidator()

    async def do_move(
            self,
            player: UUID,
            figure: Figure,
            old_position: Tuple[int, int],
            new_position: Tuple[int, int]
    ):
        pass




