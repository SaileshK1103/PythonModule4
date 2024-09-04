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
from random import random, choice, uniform

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
    userGuess = input("Guess a number or enter empty string to quit!")
    if userGuess == "":
        print("You choose to exit, good bye")
        break
    userGuess = int(userGuess)

    if userGuess < randomChoice:
        print(f"the guess number is {userGuess} and the random choice is {randomChoice} is vey low")
    elif userGuess > randomChoice:
        print(f"the guessed {userGuess} is vey high {randomChoice} ")
    elif userGuess == randomChoice :
        print(f"the guessed  {userGuess} is correct {randomChoice} " )
        break
'''
#4.5. Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.
'''
correct_username = "python"
correct_password = "rules"
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
print("Acccess denied")
'''

#4.6. Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0).
# Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square.
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with the fraction of
# the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi:
# Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points.
# Each point inside the square is tested for whether it resides inside circle A.
# Let n be the total number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N.
# Write a program that asks the user how many random points to generate, and then calculates the approximate value of pi using
# the method explained above. At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).
'''
#Ask user to generate the number of random points
numPoints =int(input("Enter the number of random points to generate: "))
#Initialize the number of random points in the circle
pointsInsideCircle = 0
index =0
#Generate the random points and check if they are inside the circle
for index in range(numPoints):
    x = uniform(-1,1)
    y = uniform(-1,1)
    #check if the points inside the circle
    if x**2 + y**2 <= 1:
        pointsInsideCircle += 1
#Calculate the approximation of pi
pi_approximation = 4 * pointsInsideCircle/numPoints
#Print the result
print(f"Approximation of π using {numPoints} points: {pi_approximation}")
'''