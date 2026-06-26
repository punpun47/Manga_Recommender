import requests
import json

url = "https://graphql.anilist.co"

manga_list = []

# loop because anilist caps requests at 50 manga
# doubled {, } to avoid syntax errors with .format()
for i in range(1, 21):
    query = """
    query {{
    Page(page: {0}, perPage: 50) {{
        media(type: MANGA, sort: POPULARITY_DESC) {{
        id
        title {{
            romaji
            native 
            english }}
        genres
        averageScore
        popularity
        tags {{
            name
            rank
        }}
        }}
    }}
    }}
    """.format(i)

    # Get nested dictionary from anilist
    response = requests.post(url, json = {"query": query})
    
    # Add each mangas data onto list individually
    manga_list.extend(response.json()["data"]["Page"]["media"])



with open("../data/manga.json", "w") as file:
    json.dump(manga_list, file, indent = 2)