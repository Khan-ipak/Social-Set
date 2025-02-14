from fastapi import APIRouter
from db.postservice import *
from api import result_message

comment_router = APIRouter(prefix="/comments", tags=["Комментарии"])


# Добавление коммента
@comment_router.post("/add_comment")
async def add_comment(user_id: int, post_id: int, text: str):
    result = add_comment_to_db(user_id, post_id, text)
    return result_message(result)


# Получение коммента
@comment_router.get("/get_comments")
async def get_comments(comment_id: int = 0):
    result = get_all_or_exact_comments(comment_id)
    return result_message(result)


# Изменение коммента
@comment_router.put("/update_comment")
async def update_comment(comment_id: int, new_text: str):
    result = update_comment_db(comment_id, new_text)
    return result_message(result)


# удаление коммента
@comment_router.delete("/delete_comment")
async def delete_comment(comment_id):
    result = delete_comment_db(comment_id)
    return result_message(result)