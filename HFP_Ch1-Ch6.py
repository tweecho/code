# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:17:36 2019

@author: Arlene
"""



from math import sqrt
def pythagoras( a, b ):
    return sqrt( a * a + b * b )
c = pythagoras( 3, 4 )
print( c )

# this function returns two values
def fun():
    str = "anyone"
    x = 20
    return str, x; # return two values
# code to test above method
str, x = fun() # assign returned tuple
print(str)
print(x)

a = "Hello"
if isinstance( a, int ):
    print( "integer" )
elif isinstance( a, float ):
    print( "float" )
elif isinstance( a, str ):
    print( "string" )
else:
    print( "other" )

GUESSES_ALLOWED = 10
SECRET_WORD = "caribou"

guesses_left = GUESSES_ALLOWED
guessed_word = None

while guessed_word != SECRET_WORD and guesses_left:
    guessed_word = input("Guess a word: ")
    if guessed_word == SECRET_WORD:
        print("You guessed! Congratulations!")
    else:
        guesses_left -= 1
        print("Incorrect! You have", guesses_left,"guesses left.")

for x in range( 10 ):
    print( x )
    if( x == 5 ):
        break

for fruit in ( "apple", "orange", "kiwi" ):
    print( fruit )
else:
    print( "fruit is now", fruit )
print( "Done" )

fruit = "banana"
for letter in fruit:
    
    if letter == "n":
            fruit = "orange"
            for i in fruit:
                print(i)
    print( letter )
print( "Done" )

class Athlete():
    def __init__(self, a_name, a_dob=None, a_times = []):
        #this code is to initialize an 'Athlete' object
        self.name = a_name
        self.dob = a_dob
        self.times = a_times


def print_lol(the_list):
    """
    This is a function to print all item from nested list
    """
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)

def print_lol_1(the_list, indent = False, level=0):
    """
    This is the nester.py module and it provides one function called
    print_lol_1() which prints lists that may or may not include 
    nested lists.
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol_1(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end=" ")
            print(each_item)

from distutils import setup

setup(
      name = 'nester',
      version = '1.3.0',
      py_modules = ['nester'],
      author = 'python',
      author_email = 'www@ww.com',
      url = 'http://www.ddd.com',
      description = 'A simple printer of nested lists',
      )

# python3 setup.py sdisk upload