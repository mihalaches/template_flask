from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from application import app

try:
    engine = create_engine("mysql://root:123456@172.17.0.1:3366/flask_service_api")
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