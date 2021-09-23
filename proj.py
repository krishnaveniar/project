import random
rand_words = ['colorful','comb','neighborly','dangerous','arm','quixotic','superb','omniscient','whine','broken','valuable','fat','examine']
def get_word():
    myword= random.choice(rand_words)
    return myword
def game():
    word= get_word()
    l= len(word)
    dashes="_" * l
    print("Let's play Hangman!\n")

