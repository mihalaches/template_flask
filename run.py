from application import app,DEBUG,init_db

try:
    app.logger.info("Application started!")
    init_db()
except Exception as e:
    app.logger.exception("Db error")

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0",debug=DEBUG)
    except Exception as e:
        app.logger.exception("Application Error :")