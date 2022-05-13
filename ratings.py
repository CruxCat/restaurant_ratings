"""Restaurant rating lister."""

# put your code here
# open scores.txt and save into a variable
scores = open("scores.txt")
# create an empty dictionary
ratings_dictionary = {}
# loop to iterate over scores.txt file
for score in scores:
    score = score.rstrip()
    scores_list = score.split(":") # why is scores_list iterable?
    # print(scores_list)
    ratings_dictionary[scores_list[0]] = int(scores_list[1])

ratings_list = ratings_dictionary.items()

sorted_ratings_list = sorted(ratings_list)

for restaurant, rating in sorted_ratings_list:
    print(f"{restaurant} has a rating of {rating}")

# convert variable into string
# scores_str = scores.read()

# store strings into dictionary
# split string by colon
# scores_strip = scores_str.rstrip()
# 
# print(scores_list)
# iterate over list - save first half as key and other half as value
# sort(dict.keys())

# prompt user for restaurant name