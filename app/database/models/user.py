from sqlalchemy import Column, Integer, String
from database import database


class User(database.SqlAlchemyDatabaseConnection.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255))

    def __repr__(self):
        return f"<User(username='{self.username}', id='{self.id}')>"