# user_crud.py
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from database.database import AbstractDatabase
from database.models.user import User
from database.cruds.crud_interface import ICRUD
from dto.user_dto import UserDTO
from typing import Optional, Union

class UserCRUD(ICRUD):
    def __init__(self, db: AbstractDatabase):
        self.db = db

    def add(self, username: str, password_hash: str) -> UserDTO:
        session: Session = self.db.get_session()
        new_user = User(username=username, password_hash=password_hash)
        try:
            session.add(new_user)
            session.commit()
            return UserDTO.from_orm(new_user)
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get(self, identifier: Union[int, str]) -> Optional[UserDTO]:
        session: Session = self.db.get_session()
        try:
            if isinstance(identifier, int):
                user = session.query(User).filter(User.id == identifier).first()
            elif isinstance(identifier, str):
                user = session.query(User).filter(User.username == identifier).first()
            else:
                return None  # Or raise an exception for invalid identifier type
            
            if user:
                return UserDTO.from_orm(user)
            else:
                return None
        except SQLAlchemyError as e:
            raise e
        finally:
            session.close()

    def update(self, user_id: int, **kwargs) -> UserDTO:
        session: Session = self.db.get_session()
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                for key, value in kwargs.items():
                    setattr(user, key, value)
                session.commit()
                return UserDTO.from_orm(user)
            else:
                return None
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(self, user_id: int) -> bool:
        session: Session = self.db.get_session()
        try:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
