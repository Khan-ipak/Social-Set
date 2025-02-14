from fastapi import APIRouter, UploadFile, File
import random

from db.postservice import add_photo_db

photo_router = APIRouter(prefix="/photo", tags=["Фотографии"])

@photo_router.post("/add_photo")
async def add_photo_api(post_id: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1_000_000)
    if photo_file:
        with open(f"db/images/photo_{file_id}_{post_id}.jpg", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
            add_photo_db(post_id, photo.name)
            return {"status": 1, "message": "Фото успешно сохранено"}
    return {"status": 0, "message": False}