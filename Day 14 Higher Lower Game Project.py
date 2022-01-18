from operator import truediv
from pickle import FALSE, TRUE
import random

from random import randint

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 63,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 62,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 58,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 56,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 52,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 52,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]


# # AUTHOR PHENSIC ME 😊


# chosen = (random.choice(data))
# for keys in chosen:
#     nameA = chosen['name'] 
#     descriptionA = chosen['description'] 
#     countryA = chosen['country'] 
#     followers = chosen["follower_count"]

# chosen_B = (random.choice(data))
# for keys in chosen_B:
#     name_B = chosen_B['name'] 
#     description_B = chosen_B['description'] 
#     country_B= chosen_B['country'] 
#     followers_B = chosen_B["follower_count"]

# def next_round():
#     """Generates another set of random account to ask the user """
#     global name_B, description_B, country_B, followers_B
#     nameA = name_B 
#     descriptionA = description_B 
#     countryA = country_B 
#     followers = followers_B

#     chosen_B = (random.choice(data))
#     for keys in chosen_B:
#         name_B = chosen_B['name'] 
#         description_B = chosen_B['description'] 
#         country_B= chosen_B['country']
#         followers_B = chosen_B["follower_count"]

#     print(f"Compare A: {nameA}, a {descriptionA}, from {countryA} \n")

#     print("VS \n")

#     print(f"Compare B: {name_B}, a {description_B}, from {country_B} \n")


# print("Welcome To The HIGHER LOWER Game... \n")
# print(f"Compare A: {nameA}, a {descriptionA}, from {countryA} \n")

# print("VS \n")

# print(f"Compare B: {name_B}, a {description_B}, from {country_B} \n")

# score = 0
# user_correct = True


# while user_correct == True:

#     Your_answer = input("Who has more followers 'A' or 'B': ")

#     if Your_answer == "A" and followers > followers_B:
#         score += 1
#         next_round()
#         print("Your Right!")
#         print(f"Your current score is {score}")
#     elif Your_answer == "B" and followers_B > followers:
#         score += 1
#         next_round()
#         print("Your Right!")
#         print(f"Your current score is {score}")
#     elif Your_answer != 'A' and Your_answer != 'B':
#         print("Invalid Input")
#         user_correct = False
#     elif Your_answer == 'A' and followers_B > followers:
#         print("You're Wrong")
#         user_correct = False
#     elif Your_answer == 'B' and followers > followers_B:
#         print("You're Wrong")
#         user_correct = False
#     else:
#         user_correct = False


# COURSES SOLUTION
def format_data(account):
    """Format the account into a printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

    # Score keeping


score = 0
game_should_continue = True
# account_b = random.choice(data)
account_a = random.choice(data)
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data
    # Making the account at position B become the next at position
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print("VS")
    print(f"Compare B: {format_data(account_b)}.")

    # Ask the user for a guess.
    guess = input("Who ha more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # --Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_a['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # --Use the "if statement" if user is correct
    if is_correct:
        score += 1
        print(f"Your correct! Current score {score}")
    else:
        game_should_continue = False
        print("Sorry, that's wrong. Final score {score}")

# FINITE
