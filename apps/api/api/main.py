from fastapi import FastAPI
from fastapi_pagination import add_pagination
from api.config import settings
from api.db import init_db
from identity import routes as identity

app = FastAPI(title=settings.APP_NAME, description=settings.APP_DESCRIPTION, version="0.0.1")

# TODO: Remove once migrations are in play
@app.on_event("startup")
def on_startup():
    # drop_tables()
    init_db()


app.include_router(identity.router, prefix="/v1/identity", tags=["identity"])

add_pagination(app)
