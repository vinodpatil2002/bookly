from fastapi import APIRouter


auth_router = APIRouter()


@auth_router.post("/signup")
async def create_user_account():
    pass


@auth_router.post("/signin")
async def login_user():
    pass


@auth_router.post("/signout")
async def logout_user():
    pass
