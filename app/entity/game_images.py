from sqlalchemy import Column, Integer, BigInteger, String
from app.db.database import Base

class Game_images(Base):
    __tablename__ = "games_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    game_id = Column(BigInteger, nullable=False)
    image_url = Column(String(500))
    image_type = Column(String(30)) # 썸네일, 배너, 메인, 스크린샷인지에 대한 타입
