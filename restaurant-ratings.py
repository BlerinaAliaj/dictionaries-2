# your code goes here


def create_dictionary(filename):
    """Creates dictionary of restaurants and scores from file"""

    my_file = open(filename)
    scores_dictionary = {}

    for line in my_file:
        line = line.rstrip().split(":")
        restaurant = line[0]
        score = line[1]

        scores_dictionary[restaurant] = score

    my_file.close()

    return scores_dictionary


scores_dictionary = create_dictionary("scores.txt")


def keep_asking():
    """Asks for restaurant name and scores from user and adds to existing
        dictionary """

    while True:
        answer = raw_input("Would you like to add a restaurant? >y/n ")

        if answer == "y":
            restaurant_score = raw_input("Please enter restaurant and score. ")
            restaurant_score = restaurant_score.split(" ")

            scores_dictionary[restaurant_score[0].title()] = int(restaurant_score[1])
        else:
            return scores_dictionary


def see_restaurant(restaurant_score):
    for restaurant, score in restaurant_score:
        print restaurant, "is rated at", score


user_choise = raw_input("""You have choice!!!! If you'd like to see restaurant
     ratings, press 1; If you'd like to add a new restaurant, press 2; if you'd
     like to quit, press 3. """)

if user_choise == "1":
    restaurant_score = sorted(create_dictionary("scores.txt").items())
    see_restaurant(restaurant_score)
elif user_choise == "2":
    restaurant_score = sorted(keep_asking().items())
    see_restaurant(restaurant_score)
elif user_choise == "3":
    pass
