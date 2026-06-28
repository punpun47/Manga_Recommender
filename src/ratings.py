import json
from datetime import date

def load_ratings():
    try:
        with open("../data/ratings.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def save_ratings(manga_ratings):
    with open("../data/ratings.json", "w") as file:
        json.dump(manga_ratings, file, indent = 2)

def add_rating(manga_id, rating, status):
    manga_ratings = load_ratings()
    manga_dict = {
        "manga_id": manga_id,
        "rating": rating,
        "status": status,
        "date_completed": str(date.today())
    }
    manga_ratings.append(manga_dict)
    save_ratings(manga_ratings)

# TESTING
add_rating(30642, 98.1, "Completed")
add_rating(30026, 95.9, "Releasing")
add_rating(30021, 96.9, "Completed")
add_rating(30011, 93.1, "Completed")
add_rating(85135, 99.0, "Completed")
add_rating(118586, 96, "Completed")
add_rating(140475, 100, "Releasing")
add_rating(105469, 90, "Completed")
add_rating(67707, 99, "Completed")


