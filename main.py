# imports
import art
import game_data
import random


# functions
def get_options():
    # this variable get the dictionary from game_data
    main_dict = game_data.data
    # option get one random item from main_dict
    option = main_dict[random.randint(0, len(main_dict) - 1)]

    # return the item randomic from the dict
    return option


# this function return a output, showing name, description and country of option avaliable
def compare_options(option, label):
    print(f"Compare {label}: {option['name']}, a {option['description']}, from {option['country']}")


# check the answer of the user
def check_answer(option_A, option_B, user_choice, score):
    correct_answer = 'a' if option_A['follower_count'] > option_B['follower_count'] else 'b'

    if user_choice == correct_answer:
        score += 1
        return score, False
    else:
        return score, True


# play the game
def play():
    # print logo
    print(art.logo)


    game_over = False
    score = 0


    # main logic
    while not game_over:
        option_A = get_options()
        option_B = get_options()

        # ensures that option A or B don't be equal
        while option_B == option_A:
            option_B = get_options()


        compare_options(option_A, "A")

        print(art.vs)

        compare_options(option_B, "B")

        input_A_or_B = input("Who has more followers? Type 'A' or 'B':").lower()

        score, game_over = check_answer(option_A=option_A, option_B=option_B, user_choice=input_A_or_B, score=score)
        
        if game_over:
            print(f"{'\n' * 100}")
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        else:
            print(f"{'\n' * 100}")
            print(f"You're right! Current score: {score}")


play()