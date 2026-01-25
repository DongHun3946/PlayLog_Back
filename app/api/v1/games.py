from fastapi import APIRouter
from app.db.database import get_db


router = APIRouter(
    prefix="/games",
    tags=["games"]
)