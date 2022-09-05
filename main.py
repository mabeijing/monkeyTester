# @Time 2022/9/3 19:05
# Author: beijingm
import asyncio
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Hobby(BaseModel):
    id: int  # id
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    hobby: list[Hobby]


@app.get("/")
async def index():
    await asyncio.sleep(5)
    return {"message": "Hello World!"}


@app.post("/user/{user_id}")
async def user(user_id: int):
    """
    :param user_id: 函数的类型，可以直接用于参数校验
    :return:
    """
    return {"user_id": user_id}


@app.get("/items/")
async def items(skip: int = 0, limit: int = 0):
    """
    :param skip: localhost:8000/items?skip=10&limit=22
    :param limit:
    :return:
    """
    return {"item": {"skip": skip, "limit": limit}}


@app.post("/get-item/")
async def create_item(item: Item):
    return item
