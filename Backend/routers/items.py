# routers/items.py
from fastapi import APIRouter, Depends, Response, HTTPException
from typing import List, Union
from queries.items import ItemIn, ItemOut, ItemsRepository, Error

router = APIRouter()
repository = ItemsRepository()


@router.get("/items/", response_model=List[ItemOut], tags=["Items"])
def get_items(
    repo: ItemsRepository = Depends(),
):
    return repository.get_all()


@router.post(
    "/items/",
    response_model=Union[ItemOut, Error],
    tags=["Items"],
)
def create_item(
    item: ItemIn,
    repo: ItemsRepository = Depends(),
):
    return repository.create_item(item)


@router.get("/items/{item_id}", response_model=Union[ItemOut, Error], tags=["Items"])
def get_item(
    item_id: int,
    response: Response,
    repo: ItemsRepository = Depends(),
) -> Union[ItemOut, Error]:
    record = repo.get_by_id(item_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return record


@router.put(
    "/items/{item_id}",
    response_model=Union[ItemOut, Error],
)
def update_item(
    item_id: int,
    item: ItemIn,
    repo: ItemsRepository = Depends(),
):
    return repo.update_item(item_id, item)


@router.delete(
    "/items/{item_id}",
    response_model=bool,
)
def delete_item(
    item_id: int,
    repo: ItemsRepository = Depends(),
) -> bool:
    return repo.delete_item(item_id)
