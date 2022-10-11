"""
Title: Random Password Generator
Author: Michał Chojna
Date: 05.06.2022
Description: Generates random password accordingly to user's preferences
"""

# Imports modules
import random

# List of uppercase and lowercase letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '-', '+', '=', '[', '{', '}', ']', ';', ':', '/"', '|', '<', ',',
           '>', '.', '?', '/']

# List of number
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Prints welcome message
print("Welcome to the PyPassword Generator!")

# Takes the number of letter user wants to have in the password
letters_num = int(input("How many letters would you like  in your password? "))

# Takes the number of symbols user wants to have in the password
symbols_num = int(input("How many symbols would you like in your password? "))

# Takes the number of numbers user wants to have in the password
numbers_num = int(input("How many numbers would you like in your password? "))

# Creates a list of characters which will be in user's password
password_list = []

# Takes according number of letters from letters list to create password
for num in range(0, letters_num):

    # Add random letter to user's password
    password_list.append(random.choice(letters))

# Takes according number of symbols from symbols list to create password
for num in range(0, symbols_num):

    # Add random symbol to user's password
    password_list.append(random.choice(symbols))

# Takes according number of numbers from numbers list to create password
for num in range(0, numbers_num):

    # Add random number to user's password
    password_list.append(random.choice(numbers))

# Shuffles the order of characters in user's password to be random
random.shuffle(password_list)

# Creates a string of the password
password = ""

# Convert list of characters to string
for char in password_list:

    # Add every character from password list to password string
    password += char

# Prints randomly generated password
print(password)
