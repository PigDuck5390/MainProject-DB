import oracledb, os
from sqlalchemy import create_engine, text
from datetime import datetime

# ============================================================
# ① Oracle 연결 정보
# ============================================================
instant_client_path = r"c:../instantclient-basic-windows.x64-19.28.0.0.0dbru/instantclient_19_28"#경로 설정
if os.path.exists(instant_client_path):
    oracledb.init_oracle_client(lib_dir=instant_client_path)

DB_USER = "admin"
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

# ============================================================
# ③ 데이터 추가 (INSERT)
# ============================================================

try:
    # 1️⃣ USERS 추가
    insert_user = text("""
        INSERT INTO USERS (USER_ID, USER_LOGIN_ID, EMAIL, PASSWORD_HASH, CREATED_AT)
        VALUES (SEQ_USER_ID.NEXTVAL, :login, :email, :pw, SYSDATE)
    """)
    conn.execute(insert_user, {
        "login": "test_user",
        "email": "test_user@example.com",
        "pw": "hashed_pw_123"
    })
    print("👤 USERS 데이터 추가 완료")

    # 2️⃣ FILES 추가
    insert_file = text("""
        INSERT INTO FILES (FILE_ID, USER_ID, FILE_NAME, FILE_TYPE, FILE_DIRECTORY, UPLOADED_AT)
        VALUES (SEQ_FILE_ID.NEXTVAL, (SELECT MAX(USER_ID) FROM USERS),
                :name, :type, :dir, SYSDATE)
    """)
    conn.execute(insert_file, {
        "name": "sample.pdf",
        "type": "pdf",
        "dir": "/uploads/test_user/"
    })
    print("📁 FILES 데이터 추가 완료")

    # 3️⃣ LOGS 추가
    insert_log = text("""
        INSERT INTO LOGS (LOG_ID, FILE_ID, LOG_TIME, LOG_CONTENT)
        VALUES (SEQ_LOG_ID.NEXTVAL, (SELECT MAX(FILE_ID) FROM FILES),
                SYSDATE, :content)
    """)
    conn.execute(insert_log, {
        "content": "OCR 완료 및 Gemma 분류 성공"
    })
    print("🧾 LOGS 데이터 추가 완료")

    # 커밋
    conn.commit()
    print("\n✅ 모든 데이터 정상 저장 완료!")
except Exception as e:
    conn.rollback()
    print("❌ 데이터 추가 중 오류 발생:", e)
finally:
    conn.close()
    print("\n🔚 테스트 종료.")
