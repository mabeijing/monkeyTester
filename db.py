# @Time 2022/9/5 10:26
# Author: beijingm
# 写成数据库读写demo

import asyncio
import aiomysql
from aiomysql.pool import Pool
from aiomysql.connection import Connection
from aiomysql.cursors import DictCursor

loop = asyncio.get_event_loop()

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Root123!',
    'db': 'e-shop'
}


async def pools() -> Pool:
    return await aiomysql.create_pool(echo=True, loop=loop, **db_config)


async def select():
    pool: Pool = await pools()
    conn: Connection = await pool.acquire()
    cursor: DictCursor = await conn.cursor(DictCursor)
    await cursor.execute('select * from tb_user where ID=1;')
    data = await cursor.fetchone()
    print(data)
    pool.release(conn)


loop.run_until_complete(select())
