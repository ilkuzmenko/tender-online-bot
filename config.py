import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']
ADMINS = os.environ['ADMINS']

I18N_DOMAIN = 'bot'
LOCALES_DIR = Path(__file__).parent

MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASS = os.environ['MYSQL_PASS']
MYSQL_DB_NAME = os.environ['MYSQL_DB_NAME']

ES_HOST = os.environ['ES_HOST']
ES_USER = os.environ['ES_USER']
ES_PASS = os.environ['ES_PASS']
