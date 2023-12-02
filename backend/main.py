from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from movies import Movies
movies = Movies(r'movies.txt')

app = FastAPI()

# Cross-Origin Resource Sharing
origins = [
    "https://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Movie(BaseModel):
    movie_id: int = None
    movie_name: str = None
    cast_list: list = None

class New_movie(BaseModel):
    movie_name: str = None
    cast_list: list = None

# Create get method
# Receive id input by user, return movie
@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int):
    return movies.get_movie_by_id(movie_id)

# Create put method
#@app.put("/movies/{movie_id}")
#async def put_movie(movie_id: int, movie: Movie):
#    movies.edit_movie(movie_id, movie.dict(exclude_unset=True))
#    return movies.get_movie_id(movie_id)

# Create delete method
#@app.delete("/movies/{movie_id}")
#async def delete_movie(movie_id: int):
#    deleted_movie = movies.get_movie_by_id(movie_id)
#    movies.delete_movie(movie_id)
#    return deleted_movie

# Create post method
#@app.post("/movies/{movie_id}")
#async def post_movie(movie: New_movie):
#    return movies.add_movie(movie.dict())