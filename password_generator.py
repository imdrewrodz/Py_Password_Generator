#Import random to create random variable to mix password, import string to grab alphabet
import random
import string

#Main function that takes password length, boolean to test for number, boolean to test for special characters
def generate_password(min_length, numbers=True, special_characters=True):
    #all letters upper and lower
    letters = string.ascii_letters
    #all numbers 0-9
    digits = string.digits
    #many special punctuations and special chars
    special = string.punctuation

    #initialize characters that will be randomized to generate the password
    characters = letters
    #if numbers are required in the password then add it to characters that can be chosen from
    if numbers:
        characters += digits
    #if special chars are required in the password then add it to characters that can be chosen from
    if special_characters:
        characters += special

    #initialize password    
    pwd = ""
    #condition that changes to true when password meets requirements
    meets_criteria = False
    has_number= False
    has_special = False

    #continues to add characters to the generated password until the password security criteria is met and the length ids over the required amount
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        #if the new generated character is a digit the change has_number to true to display there's a number in the password
        if new_char in digits:
            has_number = True
        #if the new generated character is a special char the change has_number to true to display there's a number in the password
        elif new_char in special:
            has_special = True

        #set criteria to true and try to disprove using parameters
        meets_criteria = True
        #check if numbers are required and if the password contains them
        if numbers:
            meets_criteria = has_number
        #check if special chars are required and if the password contains them
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


min_length = int(input("Enter the minimum length: "))

has_number = input("Do you want numbers (y/n)? ").lower() == 'y'

has_special = input("Do you want special characters (y/n)? ").lower() == 'y'
pwd = generate_password(min_length, has_number, has_special)

print("Your generated password is: ", pwd)