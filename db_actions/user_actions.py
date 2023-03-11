from models.user import User
from auth.oauth import password_hasher
from models.base_model import database
from models.user_detail import UserDetail
from helper.sort_order_mapper import mapper
from schemas.iuser import IUser, IUserQueryParams, IUserUpdate


class UserActions:

    @staticmethod
    @database.atomic()
    def create_user(user: IUser, creator: int):
        try:
            user_ = user.dict()
            user_detail = (
                user.personal_detail.dict().copy()
                if user.personal_detail else None
            )
            del user_["personal_detail"]
            user_["createdby"] = user_["last_updatedby"] = creator
            user_["password"] = password_hasher(user.password)
            q: int = User.create(**user_)
            UserDetail.create(
                user_id=q, **user_detail) if user_detail else None
            return UserActions.get_user_by_id(q)
        except Exception as e:
            print(e)
            raise ValueError(e)

    @staticmethod
    def update_user(user_id: int, user: IUserUpdate, creator: int):
        # hsl(351, 55%, 65%) Note(bugs): set last updated //
        # middle can't be set to null // user personal details
        # (should be create or update)
        user_detail = (
            user.personal_detail.dict().copy()
            if user.personal_detail else None
        )
        user_detail = {x: y for x,y in user_detail.items()} if user_detail else None
        user_ = {x: y for x, y in user.dict().items() if y != None}
        del user_["personal_detail"]
        User.update(**user_).where(User.user_id == user_id).execute()
        exist_pd = UserDetail.get_or_none(UserDetail.user_id == user_id)
        if exist_pd:
            UserDetail.update(**user_detail).where(
                UserDetail.user_id == user_id
            ).execute() if user_detail else None
        else:
            UserDetail.create(user_id=user_id, **
                              user_detail) if user_detail else None
        return UserActions.get_user_by_id(user_id)

    @staticmethod
    def get_users(params: IUserQueryParams):
        sb = mapper(User, params.sort_by, params.order)
        sort_by = sb if sb else [User.user_id]
        rows = (
            User.select()
            .where(
                User.user_name.contains(params.name)
                if params.name else True
            )
            .order_by(*sort_by)
            .limit(params.limit)
            .offset(params.skip)
            .dicts()
        )
        print(rows.sql())
        return [row for row in rows]

    @staticmethod
    def get_user_by_id(id_: int):
        rows = User.select().where(User.user_id == id_).dicts()
        user = [row for row in rows]
        try:
            return user[0]
        except IndexError:
            raise ValueError("User not found")

    @staticmethod
    def get_user_by_username(username: str):
        rows = (
            User.select()
            .where(User.user_name == username)
            .dicts()
        )
        user = [row for row in rows]

        try:
            return user[0]
        except IndexError:
            raise ValueError(f"No user with name {username} found.")

    @staticmethod
    def delete_user(id_: int, current_user: int):
        user = UserActions.get_user_by_id(id_)
        User.delete().where(User.user_id == id_).execute()
        return user

    # def disable_user(id_: int):
    #     pass

    # def enable_user(id_: int):
    #     pass

    # def update_user_access(id_: int, new_access: int):
    #     pass

    # def generate_username():
    #     pass
