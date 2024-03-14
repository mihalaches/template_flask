from application import app,DEBUG
import database

try:
    app.logger.info("Application started!")
    database.init_db()
except Exception as e:
    app.logger.exception("Db error")

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0",debug=DEBUG)
    except Exception as e:
        app.logger.exception("Application Error :")