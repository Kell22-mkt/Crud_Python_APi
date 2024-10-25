from pydantic import BaseModel

class UserBase(BaseModel):
    nome: str
    email: str
    idade: int

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
