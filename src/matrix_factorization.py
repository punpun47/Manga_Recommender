import numpy as np
from recommend import id_to_index, set_up
from ratings import load_ratings

manga_list, manga_matrix, all_genres, all_tags = set_up()

#load_ratings
ratings = load_ratings()

#set number of loops for epoch
num_epoch = 1000
# set learning rate
learning_rate = 0.001


# Initialize user and manga matrices
U = np.random.normal(0, 0.1, size = (1, 10))
M = np.random.normal(0, 0.1, size = (1000, 10))


for epoch in range(num_epoch):
    loss = 0
    for rating in ratings:
        manga_index = id_to_index(rating["manga_id"], manga_list) 
        r = rating["rating"] / 100 # get the actual rating
        predicted_rating = np.dot(U[0], M[manga_index])
        error = r - predicted_rating
        U[0] += learning_rate * error * M[manga_index]
        M[manga_index] += learning_rate * error * U[0]
        loss += error * error
    print(loss)
