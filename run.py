from application import app,DEBUG,init_db
from application import loggerInstance

_logger = loggerInstance("run")

try:
    _logger.info("Start init database!")
    init_db()
except Exception as e:
    _logger.exception("Db error")

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0",debug=DEBUG)
    except Exception as e:
        _logger.exception("Application Error :")