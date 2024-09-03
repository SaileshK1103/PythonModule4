#4. While loops(while)
#4.1. Write a program that uses a while loop to print out all numbers divisible by three in the
# range of 1-1000.
'''
range_object = range(1,1000)
index = 0
while index < len(range_object):
    value = range_object[index]
    if value % 3 == 0:
        print(f"The number is divisible by 3 {value}")
    index += 1
'''
from random import random, choice

#4.2. Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.
'''
input_inches  = float(input("Enter a positive number in inches: "))
while input_inches > 0:
    centimeter = input_inches * 2.54
    print(f"the entered{input_inches}inches is {centimeter} centimeter")
    input_inches = float(input("Enter a positive number in inches: or 0 to quit"))

'''

#4.3. Write a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.
'''
userInputList = []
while True:
    user_input = input("Enter a number or enter empty string to quit!")
    if user_input == "":
        break
    number = float(user_input)
    userInputList.append(number)
if userInputList:
    smallest = min(userInputList)
    largest = max(userInputList)
    print(f"The smallest number is {smallest}")
    print(f"The largest number is {largest}")
else:
    print("No numbers entered!")
'''

#4.4. Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.
'''
randomChoice =  choice(range(1,10))
while True:
    userGuess = float(input("Guess a number or enter empty string to quit!"))
    if userGuess == "":
        break
    if userGuess < randomChoice:
        print(f"the guess number is {userGuess} and the random choice is {randomChoice} is vey low")
    elif userGuess > randomChoice:
        print("the guessed is vey high")
    elif userGuess == randomChoice :
        print("the guessed is correct")
'''