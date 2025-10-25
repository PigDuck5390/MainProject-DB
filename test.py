import oracledb, os
from sqlalchemy import create_engine

# ============================================================
# ① Oracle 연결 정보
# ============================================================
instant_client_path = r"c:\Users\4Class_03\Downloads\instantclient-basic-windows.x64-19.28.0.0.0dbru\instantclient_19_28"#경로 설정
if os.path.exists(instant_client_path):
    oracledb.init_oracle_client(lib_dir=instant_client_path)

DB_USER = "asdf"
DB_PASS = "1234"
DB_HOST = "localhost"
DB_PORT = "1521"
DB_SERVICE = "xe"

DATABASE_URL = f"oracle+oracledb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_SERVICE}"

# ============================================================
# ② 엔진 생성 및 연결 테스트
# ============================================================
print("🔍 Oracle DB Insert 테스트 시작...\n")

try:
    print("Oracle Client 버전:", oracledb.clientversion())
except Exception as e:
    print("⚠️ 클라이언트 버전 확인 실패:", e)

try:
    engine = create_engine(DATABASE_URL, echo=False)
    conn = engine.connect()
    print("✅ Oracle DB 연결 성공\n")
except Exception as e:
    print("❌ DB 연결 실패:", e)
    exit(1)