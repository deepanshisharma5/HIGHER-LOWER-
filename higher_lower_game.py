#project-27
#higher lower game

import random
from datetime import datetime

search_data = {
    "Dubai": 2740000,
    "Piano": 6120000,
    "Teacher Training": 22200,
    "Samsung Galaxy S6": 1830000,
    "Body Odour": 14800,
    "Shaquille O'Neal": 550000,
    "City Of God": 110000,
    "Wii Sports": 49500,
    "Son Of Anarchy": 1000000,
    "Los Angeles": 2240000,
}

def get_guess(time_limit=None):
    prompt = "Your guess (yes/no)"
    if time_limit:
        prompt += " - you have 10 seconds"
    start_time = int(datetime.now().strftime("%S"))
    guess = input(f"{prompt}: ")
    end_time = int(datetime.now().strftime("%S"))
    
    if time_limit and (end_time - start_time) > time_limit:
        print("Sorry, you ran out of time!")
        return None
    return guess

def higher_lower_game():
    print("Welcome to the Higher Lower Game!")
    mode = input("Choose a mode: '1' for no time limit, '2' for 10 seconds time limit: ")

    if mode == '2':
        time_limit = 10
    else:
        time_limit = None

    score = 0
    terms = list(search_data.keys())

    while len(terms) > 1:
        term1, term2 = random.sample(terms, 2)
        print(f"Does '{term1}' have more average monthly searches than '{term2}'? (yes/no)")
        guess = get_guess(time_limit)

        if guess is None:
            break
        if guess not in ['yes', 'no']:
            print("Invalid input, please enter 'yes' or 'no'.")
            continue

        correct = (guess == 'yes' and search_data[term1] >= search_data[term2]) or (guess == 'no' and search_data[term1] < search_data[term2])
        if correct:
            print("You guessed it right!")
            score += 1
        else:
            print(f"Sorry, you guessed it wrong. '{term1}' has {search_data[term1]} searches and '{term2}' has {search_data[term2]} searches.")
            break

        print(f"Your current score is: {score}\n")

    print(f"Game over! Your final score is: {score}")

higher_lower_game()
