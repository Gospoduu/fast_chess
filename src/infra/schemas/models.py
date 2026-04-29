from enum import Enum
from typing import Tuple
from uuid import UUID

from pydantic import BaseModel

class User(BaseModel):
    username: str
    id: UUID

class Board(BaseModel):
    id: UUID

class Figure(BaseModel):
    color: str
    type: str
    position: Tuple[int, int]






class Move(BaseModel):
    board: UUID
    figure:

class Game(BaseModel):
    id: UUID
    user_1: UUID
    user_2: UUID

