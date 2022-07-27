from fastapi import FastAPI
from app.api.router import router
from fastapi_pagination import add_pagination

app = FastAPI()
add_pagination(app)
app.include_router(router)