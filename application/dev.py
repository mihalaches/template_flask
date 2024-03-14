from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import logging
import os

app = Flask(__name__)

def loggerInstance(fileName : str):
    if not os.path.exists("logs/"):
        os.makedir("logs")
    logger = logging.Logger(fileName)
    logger.setLevel = logging.DEBUG
    handler = logging.FileHandler(f"logs/{fileName}.log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(threadName)s %(pathname)s-%(lineno)s (in %(funcName)s): %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


DEBUG = True

MYSQL_HOSTNAME = os.environ.get('MYSQL_DATABASE')
MYSQL_NAME = os.environ.get('MYSQL_NAME')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_PORT = os.environ.get('MYSQL_PORT')

WEATEHR_API = "dev.weather.api"

try:
    engine = create_engine(f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:{MYSQL_PORT}/{MYSQL_NAME}")
    db_session = scoped_session(sessionmaker(autocommit=False,
                                            autoflush=False,
                                            bind=engine))
    Base = declarative_base()
    Base.query = db_session.query_property()

    def init_db():
        try:
            app.logger.info("Database inited!")
            import models
            Base.metadata.create_all(bind=engine)
        except:
            app.logger.exception("Error")
except:
    app.logger.exception("asdsa")