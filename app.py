import math
from random import random

name = input("Hello! What is your name?: ");

while name == '' or name == None :
    name = input("Hello! What is your name?: ");

print(name + ", I made a number from 1 to 100. Try to guess it in the least number off attempts. After each attempt, I will say 'little', 'a lot' or guessed'.");
w = input('Do you want to play? Press Y/N: ');
if w == "Y" or w == "Yes" or w == "yes":
    number = math.ceil(random() * 100);
    guess = input("What number did i make?: ");
    numberOfGuess = 0;

    while guess != str(number) :
        if guess > str(number) :
            guess = input("A lot. Try again: ");
            numberOfGuess = numberOfGuess + 1;
        elif guess < str(number) :
            guess = input("Little. Try again: ");
            numberOfGuess = numberOfGuess + 1;

    print("You guessed! That number " + str(number) + ". You needed " + str(numberOfGuess) + " attempts.");

if w == "N" or w == "No" or w == "no":
    print("Ok! Goodbye");

