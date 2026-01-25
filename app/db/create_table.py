from app.db.database import Base, engine

Base.metadata.drop_all(bind=engine)
print("기존 테이블 제거 완료")
Base.metadata.create_all(bind=engine)
print("테이블 생성 완료")

