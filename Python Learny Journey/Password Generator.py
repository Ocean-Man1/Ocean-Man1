#DAY 5 
#Password Generator
#This project is a password generator utilizing loops and list indexing in Python

import random
import string

#create lists for each of characters
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?']

char_list = [letters, numbers, symbols]     #create a list of all the characters

#recieve inputs
print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n"))
sym = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

total = let+sym+num     #total characters of password

#main algorithim
password = ''
for i in range(total):       #go until all characters are exhausted
    select = random.randint(0,2)    #generate random int to choose a characters
    
    #check for if all letters, numbers, and symbols have been used
    if (let != 0) and (select == 0):    
        password = password + letters[random.randint(0,len(letters)-1)]
        let -= 1
    
    if (num != 0) and (select == 1):
        password = password + numbers[random.randint(0,len(numbers)-1)]
        num -= 1
        
    if (sym != 0) and (select == 2):
        password = password + symbols[random.randint(0,len(symbols)-1)]
        sym -= 1
        
print(f"Your new password is: {password}")