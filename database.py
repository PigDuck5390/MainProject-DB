import os
import oracledb
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# .env 파일 로드 (루트 기준)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))


instant_client_path = r"c:../instantclient-basic-windows.x64-19.28.0.0.0dbru/instantclient_19_28"#경로설정
if os.path.exists(instant_client_path):
    oracledb.init_oracle_client(lib_dir=instant_client_path)


DB_USER = os.getenv("ORACLE_USER", "admin")
DB_PASS = os.getenv("ORACLE_PASSWORD", "1234")
DB_HOST = os.getenv("ORACLE_HOST", "localhost")
DB_PORT = os.getenv("ORACLE_PORT", "1521")
DB_SERVICE = os.getenv("ORACLE_SERVICE", "xe")

# Oracle 접속 URL (oracledb 드라이버 사용)
DATABASE_URL = f"oracle+oracledb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_SERVICE}"

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

# 세션 설정
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base 클래스
Base = declarative_base()

# FastAPI 의존성용 세션 생성기
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
