# Info
  # - Guess number between 1 and 100
  # - Two modes: easy and hard
  # - Easy mode: 5 attempts
  # - Hard mode: 10 attempts

# ToDos
  # - functionality to set attempts based on the difficulty user has chosen
  # - functionality to generate numbers between 1 and 100
  # - functionality to iterate over # of attempts times and inform user whether they got it or not

from art import text
import random

# Name of the game
print(text)

# Constants
EASY = 'easy'
HARD = 'hard'

# Welcome text
print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

# Get the difficulty
difficulty = input('Choose a diffculty. Type \'easy\' or \'hard\': ').lower()

# Set attempts based on difficulty
def set_attempts(difficulty: str):
  if difficulty == EASY:
    return 10
  if difficulty == HARD:
    return 5
  return 0

# Generate number between 1 and 100
def get_random():
  return random.randint(1, 100)


# Process user's guess
def guess(attempts: int, secret_number: int):
  if attempts == 0:
    print('Unknown difficulty')
  else:
    while attempts > 0:
      print(f'You have {attempts} attempts remaining to guess the number.')
      try:
        guess = int(input('Make a guess: ')) 
        if guess == secret_number:
          print(f'You got it! The answer was {guess}')
          break
        else:
          print('Too low' if guess < secret_number else 'Too high')
      except ValueError:
        print('Enter a valid number.')
      attempts -= 1
    else:
      print('You\'ve run out of guesses, you lose.')

attempts = set_attempts(difficulty)
secret_number = get_random()

guess(attempts, secret_number)
