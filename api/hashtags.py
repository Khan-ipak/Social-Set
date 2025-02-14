from fastapi import APIRouter
from db.postservice import *
from api import result_message

hashtag_router = APIRouter(prefix="/hashtags", tags=["Хэштеги"])


# Добавление хэштега
@hashtag_router.post("/add_hashtag")
async def add_hashtag(text: str):
    result = add_hashtag_db(text)
    return result_message(result)

# Получение хэштега
@hashtag_router.get("/get_hashtag")
async def get_hashtag(hashtag_text: str = None):
    result = get_all_or_exact_comments(hashtag_text)
    return result_message(result)

# Удаление хэштега
@hashtag_router.delete("/delete_hashtag")
async def delete_hashtag(hashtag_id: int):
    result = delete_hashtag_db(hashtag_id)
    return result_message(result)