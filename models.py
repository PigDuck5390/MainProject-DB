from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_login_id = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(200), nullable=False)
    access_key = Column(String(100))
    user_directory = Column(String(200))
    created_at = Column(Date)

    files = relationship("File", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"<User(id={self.user_id}, login='{self.user_login_id}')>"


class File(Base):
    __tablename__ = "files"

    file_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    file_name = Column(String(200), nullable=False)
    file_type = Column(String(50))
    file_directory = Column(String(300))
    is_transform = Column(Integer, default=0)
    is_classification = Column(Integer, default=0)
    hide = Column(Integer, default=0)
    classification_result = Column(String(200))
    uploaded_at = Column(Date)

    user = relationship("User", back_populates="files")
    logs = relationship("Log", back_populates="file", cascade="all, delete")

    def __repr__(self):
        return f"<File(id={self.file_id}, name='{self.file_name}')>"


class Log(Base):
    __tablename__ = "logs"

    log_id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey("files.file_id", ondelete="CASCADE"), nullable=False)
    log_time = Column(Date)
    log_content = Column(String(1000))

    file = relationship("File", back_populates="logs")

    def __repr__(self):
        return f"<Log(id={self.log_id}, file_id={self.file_id})>"
