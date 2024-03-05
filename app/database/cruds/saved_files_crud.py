# savedFileCrud.py
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database.database import AbstractDatabase
from database.models.models import SavedFile
from database.cruds.crud_interface import ICRUD


class SavedFileCRUD(ICRUD):
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def add(self, file_address: str, user_id: int) -> SavedFile:
        session: Session = self.db.get_session()
        new_saved_file = SavedFile(file_address=file_address, user_id=user_id)
        try:
            session.add(new_saved_file)
            session.commit()
            return new_saved_file
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            self.db.close_session(session)

    def get(self, saved_file_id: int) -> SavedFile:
        session: Session = self.db.get_session()
        try:
            saved_file = session.query(SavedFile).filter(SavedFile.id == saved_file_id).first()
            return saved_file
        except SQLAlchemyError as e:
            raise e
        finally:
            self.db.close_session(session)

    def update(self, saved_file_id: int, **kwargs) -> SavedFile:
        session: Session = self.db.get_session()
        try:
            saved_file = session.query(SavedFile).filter(SavedFile.id == saved_file_id).first()
            if saved_file:
                for key, value in kwargs.items():
                    setattr(saved_file, key, value)
                session.commit()
                return saved_file
            return None
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            self.db.close_session(session)

    def delete(self, saved_file_id: int) -> bool:
        session: Session = self.db.get_session()
        try:
            saved_file = session.query(SavedFile).filter(SavedFile.id == saved_file_id).first()
            if saved_file:
                session.delete(saved_file)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            self.db.close_session(session)
