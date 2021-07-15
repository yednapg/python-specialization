# Write a program that uses input to prompt a user for their name and then welcomes them. 
name = input('Enter your name: ')
print('Hello', name)

# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours) * float(rate)

# Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5

# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
celsius = input('Enter temperature in Celsius: ')
fahrenheit = (float(celsius) * 1.8) + 32
print('Temperature in Fahrenheit is', fahrenheit)