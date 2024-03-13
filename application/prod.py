from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

DEBUG = False

MYSQL_HOSTNAME = ""
MYSQL_NAME = ""
MYSQL_USER = ""
MYSQL_PASSWORD = ""
MYSQL_PORT = ""
