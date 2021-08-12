import asyncio
import os
import sys
import asyncpg
import logging

from config import HOST, PG_PASS, PG_USER

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def create_db():
    create_db_command = open(os.path.join(sys.path[0], "utils/db/create_db.sql"), "r").read()

    logging.info("Connecting to database...")
    conn: asyncpg.Connection = await asyncpg.connect(user=PG_USER, password=PG_PASS, host=HOST)

    try:
        await conn.execute(create_db_command)
    except asyncpg.exceptions.DuplicateTableError:
        pass
    await conn.close()
    logging.info("Table USERS created")


async def create_pool():
    return await asyncpg.create_pool(user=PG_USER, password=PG_PASS, host=HOST)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
