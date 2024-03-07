from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import database


class SavedFile(database.SqlAlchemyDatabaseConnection.Base):
    __tablename__ = 'saved_file'
    id = Column(Integer, primary_key=True)
    file_address = Column(String(255), nullable=False)

    # Foreign key to associate a deployment with a user
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    def __repr__(self):
        return f"<SavedFile(file_name='{self.file_address}', user_id='{self.user_id}')>"
