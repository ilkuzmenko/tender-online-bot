import logging

from loader import db


async def add_user(user_id, phone, first_n, last_n):
    await db.execute('''
    INSERT INTO users (user_id, phone, first_name, last_name) VALUES ($1, $2, $3, $4)
    ON CONFLICT DO NOTHING
    ''', user_id, phone, first_n, last_n)
    logging.info("User " + str(user_id) + " added to table")


async def subscribe_user(status, user_id):
    await db.execute('UPDATE users SET blog = $1 WHERE user_id = $2', status, user_id)
    logging.info("User " + str(user_id) + " subscribe blog status " + str(status))
