from fastapi import FastAPI

from app.routers.users.users import router as router_users
from app.routers.favorite_films.favorite_films import router as router_favorite_films
from app.routers.favorite_genres.favorite_genres import router as router_favorite_genres
from app.routers.viewed.viewed import router as router_viewed

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Гойда!"}


app.include_router(router_users)
app.include_router(router_favorite_films)
app.include_router(router_favorite_genres)
app.include_router(router_viewed)
