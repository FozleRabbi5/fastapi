from fastapi import FastAPI
from .routers import users

app = FastAPI(title="Hello FastApi")

app.include_router(users.user_router,prefix="/admin", tags=['Users']
                   , responses={418: {'d': 'p'}}
                   )

