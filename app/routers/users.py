from fastapi import APIRouter

user_router = APIRouter()
## use it for path operation
## You can think of APIRouter as a "mini FastAPI" class.

@user_router.get("/users")
async def users():
    return {"hello": "user"}
