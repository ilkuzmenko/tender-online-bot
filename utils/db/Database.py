import asyncio
import os
import sys
import asyncpg
import logging

from config import HOST, PG_PASS, PG_USER

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


class Database:

    def __init__(self):
        self.pool = None

    async def connect(self):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(user=PG_USER, password=PG_PASS, host=HOST)
            logging.info("Successfully initialized database pool")

    async def create_table(self, table: str):
        with open(os.path.join(sys.path[0], "utils/db/" + table + ".sql"), "r") as file:
            sql = file.read()
        try:
            await self.pool.execute(sql)
            logging.info("Table " + table + " successfully created")
        except asyncpg.exceptions.DuplicateTableError:
            pass

    async def disconnect(self):
        await self.pool.close()


if __name__ == "__main__":
    db = Database()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.connect())
    loop.run_until_complete(db.create_table("user_table"))
    loop.run_until_complete(db.create_table("blog_table"))
    loop.run_until_complete(db.disconnect())
