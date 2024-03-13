import os

ENV = os.environ.get('APP_ENV')
if ENV == "development":
    from application.dev import *
elif ENV == "production":
    from application.prod import *
elif ENV == "test":
    from application.test import *

from application import urls