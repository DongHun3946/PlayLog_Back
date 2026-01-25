from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Boolean
from app.db.database import Base
from datetime import datetime, timezone
from app.util.snowflake_id import generate_snowflake_id

class Users(Base):
    __tablename__ = "users"  # __이름__ 는 프레임 워크 및 언어 내부용 예약어

    id = Column(BigInteger, primary_key=True, default=generate_snowflake_id())
    nick_name = Column(String(100))
    email = Column(String(100))
    is_deleted = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_date = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    deleted_date = Column(DateTime, nullable=True)

