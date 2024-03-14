from application import app,loggerInstance
from modules.user import handlers
from flask import json
from werkzeug.exceptions import HTTPException
from lib.constants import UrlPaths

_logger = loggerInstance("errors")
## USERS

app.add_url_rule(f"{UrlPaths.users}/home", 'home',handlers.home, methods = ["GET"])
app.add_url_rule(f"{UrlPaths.users}/get/<user_id>","get_user",handlers.get)
app.add_url_rule(f"{UrlPaths.users}/get_all","get_all_users",handlers.get_all)
app.add_url_rule(f"{UrlPaths.users}/add", "add_new_user", handlers.add_user)





###### ERROR HANDLER ###########
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    _logger.exception(e)
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response