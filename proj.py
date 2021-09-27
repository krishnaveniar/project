import random
rand_words = ['colorful','comb','neighborly','dangerous','arm','quixotic','superb','omniscient','whine','broken','valuable','fat','examine',
'canvas','applaud']
def main():
    word= get_word(rand_words)
    game(word)
    

def get_word(rand_words):
    word= random.choice(rand_words)
    return word
def game(word):
    l= len(word)
    dashes = "_ "* l
    tries=10
    word_letters =list(word)
    guess_letters = []
    used_letters =[]
    print("Let's play Hangman!")
    print(dashes)
    while tries>0 and len(word)!= len(guess_letters)  :
        letter = input("Guess a letter!\n") 
       
        if len(letter)==1 and letter.isalpha():
            if letter not in word_letters:
                print(letter ,"is not in word")
                used_letters.append(letter)
                tries -=1
            elif letter in used_letters:
                used_letters.append(letter)
                print("You already guessed this letter. Guessed letters are",' '.join(set(used_letters)))
            else :
                print(letter, "is in the word, Nice Try!")
                guess_letters.append(letter)
                used_letters.append(letter)
                tries-=1
        else:
            print("Not a valid guess")
        word_list=[letter if letter in guess_letters else '_' for letter in word_letters]
        print("Current word :",' '.join(word_list))     

    if len(guess_letters)== len(word_letters) :
        print("You Won!, Congrats")        
    else:
        print("You lost!, you ran out of tries the word was",word.upper())          


main()


