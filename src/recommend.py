import json
import math

# Import manga.json data
with open("../data/manga.json", "r") as file:
    manga_list = json.load(file)

# Get list of all unique genres
all_genres = []
for manga in manga_list:
   all_genres.extend(manga["genres"])
all_genres = sorted(set(all_genres))

# Get list of all unique tags(num of tags is 330)
all_tags = []
for manga in manga_list:
    all_tags += [tag["name"] for tag in manga["tags"]]
all_tags = sorted(set(all_tags))


# Build manga vector using one hot encoding
manga_vectors = []
for manga in manga_list:
    vector = []
    for genre in all_genres:
        if genre in manga["genres"]:
            vector.append(1)
        else:
            vector.append(0)

    # creating dict of tags for easier access
    tags_dict = {item["name"]:item["rank"] for item in manga["tags"]}

    # incorporating tags into manga vector
    for tag in all_tags:
        vector.append(tags_dict.get(tag, 0))


    manga_vectors.append(vector)

    

def cosine_similarity(a, b):
    """Find the angle between two vectors"""
    a_squared = [element*element for element in a]
    magnitude_a = math.sqrt(math.fsum(a_squared))

    b_squared = [element*element for element in b]
    magnitude_b = math.sqrt(math.fsum(b_squared))

    dot_product = 0
    for x, y in zip(a, b):
        dot_product += x*y
    try:
      RHS = dot_product / (magnitude_a * magnitude_b)
    except ZeroDivisionError:
        print("Can't divide by Zero")
        return None
    return RHS


def get_recommendations(manga_index, n):
    """Return the top n recommendations for a manga at manga_index using cosine_similarity function"""
    recommendations = []
    for i in range(len(manga_list)):
        if i == manga_index:
            continue
        similarity = cosine_similarity(manga_vectors[manga_index], manga_vectors[i])
        manga_name = manga_list[i]["title"]["romaji"]
        recommendations.append([similarity, manga_name])
    
    # Sort list in descending order then remove any elements beyond index n
    recommendations.sort(reverse = True)
    recommendations = recommendations[:n]
    return recommendations

#test
print(get_recommendations(4, 15))


    



