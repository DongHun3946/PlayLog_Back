from sqlalchemy import (Column, String, Boolean, Float, Date,
                        Text, Integer, BigInteger, DateTime)
from app.db.database import Base
from datetime import datetime, timezone
from app.util.snowflake_id import generate_snowflake_id

class Games(Base):
    __tablename__ = "games"

    id = Column(BigInteger, primary_key=True, default=generate_snowflake_id())
    title = Column(String(200), nullable=False)
    description = Column(Text)

    developer = Column(String(100))  # 개발사
    publisher = Column(String(100))  # 배급사
    release_date = Column(Date)      # 출시일

    genre = Column(String(100))
    platform = Column(String(100))
    price = Column(Integer)
    average_rating = Column(Float, nullable=True)

    thumbnail_url = Column(String(500))

    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    deleted_at = Column(DateTime, nullable=True)
