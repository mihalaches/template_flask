from application import app,DEBUG
import database

app.logger.info("Application started!")
database.init_db()

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0",debug=DEBUG)
    except:
        app.logger.exception("s")