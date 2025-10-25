from database import engine
from models import Base

def create_tables():

    print(" 테이블 생성 중...")

    try:
        Base.metadata.create_all(bind=engine)
        print("모든 테이블이 성공적으로 생성되었습니다.")
    except Exception as e:
        print("테이블 생성 중 오류 발생:", e)


if __name__ == "__main__":
    create_tables()
