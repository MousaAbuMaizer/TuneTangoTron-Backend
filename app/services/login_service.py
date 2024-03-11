from database.cruds.crud_interface import ICRUD
from fastapi import HTTPException
from services.encrypt_service import encrypt_password 
from database.data_transfer_object.user_dto import UserDTO

class LoginService:
    def __init__(self, crud_service: ICRUD):
        self.crud_service = crud_service

    def login(self, username: str, password: str) -> UserDTO:
        try:
            user_dto = self.crud_service.get(username)
            if(user_dto is None or not encrypt_password(password) == user_dto.password_hash):
                raise HTTPException(status_code=401, detail="Invalid username or password")
            return user_dto
        except Exception as e:
            print(f"An error occurred during login: {e}")
            raise HTTPException(status_code=500, detail="An error occurred during login.")
