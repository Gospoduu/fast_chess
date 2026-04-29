from uuid import UUID

from pydantic import BaseModel

class CreateChessBoard(BaseModel):
    user_1: UUID
    user_2: UUID

class DoMove(BaseModel):
    user: UUID
    game: UUID
    old_position: list[int]
    new_position: list[int]
