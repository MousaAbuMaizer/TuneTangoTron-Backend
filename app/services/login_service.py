from database.cruds.crud_interface import ICRUD
from fastapi import HTTPException
from services.encrypt_service import EncryptService 
from database.data_transfer_object import user_dto

class LoginService:
    def __init__(self, crud_service: ICRUD):
        self.crud_service = crud_service

    def login(self, username: str, password: str) -> bool:
        try:
            user_dto = self.crud_service.get(username)
            # if user_dto is None or not EncryptService.checkPassword(input_password=password,stored_hashed_password= user_dto.password_hash):
            #     raise HTTPException(status_code=401, detail="Invalid username or password")
            if(user_dto is None or not (password == user_dto.password_hash)):
                raise HTTPException(status_code=401, detail="Invalid username or password")
            return True
            # Successful login logic here (if needed)
        except Exception as e:
            # Log the error
            print(f"An error occurred during login: {e}")
            raise HTTPException(status_code=500, detail="An error occurred during login.")
