# This file reads a random letter from the alphabet and asks for the respective morse code
import random

"""
   ____        __ _       _ _   _                 
  |  _ \  ___ / _(_)_ __ (_) |_(_) ___  _ __  ___ 
  | | | |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \/ __|
  | |_| |  __/  _| | | | | | |_| | (_) | | | \__ \
  |____/ \___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
                                                  
 
"""
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



"""
 
   __  __       _       
  |  \/  | __ _(_)_ __  
  | |\/| |/ _` | | '_ \ 
  | |  | | (_| | | | | |
  |_|  |_|\__,_|_|_| |_|
                        
 
"""
letters, codes, names = read_file("alfabeto.txt")
request_letter(letters,codes,names)




