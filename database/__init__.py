from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import os
from application import app


try:
    engine = create_engine(f"mysql://{os.environ.get('MYSQL_USER')}:{os.environ.get('MYSQL_PASSWORD')}@{os.environ.get('MYSQL_DATABASE')}:3366/{os.environ.get('MYSQL_NAME')}")
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
            app.logger.exception("pl")
except:
    app.logger.exception("asdsa")