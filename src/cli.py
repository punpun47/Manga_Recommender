import json
from recommend import get_recommendations_np, name_to_index, get_taste_recommendations
from ratings import add_rating

with open("../data/manga.json", "r") as file:
    manga_list = json.load(file)

def print_menu():
    print("")
    print("0: Get id based on name")
    print("1: Get recommendations based on a manga")
    print("2: Get personal taste recommendations")
    print("3: Add Rating")
    print("4: quit")


while True:
    print_menu()
    user_input = input("Enter Choice: ")
    if user_input == "0":
        manga_name = input("Enter manga name: ")
        index = name_to_index(manga_name)
        id = manga_list[index]["id"]
        print(id)
        

    elif user_input == "1":
        manga_name = input("Enter manga name: ")
        manga_index = name_to_index(manga_name)
        for i, (score, title) in enumerate(get_recommendations_np(manga_index, 15)):
            print(f"{i+1}. {title} ({score:.2f})")
        
    elif user_input == "2":
        for i, (score, title) in enumerate(get_taste_recommendations(15)):
            print(f"{i+1}. {title} ({score:.2f})")
    elif user_input == "3":
        id = input("Enter manga id: ")
        user_rating = input("Enter rating: ")
        user_status = input("Enter status: ")
        add_rating(id, user_rating, user_status)
    elif user_input == "4":
        break
    else:
        print("Invalid Input")
