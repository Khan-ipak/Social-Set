from fastapi import FastAPI
from starlette.responses import HTMLResponse

from api.photos import photo_router
from api.users import user_router
from api.hashtags import hashtag_router
from api.comments import comment_router
from api.posts import post_router
from db import Base, engine
# Для создания БД
Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)
app.include_router(hashtag_router)


@app.get("/user/{post_id", response_class=HTMLResponse)
async def main(request: Request, post_id: int):