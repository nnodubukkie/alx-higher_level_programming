#!/usr/bin/python3
# Author - Chukwuebuka
"""Print the numbers from 1 to 100 separated by a space.
 For multiple of three, print Fizz instead of the number
 For multiples of five, print Buzz instead of the number.
 For multiple of three and five, print FizzBuzz instead of the number.
 """

def Fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
