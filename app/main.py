from fastapi import FastAPI

from app.routers.users import router as router_users

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Гойда!"}


app.include_router(router_users)