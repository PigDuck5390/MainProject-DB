from sqlalchemy import Column, Integer, String, Date, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from database import Base

# USERS TABLE
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, Sequence("seq_user_id", start=1, increment=1), primary_key=True)
    user_login_id = Column(String(50), unique=True, nullable=False)
    user_password = Column(String(200), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(Date)
    access_key = Column(String(300))
    last_work = Column(Date)

    folders = relationship("Folder", back_populates="user")
    files = relationship("File", back_populates="user")
    logs = relationship("Log", back_populates="user")


# FOLDERS TABLE
class Folder(Base):
    __tablename__ = "folders"

    folder_id = Column(Integer, Sequence("seq_folder_id", start=1, increment=1), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    folder_name = Column(String(200))
    category_list = Column(String(500))
    connected_directory = Column(String(300))
    category_change = Column(String(300))
    last_work = Column(Date)

    user = relationship("User", back_populates="folders")
    files = relationship("File", back_populates="folder")


# FILES TABLE
class File(Base):
    __tablename__ = "files"

    file_id = Column(Integer, Sequence("seq_file_id", start=1, increment=1), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    folder_id = Column(Integer, ForeignKey("folders.folder_id"))
    file_name = Column(String(200), nullable=False)
    file_type = Column(String(50))
    file_path = Column(String(300))
    is_transform = Column(Integer, default=0)
    transform_txt_path = Column(String(300))
    is_classification = Column(Integer, default=0)
    category = Column(String(200))
    uploaded_at = Column(Date)

    user = relationship("User", back_populates="files")
    folder = relationship("Folder", back_populates="files")
    logs = relationship("Log", back_populates="file")


# LOGS TABLE
class Log(Base):
    __tablename__ = "logs"

    log_id = Column(Integer, Sequence("seq_log_id", start=1, increment=1), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    log_time = Column(Date)
    log_content = Column(String(1000))

    user = relationship("User", back_populates="logs")
    file = relationship("File", back_populates="logs")
