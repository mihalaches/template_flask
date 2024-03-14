from application import app
from modules.user import handlers


## USERS

app.add_url_rule("/users/home",'home',handlers.home)
app.add_url_rule("/users/get/<user_id>","get_user",handlers.get)
app.add_url_rule("/users/get_all","get_all_users",handlers.get_all)