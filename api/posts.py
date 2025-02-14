from fastapi import APIRouter
from db.postservice import *
from api import result_message


post_router = APIRouter(prefix="/posts", tags=["Посты"])


# Новый пост
@post_router.post("/add_post")
async def add_post(user_id: int, main_text: str, hashtag: str):
    result = add_post_db(user_id, main_text, hashtag)
    return result_message(result)


# Вывести пост
@post_router.get("/get_post")
async def get_post(post_id: int = 0):
    result = get_all_or_exact_post(post_id)
    return result_message(result)


# Удалить пост
@post_router.delete("/delete_post")
async def delete_post(post_id: int):
    result = delete_post_db(post_id)
    return result_message(result)


# Изменить пост
@post_router.put("/update_post")
async def edit_post(post_id: int, new_text: str):
    result = update_post_db(post_id, new_text)
    return result_message(result)
