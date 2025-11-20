# imports
import art
import game_data
import random

# print logo
print(art.logo)


main_dict = game_data.data

game_over = False

score = 0

while not game_over:
    
    option_A = main_dict[random.randint(1, len(main_dict))]
    option_B = main_dict[random.randint(1, len(main_dict))]


    print(f"Compare A: {option_A["name"]}, a {option_A["description"]}, from {option_A["country"]}")

    print(art.vs)

    print(f"Compare B: {option_B["name"]}, a {option_B["description"]}, from {option_B["country"]}")

    input_A_or_B = input("Who has more followers? Type 'A' or 'B':").lower()

    if option_A["follower_count"] > option_B["follower_count"]:
        if input_A_or_B == 'a':
            score += 1
        elif input_A_or_B == 'b':
            print(f"{'\n' * 100}")
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif option_B["follower_count"] > option_A["follower_count"] :
        if input_A_or_B == 'b':
            score += 1

        elif input_A_or_B == 'a':
            print(f"{'\n' * 100}")
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    
    print(f"{'\n' * 100}")
    print(f"You're right! Current score: {score}")