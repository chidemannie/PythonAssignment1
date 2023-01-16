#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:21:45 2023

@author: emmanuelbenyeogor
"""
echo "# PythonAssignment1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/chidemannie/PythonAssignment1.git
git push -u origin main
# Q 1
# This code prompts the user to enter how many Fibonacci numbers they would 
# like to generate, and then generates and prints that many Fibonacci numbers 
# using a function called fibonacci(). 

def fibonacci(n):

  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fib_list = [0, 1]
    for i in range(2, n):
      fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

num_fib = int(input("How many Fibonacci numbers would you like to generate? "))
print(fibonacci(num_fib))


# Q2 This code prompts the user to enter a long string, and then uses a function called reverse_words() to reverse the order of the words in the string. The function first splits the string into a list of words using the split() method. Then, it uses string slicing to reverse the order of the words in the list. The reversed words are then joined together into a new string using the join() method, and returned.
def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

def main():
    user_input = input("Please enter a long string: ")
    reversed_string = reverse_words(user_input)
    print(reversed_string)

if __name__ == "__main__":
    main()
    
# Q3 This code prompts the user to enter a string and then uses a function called is_palindrome() to check if the string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same forward and backward. The function uses string slicing to reverse the string and then compares it with the original input. If the two are the same, the function returns True, indicating that the input is a palindrome. If the two are not the same, the function returns False, indicating that the input is not a palindrome.  
def is_palindrome(string):
    return string == string[::-1]

def main():
    user_input = input("Please enter a word you think is palindromic i.e. reads the same forwards and backwards:")
    if is_palindrome(user_input):
        print("The word you entered is a palindrome.")
    else:
        print("The word you entered is not a palindrome.")

if __name__ == "__main__":
    main()

# Q3a To help to find a palindrome if any exists in the string
def find_palindrome(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if string[i:j] == string[i:j][::-1]:
                return string[i:j]
    return "No palindrome found."

# Q3b To help to find a palindrome if any exists in the string
def main():
    user_input = input("Please enter a string: ")
    palindrome = find_palindrome(user_input)
    print("The longest palindrome found in the string is:", palindrome)

if __name__ == "__main__":
    main()
    
# Q3c To help to create a palindrome from the word entered
def create_palindrome(string):
    return string + string[::-1]

def main():
    user_input = input("Please enter a string: ")
    palindrome = create_palindrome(user_input)
    print("The created palindrome is:", palindrome)

if __name__ == "__main__":
    main()

# Q4 This code creates a dictionary of names and birthdays of the great individuals listed, and allows the user to enter a name and return the corresponding birthday:
print("Welcome to the birthday dictionary. We know the birthdays of:")    
birthdays = {"Albert Einstein": "03/14/1879", 
             "Benjamin Franklin": "01/17/1706", 
             "Emmanuel Benyeogor": "09/12/1987", 
             "Ada Lovelace": "12/10/1815"}
for name in birthdays.keys():
    print(name)

name = input("Who's birthday do you want to look up? (Enter any name from list above)")

# convert name to lowercase to match dictionary keys
name = name.lower()

# use the in operator to check if any of the dictionary keys contain the user's input
matches = [k for k in birthdays.keys() if name in k.lower()]
if matches:
    match = matches[0]
    print(f"{match}'s birthday is {birthdays[match]}.")
else:
    print(f"Sorry, we don't have any record of  {name}.")


# Q5 This script uses the requests.get() function to fetch the HTML of the New York Times homepage, and then uses the BeautifulSoup class to parse the HTML. The soup.find_all() method is used to find all the h2 tags with class css-1cmu9py e1voiwgp0 and extract the text of the titles, which are then printed using a for loop.
# Please note that: web scraping the website without the permission of the website owner is against the terms of service of many websites and might cause the IP to be banned from accessing the website. Also, the website might change the structure of the HTML and the script might not work as expected.    
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all article titles
titles = soup.find_all('h2', class_='css-4jyr1y')

# Print the titles
for title in titles:
    print(title.text)
  
    
# Q6 This script uses the open() function to create a file called titles.txt in the same directory as the script, and then opens it in "write" mode ('w'). The with open statement is used to open the file and automatically handle closing it after all the indented code underneath it has been executed. The script then uses a for loop to iterate over each title and writes the text of each title to the file, followed by a newline ('\n').

# Write the titles to a file
with open('titles.txt', 'w') as file:
    for title in titles:
        file.write(title.text + '\n')



