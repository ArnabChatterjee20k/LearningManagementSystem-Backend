from system import create_api
from system import celery
app = create_api()
app.app_context().push()