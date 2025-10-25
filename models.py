from sqlalchemy import Column, Integer, String, Date, Sequence, Numeric
from database import Base

# USERS 테이블
user_id_seq = Sequence("SEQ_USER_ID", start=1, increment=1)

class User(Base):
    __tablename__ = "USERS"

    user_id = Column("USER_ID", Integer, user_id_seq,
                     primary_key=True,
                     server_default=user_id_seq.next_value())

    user_login_id = Column("USER_LOGIN_ID", String(50),
                           unique=True, nullable=False)

    user_password = Column("USER_PASSWORD", String(200),
                           nullable=False)

    email = Column("EMAIL", String(100),
                   unique=True, nullable=False)

    created_at = Column("CREATED_AT", Date)
    access_key = Column("ACCESS_KEY", String(100))
    last_work = Column("LAST_WORK", Date)


# FOLDERS 테이블
folder_id_seq = Sequence("SEQ_FOLDER_ID", start=1, increment=1)

class Folder(Base):
    __tablename__ = "FOLDERS"

    folder_id = Column("FOLDER_ID", Integer, folder_id_seq,
                       primary_key=True,
                       server_default=folder_id_seq.next_value())

    user_id = Column("USER_ID", Integer, nullable=False)
    folder_name = Column("FOLDER_NAME", String(200))
    category_list = Column("CATEGORY_LIST", String(500))
    connected_directory = Column("CONNECTED_DIRECTORY", String(300))
    category_change = Column("CATEGORY_CHANGE", String(300))
    last_work = Column("LAST_WORK", Date)


# FILES 테이블
file_id_seq = Sequence("SEQ_FILE_ID", start=1, increment=1)

class File(Base):
    __tablename__ = "FILES"

    file_id = Column("FILE_ID", Integer, file_id_seq,
                     primary_key=True,
                     server_default=file_id_seq.next_value())

    user_id = Column("USER_ID", Integer, nullable=False)
    folder_id = Column("FOLDER_ID", Integer)
    file_name = Column("FILE_NAME", String(200), nullable=False)
    file_type = Column("FILE_TYPE", String(50))
    file_path = Column("FILE_PATH", String(300))
    is_transform = Column("IS_TRANSFORM", Numeric(1), default=0)
    transform_txt_path = Column("TRANSFORM_TXT_PATH", String(300))
    is_classification = Column("IS_CLASSIFICATION", Numeric(1), default=0)
    category = Column("CATEGORY", String(200))
    uploaded_at = Column("UPLOADED_AT", Date)


# LOGS 테이블
log_id_seq = Sequence("SEQ_LOG_ID", start=1, increment=1)

class Log(Base):
    __tablename__ = "LOGS"

    log_id = Column("LOG_ID", Integer, log_id_seq,
                    primary_key=True,
                    server_default=log_id_seq.next_value())

    user_id = Column("USER_ID", Integer, nullable=False)
    log_time = Column("LOG_TIME", Date)
    log_content = Column("LOG_CONTENT", String(1000))
