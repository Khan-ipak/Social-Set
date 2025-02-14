from fastapi import APIRouter

from api import result_message
from db.userservice import *
from pydantic import BaseModel, EmailStr


user_router = APIRouter(prefix="/users", tags=["Пользователи"])


class UserCreate(BaseModel):
    username: str
    name: str
    email: EmailStr
    password: str
    surname: str = None
    age: str = None
    city: str = None


@user_router.post("/add_user")
async def add_user(user_data: UserCreate):
    user_dict = dict(user_data)
    result = add_user_db(**user_dict)
    return result


@user_router.get("/get_user")
async def get_user(user_id: int = 0):
    result = get_exact_or_all_users(user_id)
    return result_message(result)


@user_router.delete("/delete_user")
async def delete_user(user_id: int):
    result = delete_user_db(user_id)
    return result_message(result)


@user_router.put("/update_user")
async def update_user(user_id: int, change_info: str, new_info: str):
    result = update_user_db(user_id, change_info, new_info)
    return result_message(result)
