import aiomysql
import logging
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB_NAME

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


class Database:
    """ Реалізація класу для роботи з MySQL """
    def __init__(self):
        self.pool = None

    async def create_pool(self) -> None:
        """ Ініціалізація з'єднання з MySQL """
        if self.pool is None:
            self.pool = await aiomysql.create_pool(
                host=MYSQL_HOST,
                port=3306,
                user=MYSQL_USER,
                password=MYSQL_PASS,
                db=MYSQL_DB_NAME,
                autocommit=True
            )
            logging.info("Successfully initialized database connection")
