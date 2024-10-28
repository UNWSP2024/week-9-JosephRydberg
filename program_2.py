# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
from random import randrange


def write_numbers():
    totalNumbers = int(input("How many random numbers do you want? (1000 max) "))

    if totalNumbers <= 1000:
        file = open("random_numbers", "w")
        for i in range(0, totalNumbers):
            file.write(str(randrange(0, 500)) + "\n")
    else:
        print("Too large")
write_numbers()