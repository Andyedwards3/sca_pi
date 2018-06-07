
import random
i = 0
num_random_numbers = 12
while i < 10:
      random_number = random.randint(1,200)
      guessed_random_number = int(raw_input("Guess an integer(bewtween 1 and 200): "))
      print random_number
      i=i+1

