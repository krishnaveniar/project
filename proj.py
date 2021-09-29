import random

def hangedman():
    HANGMAN_PICS = [  """
                  
                   --------
                   |      |
                   |      |
                   |      O
                   |    __|__
                   |      |
                   |     / \\
                   -
                   """, """
                  
                   --------
                   |      |
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                   ""","""
                   --------
                   |      |
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                   ""","""
                   --------
                   |      |
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                   ""","""
                   --------
                   |      |
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                   """, 
    """
                   --------
                   |      |
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   
    """
                   --------
                   |      |
                   |      |
                   |      O
                   |      |
                   |
                   |
                   -
                   ""","""
                   --------
                   |      |
                   |      |
                   |      O
                   |      
                   |
                   |
                   -
                   ""","""
                   --------
                   |      |
                   |      |
                   |
                   |
                   |
                   |
                   -
                   """,
           """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |     
                   |      
                   |
                   |
                   |
                   |
                   -
                   """]
    return HANGMAN_PICS
rand_words = ['colorful','comb','neighborly','dangerous','arm','quixotic','superb','omniscient','whine','broken','valuable','fat','examine',
'canvas','applaud',]
def main():
    word= get_word(rand_words)
    game(word)
    again_play=input("Do you wanna play again?\n Y/N\n")
    play =again_play.upper()
    if play =="Y":
        get_word(rand_words)
        game(word)  
    else:
        print("Bye")  

def get_word(rand_words):
    word= random.choice(rand_words)
    return word
def game(word):
    pics =hangedman()
    l= len(word)
    dashes = "_ "* l
    tries=10
    picno =10
    word_letters =list(word)
    guess_letters = []
    used_letters =[]
    print("Let's play Hangman!")
    print(dashes)
    print(pics[picno])
    count = 0
    while tries>0 and len(word) > count  :
        letter = input("Guess a letter!\n") 
       
        if len(letter)==1 and letter.isalpha():
            if letter not in word_letters:
                print(letter ,"is not in word")
                used_letters.append(letter)
                picno -=1
                print (pics[picno])
                tries -=1
            elif letter in used_letters:
                used_letters.append(letter)
                print("You already guessed this letter. Guessed letters are",' '.join(used_letters))
            else :
                print(letter, "is in the word, Nice Try!")
                guess_letters.append(letter)
                used_letters.append(letter)
                tries-=1
            word_list=[letter if letter in guess_letters else '_' for letter in word_letters] 
            count = l- word_list.count('_') 
            print("Current word :",' '.join(word_list))     
        else:
            print("Not a valid guess")

    if count == len(word_letters) :
        print("You Won!,congrats")        
    else:
        print("You lost!, the word was",word.upper())          

main()
