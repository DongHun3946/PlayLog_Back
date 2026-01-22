from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.database import Base
class Users(Base):
    __tablename__ = "users"  # __이름__ 는 프레임 워크 및 언어 내부용 예약어

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    is_deleted = Column(Boolean, default=False)

