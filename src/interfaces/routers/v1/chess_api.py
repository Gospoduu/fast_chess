from uuid import uuid4, UUID

from fastapi import APIRouter, Depends

from src.infra.schemas.chess import CreateChessBoard, DoMove

router = APIRouter()

@router.post("/chess")
async def create_game(CreateChessBoard: CreateChessBoard):
    return uuid4

@router.get("/chess/{id}")
async def get_game(id: UUID):
    return uuid4

@router.put("/chess/move")
async def update_game(id: UUID, move: DoMove):
    pass