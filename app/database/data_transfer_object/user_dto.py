from pydantic import BaseModel

class UserDTO(BaseModel):
    id: int
    username: str
    password_hash: str

    class Config:
        from_attributes = True