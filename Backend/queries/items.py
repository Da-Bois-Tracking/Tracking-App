# queries/items.py
from pydantic import BaseModel
from queries.pool import connection_pool
from typing import Union


class Error(BaseModel):
    message: str


class ItemIn(BaseModel):
    title: str
    description: str


class ItemOut(BaseModel):
    id: int
    title: str
    description: str


class ItemsRepository:
    def get_all(self):
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute("SELECT * FROM items;")
                items_data = db.fetchall()
                return [
                    ItemOut(id=item[0], title=item[1], description=item[2])
                    for item in items_data
                ]
        except Exception as e:
            return Error(message=f"Failed to retrieve items: {str(e)}")

    def item_in_to_out(self, id: int, item: ItemOut):
        old_data = item.model_dump()
        return ItemOut(id=id, **old_data)

    def create_item(self, item: ItemIn) -> ItemOut:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute(
                    """
                    insert into items (title, description)
                    values (%s, %s)
                    returning id;
                    """,
                    [
                        item.title,
                        item.description,
                    ],
                )
                id = db.fetchone()[0]
                conn.commit()
                return self.item_in_to_out(id, item)
        except Exception as e:
            return Error(message=f"Failed to create item: {str(e)}")

    def item_to_out(self, item):
        return ItemOut(
            id=item[0],
            title=item[1],
            description=item[2],
        )

    def get_by_id(self, id: int) -> Union[ItemOut, Error]:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT * FROM items
                    WHERE id = %s;
                    """,
                    [id],
                )
                record = db.fetchone()
                if not record:
                    return None
                return self.item_to_out(record)
        except Exception as e:
            return Error(message=f"Failed to retrieve item: {str(e)}")

    def update_item(self, id: int, item: ItemIn) -> Union[ItemOut, Error]:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute(
                    """
                    UPDATE items
                    SET title = %s, description = %s
                    WHERE id = %s
                    RETURNING *;
                    """,
                    [
                        item.title,
                        item.description,
                        id,
                    ],
                )
                conn.commit()
                record = db.fetchone()
                if not record:
                    return None
                return self.item_to_out(record)
        except Exception as e:
            return Error(message=f"Failed to update item: {str(e)}")

    def delete_item(self, id: int) -> bool:
        try:
            conn = connection_pool.getconn()
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM items
                    WHERE id = %s;
                    """,
                    [id],
                )
                conn.commit()
                return True
        except Exception as e:
            return Error(message=f"Failed to delete item: {str(e)}")
