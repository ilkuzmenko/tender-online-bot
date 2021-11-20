import aiomysql
import logging
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASS


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


class Database:
    """ Реалізація класу для роботи з MySQL """
    def __init__(self):
        self.connection = None

    async def connect(self) -> None:
        """ Ініціалізація з'єднання з MySQL """
        if self.connection is None:
            self.connection = await aiomysql.connect(host=MYSQL_HOST, port=3306,
                                                     user=MYSQL_USER, password=MYSQL_PASS,
                                                     db="mydb", autocommit=True)
            logging.info("Successfully initialized database connection")
