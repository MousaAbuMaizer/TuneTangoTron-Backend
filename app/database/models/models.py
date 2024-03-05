from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from  database.database import SqlAlchemyDatabaseConnection

class User(SqlAlchemyDatabaseConnection.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(255))

    def __repr__(self):
        return f"<User(username='{self.username}', id='{self.id}')>"

class SavedFile(SqlAlchemyDatabaseConnection.Base):
    __tablename__ = 'saved_file'
    id = Column(Integer, primary_key=True)
    file_address = Column(String(255), nullable=False)

    # Foreign key to associate a deployment with a user
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    def __repr__(self):
        return f"<SavedFile(file_name='{self.file_address}', user_id='{self.user_id}')>"
