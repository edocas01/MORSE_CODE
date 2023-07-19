# This file reads a random letter from the alphabet and asks for the respective morse code
import random
import os
from os import name
import time

"""
 
   _____                 _   _                 
  |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
  | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
  |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
  |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
                                               
 
"""

# this function reads the file and returns the letters, codes and names
def read_file(file_name):
    alphabet = open(file_name, "r").read()
    letters = []
    codes = []
    names = []
    index = 0
    while True:
        letters.append(alphabet[0])
        alphabet = alphabet[2:]
        codes.append(alphabet[0:alphabet.find(" ")])
        alphabet = alphabet[alphabet.find(" ")+1:]
        names.append(alphabet[0:alphabet.find("\n")])
        alphabet = alphabet[alphabet.find("\n")+1:]
        index += 1
        if letters[-1] == "Z":
            break
    return letters, codes, names

# this function translate a given phrase in morse code
def translate_phrase(l = None, c = None):
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    while True:
        text_phrase = input("Give the phrase to be translated:\n")
        text_phrase = text_phrase.upper()
        # check if the user wants to exit
        exit_str = "\\"
        if text_phrase == exit_str.upper():
            print("EXITING...")
            break
        # parsing the phrase and remove empty words
        words = text_phrase.split(" ")
        new_words = []
        for x in words:
            if x != "":
                new_words.append(x)
        words = new_words
        solution = ""
        for k in range(len(words)):
            if k > 0:
                solution += " "
            for z in range(len(words[k])):
                idx = l.index(words[k][z])
                solution += c[idx] + " "
        print("The solution is:")
        print(solution)
        tmp = input()
        if tmp == exit_str.upper():
            print("EXITING...")
            break
            
        if name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    

# this function checks if the code associated to a given phrase is correct
def check_phrase(l = None, c = None):
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
    print("=> EXERCISES ON MORSE CODE")
    print("- press \"\\\" to exit the program")
    print("- space the letters in morse code with one space")
    print("- space the words in morse code with two spaces")
    print("==============================================")
    exit_str = "\\"
    while True:
        text_phrase = input("Give the phrase to be checked:\n")
        text_phrase = text_phrase.upper()
        
        # check if the user wants to exit
        if text_phrase == exit_str.upper():
            print("EXITING...")
            break
        # parsing the phrase and remove empty words
        words = text_phrase.split(" ")
        new_words = []
        for x in words:
            if x != "":
                new_words.append(x)
        words = new_words
        
        # check flag to exit the while loop
        check = True
        # exit flag to exit the program from user input
        exit_flag = False
        # counter to count the number of errors
        counter = 0
        
        # give as input the corresponding morse code and check if it is correct
        while check:
            # flag to exit in case of error and return to the request of the morse code
            error_flag = False
            code_phrase = input("Give the corresponding morse code:\n")
            
            # check if the user wants to exit
            if code_phrase == exit_str.upper():
                exit_flag = True
                print("EXITING...")
                break
            
            for i in range(len(words)):
                # remove the second space from the given morse code
                if i > 0:
                    code_phrase = code_phrase[1:]
                    
                # brake the loop if the code is not correct
                if error_flag:
                    break
                
                for j in range(len(words[i])):
                    # find the letter in l corresponding to words[i][j]
                    index = l.index(words[i][j])
                    
                    # parse the letter in the given code
                    if code_phrase.find(" ") == -1:
                        morse_letter = code_phrase
                    else:
                        morse_letter = code_phrase[:code_phrase.find(" ")]
                    
                    # check if the letter is correct
                    if morse_letter != c[index]:
                        print("Wrong answer in letter: ", l[index])
                        print("Try again, the phrase was: " + text_phrase.lower())
                        error_flag = True
                        counter += 1
                        
                        # if the user fails three times, give the solution
                        if counter >= 3:
                            # build up the solution
                            solution = ""
                            for k in range(len(words)):
                                if k > 0:
                                    solution += " "
                                for z in range(len(words[k])):
                                    idx = l.index(words[k][z])
                                    solution += c[idx] + " "
                            
                            print("YOU FAILED MULTIPLE TIMES!")
                            print("The correct answer was: " + solution)
                        break
                    else:
                        # remove the letter from the code
                        code_phrase = code_phrase[code_phrase.find(" ")+1:]
                        
                        # exit the loop if the last letter is correct
                        if i == len(words)-1 and j == len(words[i])-1:
                            check = False
                            print("Correct!")
                            time.sleep(0.5)
                            if name == 'nt':
                                os.system('cls')
                            else:
                                os.system('clear')
       
                            
        if exit_flag:
            break
                        
"""
   __  __       _       
  |  \/  | __ _(_)_ __  
  | |\/| |/ _` | | '_ \ 
  | |  | | (_| | | | | |
  |_|  |_|\__,_|_|_| |_|
                        

"""

letters, codes, names = read_file("alfabeto.txt")
while True:
    string = input("Press 0 to translate or 1 to learn: ")
    if string == "0":
        translate_phrase(letters, codes)
        break
    elif string == "1":
        check_phrase(letters, codes)
        break
    elif string == "\\":
        print("EXITING...")
    else:
        print("Wrong input!")
    
    


