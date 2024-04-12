from pydantic import BaseModel
from queries.pool import connection_pool
from typing import Union, Optional
from datetime import date


class Error(BaseModel):
    message: str


class UserIn(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    member_since: date
    date_of_birth: date
    phone_number: str
    country: str
    state: str
    city: str
    weight: float
    height_cm: float
    skill_level: str
    position: str


class UserOut(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    member_since: date
    date_of_birth: date
    phone_number: str
    country: str
    state: str
    city: str
    weight: float
    height_cm: float
    skill_level: str
    position: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    member_since: Optional[date] = None
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    weight: Optional[float] = None
    height_cm: Optional[float] = None
    skill_level: Optional[str] = None
    position: Optional[str] = None


class UsersRepository:
    def get_all(self):
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute("SELECT * FROM users;")
                users_data = db.fetchall()
                return [
                    UserOut(
                        id=user[0],
                        username=user[1],
                        first_name=user[2],
                        last_name=user[3],
                        email=user[4],
                        password=user[5],
                        member_since=user[6],
                        date_of_birth=user[7],
                        phone_number=user[8],
                        country=user[9],
                        state=user[10],
                        city=user[11],
                        weight=user[12],
                        height_cm=user[13],
                        skill_level=user[14],
                        position=user[15],
                    )
                    for user in users_data
                ]
        except Exception as e:
            return Error(message=f"Failed to retrieve users: {str(e)}")

    def user_in_to_out(self, id: int, user_data: dict) -> Union[UserOut, Error]:
        user_data.pop("id", None)
        return UserOut(id=id, **user_data)

    def create_user(self, user: UserIn) -> Union[UserOut, Error]:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute(
                    """
                    insert into users (
                        username,
                        first_name,
                        last_name,
                        email,
                        password,
                        member_since,
                        date_of_birth,
                        phone_number,
                        country,
                        state,
                        city,
                        weight,
                        height_cm,
                        skill_level,
                        position
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    returning id;
                    """,
                    [
                        user.username,
                        user.first_name,
                        user.last_name,
                        user.email,
                        user.password,
                        user.member_since,
                        user.date_of_birth,
                        user.phone_number,
                        user.country,
                        user.state,
                        user.city,
                        user.weight,
                        user.height_cm,
                        user.skill_level,
                        user.position,
                    ],
                )
                user_id = db.fetchone()[0]
                conn.commit()
                return self.user_in_to_out(user_id, user.model_dump())
        except Exception as e:
            print(e)
            return Error(message=f"Failed to create user: {str(e)}")

    def user_to_out(self, user):
        return UserOut(
            id=user[0],
            username=user[1],
            first_name=user[2],
            last_name=user[3],
            email=user[4],
            password=user[5],
            member_since=user[6],
            date_of_birth=user[7],
            phone_number=user[8],
            country=user[9],
            state=user[10],
            city=user[11],
            weight=user[12],
            height_cm=user[13],
            skill_level=user[14],
            position=user[15],
        )

    def get_by_id(self, id: int) -> Union[UserOut, Error]:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT * FROM users
                    WHERE id = %s;
                    """,
                    [id],
                )
                record = db.fetchone()
                if not record:
                    return None
                return self.user_to_out(record)
        except Exception as e:
            return Error(message=f"Failed to retrieve user: {str(e)}")

    def update_user(self, user_id: int, user: UserUpdate) -> Union[UserOut, Error]:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute("SELECT * FROM users WHERE id = %s;", [user_id])
                existing_user = db.fetchone()
                if not existing_user:
                    return Error(message="User not found.")

                updates, values = [], []
                for field, value in user.model_dump(exclude_none=True).items():
                    updates.append(f"{field} = %s")
                    values.append(value)
                if updates:
                    query = (
                        "UPDATE users SET "
                        + ", ".join(updates)
                        + " WHERE id = %s RETURNING *;"
                    )
                    values.append(user_id)
                    db.execute(query, values)
                    updated_user = db.fetchone()
                    conn.commit()
                    return self.user_in_to_out(
                        user_id, self.user_to_out(updated_user).model_dump()
                    )
                else:
                    return self.user_in_to_out(
                        user_id, self.user_to_out(existing_user).model_dump()
                    )
        except Exception as e:
            return Error(message=f"Failed to update user: {str(e)}")

    def delete_user(self, id: int) -> bool:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM users
                    WHERE id = %s;
                    """,
                    [id],
                )
                conn.commit()
                return True
        except Exception as e:
            return Error(message=f"Failed to delete user: {str(e)}")
