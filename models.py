# @Time 2022/9/3 22:28
# Author: beijingm

from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


if __name__ == '__main__':
    user = User(name='beijingm', age=33)
    print(user.dict())

