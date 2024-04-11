from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.users import UserOut, UsersRepository, Error, UserIn

router = APIRouter()


@router.get("/users/", response_model=List[UserOut], tags=["Users"])
def get_users(
    repo: UsersRepository = Depends(),
):
    return repo.get_all()


@router.post("/users/", response_model=Union[UserOut, Error], tags=["Users"])
def create_user(
    user: UserIn,
    repo: UsersRepository = Depends(),
):
    return repo.create_user(user)


@router.get("/users/{user_id}", response_model=Union[UserOut, Error], tags=["Users"])
def get_user(
    user_id: int,
    response: Response,
    repo: UsersRepository = Depends(),
) -> Union[UserOut, Error]:
    record = repo.get_by_id(user_id)
    if record is None:
        response.status_code = 404
    return record


@router.put("/users/{user_id}", response_model=Union[UserOut, Error], tags=["Users"])
def update_user(
    user_id: int,
    user: UserIn,
    repo: UsersRepository = Depends(),
) -> Union[UserOut, Error]:
    return repo.update_user(user_id, user)


@router.delete("/users/{user_id}", response_model=bool, tags=["Users"])
def delete_user(
    user_id: int,
    repo: UsersRepository = Depends(),
) -> bool:
    return repo.delete_user(user_id)
