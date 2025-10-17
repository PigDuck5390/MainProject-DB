from sqlalchemy.orm import Session
from datetime import datetime
from . import models

# ──────────────── USERS ──────────────── #
def create_user(db: Session, login_id: str, email: str, pw_hash: str, directory: str = None):
    user = models.User(
        user_login_id=login_id,
        email=email,
        password_hash=pw_hash,
        user_directory=directory,
        created_at=datetime.now()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_login(db: Session, login_id: str):
    return db.query(models.User).filter(models.User.user_login_id == login_id).first()

def get_all_users(db: Session):
    return db.query(models.User).all()

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


# ──────────────── FILES ──────────────── #
def create_file(db: Session, user_id: int, name: str, ftype: str, directory: str):
    file = models.File(
        user_id=user_id,
        file_name=name,
        file_type=ftype,
        file_directory=directory,
        uploaded_at=datetime.now()
    )
    db.add(file)
    db.commit()
    db.refresh(file)
    return file

def update_file_status(db: Session, file_id: int, transform: int = None, classify: int = None, error: str = None, result: str = None):
    file = db.query(models.File).filter(models.File.file_id == file_id).first()
    if not file:
        return None

    if transform is not None:
        file.is_transform = transform
    if classify is not None:
        file.is_classification = classify
    if error:
        file.error_message = error
    if result:
        file.classification_result = result

    db.commit()
    db.refresh(file)
    return file

def get_files_by_user(db: Session, user_id: int):
    return db.query(models.File).filter(models.File.user_id == user_id).all()


# ──────────────── LOGS ──────────────── #
def add_log(db: Session, file_id: int, content: str):
    log = models.Log(
        file_id=file_id,
        log_time=datetime.now(),
        log_content=content
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_logs_by_file(db: Session, file_id: int):
    return db.query(models.Log).filter(models.Log.file_id == file_id).order_by(models.Log.log_time).all()
