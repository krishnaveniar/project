import random
rand_words = ['colorful','comb','neighborly','dangerous','arm','quixotic','superb','omniscient','whine','broken','valuable','fat','examine']

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
    guess_letters = []
    print("Let's play Hangman!")
    print(dashes)
    while tries>0:
          letter = input("Guess a letter!")
          if len(letter)==1 and letter.isalpha():
              if letter not in word:
                  print(letter ,"is not in word")
                  tries -=1
              elif letter in guess_letters:
                  print("You already guessed these letters",guess_letters)
              else :
                  print(letter, "is in the word, Nice Try!")
                  guess_letters.append(letter)

main()


