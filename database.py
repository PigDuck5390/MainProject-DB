import os
import oracledb
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# env 파일 로드
load_dotenv()

# Oracle Instant Client 초기화
instant_client_path = r"c:/Users/4Class_03/Downloads/instantclient-basic-windows.x64-19.28.0.0.0dbru/instantclient_19_28"
if os.path.exists(instant_client_path):
    oracledb.init_oracle_client(lib_dir=instant_client_path)

# 환경 변수 불러오기
DB_USER = os.getenv("ORACLE_USER")
DB_PASS = os.getenv("ORACLE_PASSWORD")
DB_HOST = os.getenv("ORACLE_HOST")
DB_PORT = os.getenv("ORACLE_PORT")
DB_SERVICE = os.getenv("ORACLE_SERVICE")

# SQLAlchemy용 URL 생성
DATABASE_URL = (
    f"oracle+oracledb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"
)

# 엔진, 세션, 베이스 설정
engine = create_engine(
    DATABASE_URL,
    echo=True,            
    pool_pre_ping=True,   
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# 세션 종속성 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
