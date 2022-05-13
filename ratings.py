"""Restaurant rating lister."""

# put your code here
# open scores.txt and save into a variable
scores = open("scores.txt")
# create an empty dictionary
ratings_dictionary = {}

def sorting_dict(dict):
    ratings_list = dict.items()
    sorted_ratings_list = sorted(ratings_list)
    for restaurant, rating in sorted_ratings_list:
        print(f"{restaurant} has a rating of {rating}")

# loop to iterate over scores.txt file
for score in scores:
    score = score.rstrip()
    scores_list = score.split(":") # why is scores_list iterable?
    # print(scores_list)
    ratings_dictionary[scores_list[0]] = int(scores_list[1])

sorting_dict(ratings_dictionary)
# ratings_list = ratings_dictionary.items()

# sorted_ratings_list = sorted(ratings_list)

# for restaurant, rating in sorted_ratings_list:
#     print(f"{restaurant} has a rating of {rating}")

restaurant_input = input("What restaurant do you want to add? ")
score_input = input("How do you score it? ")

ratings_dictionary[restaurant_input] = score_input

sorting_dict(ratings_dictionary)
# ratings_list = ratings_dictionary.items()

# sorted_ratings_list = sorted(ratings_list)

# for restaurant, rating in sorted_ratings_list:
#     print(f"{restaurant} has a rating of {rating}")

# convert variable into string
# scores_str = scores.read()

# store strings into dictionary
# split string by colon
# scores_strip = scores_str.rstrip()
# 
# print(scores_list)
# iterate over list - save first half as key and other half as value
# sort(dict.keys())

