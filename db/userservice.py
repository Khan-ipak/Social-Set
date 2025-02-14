from db import get_db
from db.models import User


# Добавления пользователя // регистрация
def add_user_db(usernmane, password, email, name, surname = None, age = None, city = None):
    db = next(get_db())
    new_user = User(usernmane=usernmane, password=password, email=email,
                    name=name, surname=surname, age=age, city=city)

    db.add (new_user)
    db.commit()
    return True

# Получение пользователей
def get_exact_or_all_users(user_id=0):
    db = next(get_db())
    if user_id:
        exact_user = db.query(User).filter_by(id=user_id).first()
        if exact_user:
            return exact_user
        return False
    return db.query(User).all()


# Удаление пользователя
def delete_user_db(user_id):
    db = next(get_db())
    to_delete_user = db.query(User).filter_by(id=user_id).first()
    if to_delete_user:
        db.delete(to_delete_user)
        db.commit()
        return True
    return False


# Изменение данных пользователя
def update_user_db(user_id, change_info, new_info):
    db = next(get_db())
    to_update_user = db.query(User).filter_by(id=user_id).first()
    if to_update_user:
        if change_info == "name":
            to_update_user.name = new_info
        elif change_info == "surname":
            to_update_user.surname = new_info
        elif change_info == "username":
            to_update_user.username = new_info
        elif change_info == "email":
            to_update_user.email = new_info
        elif change_info == "age":
            to_update_user.age = new_info
        elif change_info == "password":
            to_update_user.password = new_info
        elif change_info == "city":
            to_update_user.city = new_info
        db.commit()
        return True
    return False
