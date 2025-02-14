from db import get_db
from db.models import PostPhoto, UserPost, Comment, Hashtag

"""
UserPost

1. добавление поста add_post_db(user_id, main_text, hashtag) 
2. получение постов get_all_or_exact_post(post_id=0)
3. удаление пота delete_post_db(post_id)
4. изменение поста update_post_db(post_idm new_hashtag)
"""




"""
Comment

1. добавлние коммента add_comment_db(user_id, post_id, text)
2. получение комментов get_all_or_exact_comments(comment_id=0)
3. удаление коммента delete_comment_db(comment_id)
4. изменение коммента update_comment_db(comment_id, new_text)
"""


# Добавление нового поста
def add_post_db(user_id, main_text, hashtag):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, main_text=main_text, hashtag=hashtag)

    db.add(new_post)
    db.commit()
    return True
# Получение всех постов, либо одного
def get_all_or_exact_post(post_id = 0):
    db = next(get_db())
    if post_id:
        all_post = db.query(UserPost).filter_by(id=post_id).first()
        if all_post:
            return all_post
        return False
    return db.query(UserPost).all()
# Удаление поста
def delete_post_db(post_id):
    db = next(get_db())
    to_delete_post = db.query(UserPost).filter_by(id=post_id).first()
    if to_delete_post:
        db.delete(to_delete_post)
        db.commit()
        return True
    return False


def update_post_db(post_id, new_text):
    db = next(get_db())
    update_post = db.query(UserPost).filter_by(id=post_id).first()
    if update_post:
        update_post.main_text = new_text
        db.commit()
        return True
    return False


# CRUD для комментов

def add_comment_to_db(user_id, post_id, text):
    db = next(get_db())
    comment = Comment(user_id=user_id, post_id=post_id, comment=text)

    db.add(comment)
    db.commit()

    return True


def get_all_or_exact_comments(comment_id=0):
    db = next(get_db())

    if comment_id:
        comment = db.query(Comment).filter_by(id=comment_id).first()

        if comment:
            return comment
        return False
    return db.query(Comment).all()


def delete_comment_db(comment_id):
    db = next(get_db())
    comment_to_delete = db.query(Comment).filter_by(id=comment_id).first()

    if comment_to_delete:
        db.delete(comment_to_delete)
        db.commit()

        return True
    return False


def update_comment_db(comment_id, new_text):
    db = next(get_db())
    comment = db.query(Comment).filter_by(id=comment_id).first()

    if comment:
        comment.comment = new_text
        db.commit()

        return True
    return False


"""
Hashtag

1. добавление хэштега add_hashtag_db(hashtag_text)
2. получение хэштега get_all_or_exact_hashtags(hashatg_text=None)
3. удаление хэштега delete_hashtag_db(hashtag_id)
4. PostPhoto: добавление фото add_photo_db(post_id, photo_file)
"""


# Добавление хэштега
def add_hashtag_db(hashtag_text):
    db = next(get_db())
    new_hashtag = Hashtag(text=hashtag_text)

    db.add(new_hashtag)
    db.commit()
    return True


# Получение хэштега
def get_all_or_exact_hashtags(hashtag_text=None):
    db = next(get_db())
    if hashtag_text:
        exact_hashtag = db.query(Hashtag).filter_by(text=hashtag_text).first()
        if exact_hashtag:
            return exact_hashtag
        return False
    return db.query(Hashtag).all()


# Удаление хэштега
def delete_hashtag_db(hashtag_id):
    db = next(get_db())
    to_delete_hashtag = db.query(Hashtag).filter_by(id=hashtag_id).first()
    if to_delete_hashtag:
        db.delete(to_delete_hashtag)
        db.commit()
        return True
    return False


# Добавление фото
def add_photo_db(post_id, photo_file):
    db = next(get_db())
    new_photo = PostPhoto(post_id=post_id, photo_file=photo_file)

    db.add(new_photo)
    db.commit()