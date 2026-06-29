from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from ratings import add_rating
from recommend import get_recommendations_np, get_taste_recommendations, name_to_index
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

#To get around browser blocking the reequest
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="../static"), name="static")

@app.get("/")
def root():
    return {"message": "Manga Recommender API"}

@app.get("/manga")
def get_manga():
    with open("../data/manga.json", "r") as file:
        return json.load(file)
    
@app.get("/ratings")
def get_ratings():
    with open("../data/ratings.json", "r") as file:
        return json.load(file)
    
@app.get("/recommendations/taste")
def taste_recommendations():
    return get_taste_recommendations(15)

@app.get("/recommendations/{manga_name}")
def get_manga_recommendations(manga_name: str):
    manga_index = name_to_index(manga_name)
    return get_recommendations_np(manga_index, 15)


class Rating(BaseModel):
    manga_id: int
    rating: float
    status: str

@app.post("/ratings")
def post_rating(rating: Rating):
    add_rating(rating.manga_id, rating.rating, rating.status)
    return {"message": "Rating added"}
