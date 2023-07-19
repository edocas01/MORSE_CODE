# This file reads a random letter from the alphabet and asks for the respective morse code
import random

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


# this function requests a letter and checks if the code is correct
def request_letter(l,c,n):
    if len(l) != len(c) or len(l) != len(n):
        return False
    letter = random.randint(0,len(l)-1)
    print("Letter: " + l[letter])
    code = input("Code: ")
    if code == c[letter]:
        print("Correct!")
        return True
    else:
        print("Incorrect! The correct answer was " + c[letter])
        False

# this function checks if the code associated to a given phrase is correct
def check_phrase(l = None, c = None):
    print("=> EXERCISES ON MORSE CODE")
    print("- press \"exit\" to exit")
    print("- space the letters in morse code with one space")
    print("- space the words in morse code with two spaces")
    print("==============================================")
    exit_str = "exit"
    while True:
        text_phrase = input("Give the phrase to be checked:\n")
        text_phrase = text_phrase.upper()
        if text_phrase == exit_str.upper():
            break
        # parsing the phrase
        words = text_phrase.split(" ")
        new_words = []
        for x in words:
            if x != "":
                new_words.append(x)
        words = new_words
        print(words)
        # give as input the corresponding morse code and check if it is correct
        check = True
        while check:
            code_phrase = input("Give the corresponding morse code:\n")
            for i in range(len(words)):
                for j in range(len(words[i])):
                    if words[i][j] != ..... # TO BE CONTINUED
            
            check = False
"""
   __  __       _       
  |  \/  | __ _(_)_ __  
  | |\/| |/ _` | | '_ \ 
  | |  | | (_| | | | | |
  |_|  |_|\__,_|_|_| |_|
                        
 
"""

letters, codes, names = read_file("alfabeto.txt")
check_phrase(letters, codes)





